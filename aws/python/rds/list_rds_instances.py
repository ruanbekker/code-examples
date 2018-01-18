import boto3

session = boto3.Session(region_name='eu-west-1', profile_name='test')
rds = session.client('rds')

response = rds.describe_db_instances()

for rds_dbs in response['DBInstances']:
	print(rds_dbs['DBInstanceIdentifier'])
