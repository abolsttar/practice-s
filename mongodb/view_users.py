import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['registration_db']
collection = db['users']


print("کاربران ثبت شده:")
for user in collection.find():
    print(f"نام: {user['name']}")
    print(f"فامیلی: {user['family']}")
    print(f"سن: {user['age']}")
    print("-" * 30) 