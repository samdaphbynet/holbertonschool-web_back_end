# Pagination

## Learning Objectives

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

### Pagination
Most endpoints that returns a list of entities will need to have some sort of pagination.

Without pagination, a simple search could return millions or even billions of hits causing extraneous network traffic.

Paging requires an implied ordering. By default this may be the item’s unique identifier, but can be other ordered fields such as a created date.

### Offset Pagination
This is the simplest form of paging. Limit/Offset became popular with apps using SQL databases which already have LIMIT and OFFSET as part of the SQL SELECT Syntax. Very little business logic is required to implement Limit/Offset paging.

Limit/Offset Paging would look like GET /items?limit=20&offset=100. This query would return the 20 rows starting with the 100th row.

#### Example
(Assume the query is ordered by created date descending)

- Client makes request for most recent items: GET /items?limit=20
- On scroll/next page, client makes second request GET /items?limit=20&offset=20
- On scroll/next page, client makes third request GET /items?limit=20&offset=40
- As a SQL statement, the third request would look like:

```
SELECT
    *
FROM
    Items
ORDER BY Id
LIMIT 20
OFFSET 40;
```

#### Benefits
- Easiest to implement, almost no coding required other than passing parameters directly to SQL query.

- Stateless on the server.

- Works regardless of custom sort_by parameters.

#### Downsides
- Not performant for large offset values. Let’s say you perform a query with a large offset value of 1000000. The database needs to scan and count rows starting with 0, and will skip (i.e. throw away data) for the first 1000000 rows.

- Not consistent when new items are inserted to the table (i.e. Page drift) This is especially noticeable when we are ordering items by newest first. Consider the following that orders by decreasing Id:

    - Query GET /items?offset=0&limit=15
    - 10 new items added to the table
    - Query GET /items?offset=15&limit=15 The second query will only return 5 new items, as adding 10 new items moved the offset back by 10 items. To fix this, the client would really need to offset by 25 for the second query GET /items?offset=25&limit=15, but the client couldn’t possibly know other objects being inserted into the table.
    Even with limitations, offset paging is easy to implement and understand and can be used in applications where the data set has a small upper bounds.

### Keyset Pagination
Keyset pagination uses the filter values of the last page to fetch the next set of items. Those columns would be indexed.

#### Example
(Assume the query is ordered by created date descending)

- Client makes request for most recent items: GET /items?limit=20
- On scroll/next page, client finds the minimum created date of 2021-01-20T00:00:00 from previously returned results. and then makes second query using date as a filter: GET /items?limit=20&created:lte:2021-01-20T00:00:00
- On scroll/next page, client finds the minimum created date of 2021-01-19T00:00:00 from previously returned results. and then makes third query using date as a filter: GET /items?limit=20&created:lte:2021-01-19T00:00:00

```
SELECT
    *
FROM
    Items
WHERE
  created <= '2021-01-20T00:00:00'
ORDER BY Id
LIMIT 20
```

### Conclusion
Good API design is a critical component for your Developer Experience (DX). API specifications can outlast many underlying server implementations which requires thinking about future use cases for your API.