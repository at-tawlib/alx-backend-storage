#!/usr/bin/env python3
"""
Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """returns a list of school having a specific topic"""
    return mongo_collection.find({"topics": topic})
