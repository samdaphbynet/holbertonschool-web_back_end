#!/usr/bin/env python3
""" 4-mru_cache """


from collections import OrderedDict


BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class """

    def __init__(self):
        """ initialize """
        super().__init__()
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """ put item in cache """
        if key is None or item is None:
            return

        # Remove item from cache
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key, _ = self.usage_order.popitem()
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))

        # Add the new item to the cache
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
