from pymongo import MongoClient

# Replace this with your MongoDB Atlas connection string
CONNECTION_STRING = "your_connection_string"

# Connect to the MongoDB Atlas cluster
client = MongoClient(CONNECTION_STRING)

# Access your database
db = client['your_database_name']

# Access your collection
collection = db['your_collection_name']

# Example: Insert a document into the collection
document = {"key": "value"}
collection.insert_one(document)

# Example: Query documents from the collection
results = collection.find({"key": "value"})
for result in results:
    print(result)

# Example: Update documents in the collection
collection.update_one({"key": "value"}, {"$set": {"key": "new_value"}})

# Example: Delete documents from the collection
collection.delete_one({"key": "new_value"})
