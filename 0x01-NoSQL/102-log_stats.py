#!/usr/bin/env python3
"""
provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    # get datatabase
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    number_of_gets = collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{number_of_gets} status check")

    print("IPs:")
    sorted_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}])
    i = 0
    for s in sorted_ips:
        if i == 10:
            break
        print(f"\t{s.get('_id')}: {s.get('count')}")
        i += 1
