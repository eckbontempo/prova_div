import pymongo

def obter_colecao_mongodb(url_conexao, colecao):
    cluster = pymongo.MongoClient(url_conexao)
    collect = cluster[colecao]
    return collect

url_conexao = "mongodb+srv://er_bontempo:erick2710@cluster0.aqehs47.mongodb.net/python"
colecao = 'test'

mongodb = obter_colecao_mongodb(url_conexao, colecao)
print(mongodb)