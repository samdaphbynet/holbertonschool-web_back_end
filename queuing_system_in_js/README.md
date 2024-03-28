# Queuing System in JS - Amateur

## Description
This project aims to implement a queuing system in JavaScript, focusing on utilizing Redis as the backend datastore. By following the provided resources and learning objectives, you will gain insights into setting up a Redis server, interacting with it using a Redis client in Node.js, and integrating a queuing system using Kue. Additionally, you will learn to build basic Express applications that interact with Redis servers and queues.

## Resources
Read or watch:
- [Redis quick start](https://redis.io/topics/quickstart)
- [Redis client interface](https://redis.io/clients)
- [Redis client for Node.js](https://www.npmjs.com/package/redis)
- [Kue deprecated but still used in the industry](https://github.com/Automattic/kue)

## Learning Objectives

- Running a Redis server on your machine
- Executing simple operations with the Redis client
- Utilizing a Redis client with Node.js for basic operations
- Storing hash values in Redis
- Handling asynchronous operations with Redis
- Implementing Kue as a queue system
- Developing a basic Express app interacting with a Redis server
- Building a basic Express app interacting with a Redis server and queue

## Requirements
- All code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Code should use the `.js` extension for JavaScript files

### Required Files for the Project
- `package.json`
- `.babelrc`
- Other necessary files (specified in tasks)

### Instructions
Don’t forget to run `$ npm install` when you have the `package.json`.

## Tasks
### 0. Install a Redis instance (mandatory)
Download, extract, and compile the latest stable Redis version (higher than 5.0.7) from [Redis Download](https://redis.io/download/):

```
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
```

Start Redis in the background with src/redis-server:
```
$ src/redis-server &
```
Ensure that the server is working with a ping using src/redis-cli ping:
```
PONG
```
Using the Redis client, set the value "School" for the key "Holberton":
```
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
```
Kill the server with the process ID of the redis-server (hint: use ps and grep):
```
kill [PID_OF_Redis_Server]
```

Copy the dump.rdb from the redis-5.0.7 directory into the root of the Queuing project.

Requirements:

Running get Holberton in the client should return "School".