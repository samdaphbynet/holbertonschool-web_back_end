#!/usr/bin/env python3
""" 0-basic_cache """


BaseCaching = __import__('base_caching').BaseCaching


'''
class BasicCache that inherits from BaseCaching and is a caching system.
'''


class BasicCache(BaseCaching):
    """ BasicCache class """

    def put(self, key, item):
        ''' Add an item '''
        if key is not None or item is not None:
            self.cache_data[key] = item
        else:
            return

    def get(self, key):
        ''' Get an item '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
