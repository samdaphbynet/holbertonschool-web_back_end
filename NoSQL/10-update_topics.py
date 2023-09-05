#!/usr/bin/env python3
"""
  function that changes all topics of a school document based on the name:
   - Prototype: def update_topics(mongo_collection, name, topics):
   - mongo_collection will be the pymongo collection object
   - name (string) will be the school name to update
   - topics (list of strings) will be the list of topics approached.
"""


def update_topics(mongo_collection, name, topics):
    """
        update_topics: changes all topics of a school document.
    """
    up_name = {"name": name}
    up_topics = { "$set": {"topics": topics } }
    mongo_collection.update_many(up_name, up_topics)
