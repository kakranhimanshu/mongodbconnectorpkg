from pymongo import MongoClient

# Replace this with your MongoDB Atlas connection string
CONNECTION_STRING = "mongodb+srv://kakranhimanshu2004:hs0Q0XJXcAbFyjKD@cluster0.9cm1jum.mongodb.net/"

# Connect to the MongoDB Atlas cluster
client = MongoClient(CONNECTION_STRING)

dataBase = client["neurolabDB"]

# Collection  Name
collection = dataBase['Products']

# Sample data
d = {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'}

# Insert above records in the collection
rec = collection.insert_one(d)

# Lets Verify all the record at once present in the record with all the fields
all_record = collection.find()

# Printing all records present in the collection
for idx, record in enumerate(all_record):
     print(f"{idx}: {record}")
