from elasticsearch import Elasticsearch

es = Elasticsearch(
    hosts = [{'host': 'es.id.eu-west-1.es.amazonaws.com', 'port': 443}], 
    use_ssl=True, verify_certs=True
)

es.info()
