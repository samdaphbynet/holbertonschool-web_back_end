#!/usr/bin/env python3
"""
    Writing strings to Redis
"""


import redis
import uuid
from typing import Optional, Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    function that count the number of calls
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function that count the number of calls
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to store the history of inputs and
    outputs for a particular function.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper for decorator functionality """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper


def replay(fn: Callable):
    """Display the history of calls of a particular function"""
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{f_name} was called {n_calls} times:')

    ins = r.lrange(f_name + ":inputs", 0, -1)
    outs = r.lrange(f_name + ":outputs", 0, -1)

    for i, o in zip(ins, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ""
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ""

        print(f'{f_name}(*{i}) -> {o}')


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

    @call_history
    @count_calls
    def store(self, data: Union[int, bytes, str, float]) -> str:
        """
        function that return the string writing
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
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
