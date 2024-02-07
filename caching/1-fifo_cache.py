#!/usr/bin/env python3
"""1-fifo_cache"""


BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache Class"""
    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the first item in the cache
            first_key = next(iter(self.cache_data))
            print("DISCARD: {}".format(first_key))
            del self.cache_data[first_key]

        self.cache_data[key] = item

    def get(self, key):
        """Get the cache data"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
