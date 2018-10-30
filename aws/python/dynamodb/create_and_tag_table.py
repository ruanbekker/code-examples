# Creates a DynamoDB Table: test_20181030 and Tags it

import boto3
import time

session = boto3.Session(region_name='eu-west-1', profile_name='test')
resource = session.resource('dynamodb')
client = session.client('dynamodb')

def create_table():
    table_name = "test_{0}".format(time.strftime("%Y%m%d"))
    response = resource.create_table(
        TableName=table_name,
        KeySchema=[{
            'AttributeName': 'uuid',
            'KeyType': 'HASH'
        }],
        AttributeDefinitions=[{
            'AttributeName': 'uuid',
            'AttributeType': 'S'
        }],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    resource.Table(table_name).wait_until_exists()

    arn = client.describe_table(TableName=table_name)['Table']['TableArn']
    client.tag_resource(
        ResourceArn=arn,
        Tags=[
            {'Key': 'Name','Value': 'yes'},
            {'Key': 'Environment','Value': 'yes'},
            {'Key': 'Owner','Value': 'yes'}
        ]
    )

    return resource.Table(table_name).table_status
