from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["company_db"]
collection = db["c1"]

collection.insert_one({"name": "Rohit", "dep": "30000", "course": "Python", "salary": "25000"})

result = collection.find_one({"name": "Rohit"})

print(result)

