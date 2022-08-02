from pymongo import MongoClient
ct=MongoClient('localhost',27017)
mydb=ct['testdb']
mycoll=mydb['Employee']
data=mycoll.find()
for r in data:
    print(r)