#!/usr/bin/env python3
"""
    Writing strings to Redis
"""


import redis
import uuid
from typing import Union


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

    def store(self, data: Union[int, bytes, str, float]) -> str:
        """
        function that return the string writing
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: callable = None)\
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
