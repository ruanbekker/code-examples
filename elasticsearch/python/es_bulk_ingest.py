from elasticsearch import Elasticsearch, helpers

es = Elasticsearch(
    hosts = [{'host': 'es-domain.es.amazonaws.com', 'port': 443}], 
    use_ssl=True, verify_certs=True
)

bulk_docs = []
list_of_dicts = [{"name": "ruan", "age": 32}, {"name": "stefan", "age": 31}]

for doc in list_of_dicts:
    doc['_index'] = 'my-index'
    bulk_docs.append(doc)
    
helpers.bulk(es, bulk_docs)
