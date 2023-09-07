#!/usr/bin/env python3
"""
    function named index_range that takes two integer arguments.
"""
import csv
from math import ceil
from typing import List


def index_range(page, page_size):
    """
        function should return a tuple of size two containing a start index
        and an end index corresponding to the range of indexes to return in
        a list for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            return the appropriate page of the dataset
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        index = index_range(page, page_size)
        start = index[0]
        end = index[1]

        try:
            return self.dataset()[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
            get_hyper method that takes the same arguments as get_page and
            returns a dictionary containing the following key-value pairs:
            'page_size': the length of the returned dataset page
            'page': the current page number
            'data': the dataset page (equivalent to return from previous task)
            'next_page': number of the next page, None if no next page
            'prev_page': number of the previous page, None if no previous page
            'total_pages': the total number of pages in the dataset
        """
        page_data = self.get_page(page, page_size)
        all_data = len(self.dataset())
        all_pages = ceil(all_data / page_size)

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page < all_pages else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': all_pages
        }
