import boto3

session = boto3.Session(
	region_name='eu-west-1', 
	profile_name='test'
)

missing_tag_value = 'N/A'
rds = session.client('rds')
response = rds.describe_db_instances()
rds_resource_arns = []

for rds_db_id in response['DBInstances']:
	rds_resource_arns.append(rds_db_id['DBInstanceArn'])

def get_resource_id(arn_string):
	resource_name = arn_string.split(":")[6]
	resource_id = rds.describe_db_instances(DBInstanceIdentifier=resource_name)['DBInstances'][0]['DbiResourceId']

	return resource_id 

def list_rds_tags(arn_string):
	tag_name = missing_tag_value
	tag_owner = missing_tag_value
	tag_classification = missing_tag_value
	tag_list = rds.list_tags_for_resource(ResourceName=arn_string)
	for tags in tag_list['TagList']:
		if tags['Key'] == 'Name':
			tag_name = tags['Value']
		if tags['Key'] == 'Owner':
			tag_owner = tags['Value']

	return tag_name, tag_owner

for arn in rds_resource_arns:
	db_id = get_resource_id(arn)
	tag_name, tag_owner = list_rds_tags(arn)
	print(
		"{0}, {1}, {2}, {3}".format(
			"RDS", db_id, tag_name, tag_owner
		)
	)
