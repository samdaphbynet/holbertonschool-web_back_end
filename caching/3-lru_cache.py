#!/usr/bin/env python3
""" 3-lru_cache """


from collections import OrderedDict


BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """
    def __init__(self):
        """ Initialize LRUCache """
        super().__init__()
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        # Remove the least recently used item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = next(iter(self.usage_order))
            del self.cache_data[lru_key]
            del self.usage_order[lru_key]
            print("DISCARD: {}".format(lru_key))

        self.cache_data[key] = item
        self.usage_order.pop(key, None)
        self.usage_order[key] = None

    def get(self, key):
        """ get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.pop(key, None)
        self.usage_order[key] = None
        return self.cache_data[key]
