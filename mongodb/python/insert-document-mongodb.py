from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017/')
mydb = client['mydb']

myrecord = {
        "author": "James",
        "title" : "PyMongo 101",
        "tags" : ["MongoDB", "PyMongo", "Tutorial"],
        "date" : datetime.datetime.utcnow()
        }

record_id = mydb.collection01.insert(myrecord)

print record_id
print mydb.collection_names()
