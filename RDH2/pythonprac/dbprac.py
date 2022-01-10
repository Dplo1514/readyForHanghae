from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.axhff.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name' : 'hyuk',
    'age' : 25
}

db.users.insert_one(doc)