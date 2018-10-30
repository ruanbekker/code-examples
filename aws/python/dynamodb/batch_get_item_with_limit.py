# Duplicated HashKey to the metadata table and duplicated timestamp attribute
# Scan and Filter metadata table, get HK's
# Execute BatchGet on the Base Table

import boto3
import time
from boto3.dynamodb.conditions import Key

base_table = 'test_base'
meta_table = 'test_20181029'

session = boto3.Session(region_name='eu-west-1', profile_name='test')
resource = session.resource('dynamodb')
table = resource.Table(meta_table)
filtering_expression = Key('timestamp').gt(1540841144)

response = table.scan(FilterExpression=filtering_expression, Limit=100)

all_items = []
finished=False
while finished != True:
    if 'LastEvaluatedKey' in response.keys():
        print("Getting {} Items".format(response['Count']))
        items = resource.batch_get_item(RequestItems={base_table: {'Keys': response['Items']}})
        #print(items['Responses'][base_table])
        all_items += items['Responses'][base_table]
        time.sleep(2)
        response = table.scan(FilterExpression=filtering_expression, Limit=100, ExclusiveStartKey=response['LastEvaluatedKey'])
    else:
        print("Getting {} Items".format(response['Count']))
        items = resource.batch_get_item(RequestItems={base_table: {'Keys': response['Items']}})
        #print(items['Responses'][base_table])
        all_items += items['Responses'][base_table]
        finished=True

print(len(all_items))
# Output:
# Getting 100 Items
# Getting 100 Items
# Getting 54 Items
# 254
