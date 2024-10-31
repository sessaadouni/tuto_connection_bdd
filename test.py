from config.connectionMongo import connect_mongodb
from config.connectionRedis import connect_redis

# connexion à redis et mongo
client_redis = connect_redis()
client_mongo = connect_mongodb()

print()

# test de redis
client_redis.set("test", "test")
print(client_redis.get("test"))

# test de mongo
db = client_mongo.TestDB
collection = db.TestCollection
collection.insert_one({"test": "test"})
print(collection.find_one())
