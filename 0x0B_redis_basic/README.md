# Redis basic

## Resources
- [Redis commands](link)
- [Redis python client](link)
- [How to Use Redis With Python](link)
- [Redis Crash Course Tutorial](link)

## Learning Objectives
- Learn how to use Redis for basic operations.
- Learn how to use Redis as a simple cache.

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All files should end with a new line.
- A README.md file, at the root of the folder of the project, is mandatory.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- Your code should use the pycodestyle style (version 2.5).
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All functions and methods should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified).
- All functions and coroutines must be type-annotated.
- Install Redis on Ubuntu 18.04:
  ```bash
  $ sudo apt-get -y install redis-server
  $ pip3 install redis
  $ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

```
Use Redis in a container: Redis server is stopped by default - when you are starting a container, you should start it with: service redis-server start
```

## Tasks
0. Writing Strings to Redis
Description
Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g., using uuid), store the input data in Redis using the random key, and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes, int, or float.

```
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

```

1. Reading from Redis and Recovering Original Type
Description
Redis only allows storing strings, bytes, and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store "a" as a UTF-8 string, it will be returned as b"a" when retrieved from the server.

In this exercise, we will create a get method that takes a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.

Remember to conserve the original Redis.get behavior if the key does not exist.

Also, implement 2 new methods: get_str and get_int that will automatically parameterize Cache.get with the correct conversion function.

The following code should not raise:

```
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```

2. Incrementing Values
Description
Familiarize yourself with the INCR command and its Python equivalent.

In this task, we will implement a system to count how many times methods of the Cache class are called.

Above Cache, define a count_calls decorator that takes a single method Callable argument and returns a Callable.

As a key, use the qualified name of method using the __qualname__ dunder method.

Create and return a function that increments the count for that key every time the method is called and returns the value returned by the original method.

Remember that the first argument of the wrapped function will be self, which is the instance itself, which lets you access the Redis instance.

Decorate Cache.store with count_calls.

```
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
```

3. Storing Lists
Description
Familiarize yourself with Redis commands RPUSH, LPUSH, LRANGE, etc.

In this task, we will define a call_history decorator to store the history of inputs and outputs for a particular function.

Every time the original function will be called, we will add its input parameters to one list in Redis and store its output into another list.

In call_history, use the decorated function’s qualified name and append ":inputs" and ":outputs" to create input and output list keys, respectively.

call_history has a single parameter named method that is a Callable and returns a Callable.

In the new function that the decorator will return, use rpush to append the input arguments. Remember that Redis can only store strings, bytes, and numbers. Therefore, we can simply use str(args) to normalize. We can ignore potential kwargs for now.

Execute the wrapped function to retrieve the output. Store the output using rpush in the "...:outputs" list, then return the output.

Decorate Cache.store with call_history.

```
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))
```

4. Retrieving Lists
Description
In this task, we will implement a replay function to display the history of calls of a particular function.

Use keys generated in previous