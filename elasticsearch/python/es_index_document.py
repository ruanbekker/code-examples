from elasticsearch import Elasticsearch

es = Elasticsearch(
    hosts = [{'host': 'es-domain.es.amazonaws.com', 'port': 443}], 
    use_ssl=True, verify_certs=True
)

document = {"name": "ruan", "surname": "bekker"}

response = es.index(index='my-index', doc_type='_doc', body=document)

# response
# {'_index': 'my-index', '_type': '_doc', '_id': 'Mlq9FHMB6HS5JLZeF5Rs', '_version': 1, 'result': 'created', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 0, '_primary_term': 1}
