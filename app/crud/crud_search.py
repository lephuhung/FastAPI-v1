from elasticsearch import Elasticsearch


# Your API token
api_token = "eTJJbEZwRUJuWUN5MmZocjZFVy06T3lZREl5aE9TM2FKTTlyT25jU091dw=="

client = Elasticsearch("http://elasticsearch:9200/", api_key=api_token)


def doituong_search(query: str = ''):
    resp = client.search(index="doituong_index", query={"multi_match": {"query": f"{query}", "fields": ["*"]}})
    return resp["hits"]["hits"]

def uid_search(query: str = ''):
    resp = client.search(index="uid_index", query={"multi_match": {"query": f"{query}", "fields": ["*"]}})
    return resp["hits"]["hits"]

def trichtin_search(query: str = ''):
    resp = client.search(index="trichtin_index", query={"multi_match": {"query": f"{query}", "fields": ["*"]}})
    return resp["hits"]["hits"]