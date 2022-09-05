import pymongo

client = pymongo.MongoClient("mongodb+srv://sas1:dreamdream@sas.besrf7r.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"sas",
    "email" : "sas@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
