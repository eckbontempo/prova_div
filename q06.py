import pymongo

url = "mongodb+srv://er_bontempo:erick2710@cluster0.aqehs47.mongodb.net/?retryWrites=true&w=majority"

cluster = pymongo.MongoClient(url)

db = cluster.get_database('python')

collection = db.get_collection('test')

def ajustar_estoque(sku, estoque):
    collection.update_one({"sku":sku}, {"$set": {"estoque":estoque}})

sku = int(input('Digite o sku do produto: '))
estoque = int(input('Digite a nova quantidade no estoque: '))

ajustar_estoque(sku, estoque)
