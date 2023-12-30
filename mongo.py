import pymongo as pym
from pymongo.errors import OperationFailure
import json
import pprint   

with open('champs_data.json', 'r') as file:
    data = json.load(file)


client = pym.MongoClient("mongodb+srv://thalesmartins:Cogumelos7#@cluster0.csvojnb.mongodb.net/")

db = client.LOL

colecao = db.Champions

post = colecao.insert_many(data)

for post in colecao.find():
    pprint.pprint(post)
