# MySQL Project

## Resources

Before starting the project, it's recommended to go through the following resources:

- [MySQL cheatsheet](https://intranet.hbtn.io/rltoken/XCHG-pgtifYRSw8ILB6DEw)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://intranet.hbtn.io/rltoken/VXAPISdkpKg3YD3HmVQXlw)
- [Stored Procedure](https://intranet.hbtn.io/rltoken/C37E-NvP8KxpI5Ds5w1oAQ)
- [Triggers](https://intranet.hbtn.io/rltoken/0xFZu5AK0imLk70dxxcODA)
- [Views](https://intranet.hbtn.io/rltoken/Q8butAms3BthfCFhXuQSPA)
- [Functions and Operators](https://intranet.hbtn.io/rltoken/0ezATipRSpz1K8MixrD2Rg)
- [Trigger Syntax and Examples](https://intranet.hbtn.io/rltoken/rc8oho9n7LAjtffC584tgA)
- [CREATE TABLE Statement](https://intranet.hbtn.io/rltoken/F1SUJgWz-4YNNYLPkL9tPw)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://intranet.hbtn.io/rltoken/XhYdXik2tTMK2k81WxulpA)
- [CREATE INDEX Statement](https://intranet.hbtn.io/rltoken/K90KZ3z4gL5mPpHROlEOcg)
- [CREATE VIEW Statement](https://intranet.hbtn.io/rltoken/VJESVxV2V7jGqrR-50903A)

## Learning Objectives

Upon completing this project, you should be able to:

- Explain how to create tables with constraints
- Optimize queries by adding indexes
- Implement stored procedures and functions in MySQL
- Implement views in MySQL
- Implement triggers in MySQL

## Requirements

- All files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- All files should end with a new line
- All SQL queries should have a comment just before (i.e., syntax above)
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE...)
- A README.md file at the root of the project folder is mandatory
- The length of your files will be tested using wc

## Usage

Follow these steps to set up and run the project:

1. Use "container-on-demand" to run MySQL.
2. Ask for a container with Ubuntu 18.04 and Python 3.7.
3. Connect via SSH or WebTerminal.
4. Start MySQL in the container using `$ service mysql start`.
5. Import a SQL dump using the provided commands.
6. Execute the required SQL scripts.

## Tasks

### Task 0: We are all unique! (mandatory)

Write a SQL script that creates a table `users` with the following requirements:

- Attributes:
  - `id`: integer, never null, auto increment, primary key
  - `email`: string (255 characters), never null, unique
  - `name`: string (255 characters)
- Ensure the script doesn't fail if the table already exists.

Example usage:

```
$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password:
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
$ cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password:
$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password:
$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password:
$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password:
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password:
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
```

# Task 1: Creating Users Table with Country Attribute

Write a SQL script that creates a table `users` with the following requirements:

- Attributes:
  - `id`: integer, never null, auto increment, primary key
  - `email`: string (255 characters), never null, unique
  - `name`: string (255 characters)
  - `country`: enumeration of countries: US, CO, and TN, never null (default will be US)

Ensure the script doesn't fail if the table already exists.

Example usage:

```
$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password:
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
$ cat 1-country_users.sql | mysql -uroot -p holberton
Enter password:
$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password:
$ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password:
$ echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password:
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password:
$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password:
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
```
