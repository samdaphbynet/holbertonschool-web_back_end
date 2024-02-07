#!/usr/bin/env python3
""" 2-lifo_cache """

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class """
    def __init__(self):
        """ Initialize the cache """
        super().__init__()

    def put(self, key, item):
        """ Put an item in the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """ Cache the item with the specified key """
            last = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(last))
            del self.cache_data[last]

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
