import pymongo
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection['test_database']
collection = db['test']
dic = {
    "name": "reza",
    "age": 20,
    "city": "tehran"
}
# x = db.test.insert_one(dic)
# print(x.name)
now_dic = {"$set":{'age':22}}
collection.update_one(dic,now_dic)
# collection.update_one({"name": "reza"}, {"$set": {"age": 22}})
print(collection.find_one({"name": "reza"}))

# collection.delete_one({"name": "reza"})
# print(collection.find_one({"name": "reza"}))





