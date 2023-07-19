#!/usr/bin/env python3
"""
provides some stats about Nginx logs stored in MongoDB
"""
import pymongo
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    # get datatabase
    collection = client.logs.nginx

    print(f"{collection.estimated_document_count()} logs")

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
    for ip in sorted_ips:
        if i == 10:
            break
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
        i += 1
