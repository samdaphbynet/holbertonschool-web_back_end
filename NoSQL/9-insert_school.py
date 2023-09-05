#!/usr/bin/env python3
"""
    Function that inserts a new document in a collection based ok 'kwargs'
"""


def insert_school(mongo_collection, **kwargs):
    """
        Insert document in collection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
