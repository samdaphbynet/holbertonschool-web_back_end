#!/usr/bin/env python3
"""
    Writing strings to Redis
"""


import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(func: Callable) -> Callable:
    """
    function that count the number of calls
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function that count the number of calls
        """
        key = func.__qualname__
        self._redis.incr(key)
        return func(self, *args, **kwargs)
    return wrapper


class Cache():
    """
    class that store an instance of the Redis client
    """
    def __init__(self):
        """
         private variable named _redis using redis.Redis() and flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[int, bytes, str, float]) -> str:
        """
        function that return the string writing
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable = None)\
            -> Union[str, int, bytes, float]:
        """
        function that return the string reading
        """
        data = self._redis.get(key)

        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Union[str, bytes]:
        """
        function that return the string reading from the specified key
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[str, bytes]:
        """
        function that automatically parametrize
        """
        return self.get(key, fn=lambda d: int(d))
