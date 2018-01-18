import boto3

session = boto3.Session(
	region_name='eu-west-1', 
	profile_name='test'
)

rds = session.client('rds')
response = rds.describe_db_instances(DBInstanceIdentifier='MyRDS_DB_Name')

print(response)
