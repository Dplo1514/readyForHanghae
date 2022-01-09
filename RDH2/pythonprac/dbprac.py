from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ps8a8.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


doc = {
    'name' : 'hyuk',
    'age' : 25
}

db.users.insert_one(doc)