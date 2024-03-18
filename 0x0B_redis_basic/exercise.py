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
