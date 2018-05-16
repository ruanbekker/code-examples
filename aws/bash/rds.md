
## List all RDS DB Instances and limit output:

```
$ aws --profile prod rds describe-db-instances --query 'DBInstances[*].[DBInstanceArn,DBInstanceIdentifier,DBInstanceClass,Endpoint]'
[
    [
        "arn:aws:rds:eu-west-1:<customer_id>:db:db-name",
        "db-name",
        "db.t2.micro",
        {
            "HostedZoneId": "ABCDEFGHILKL",
            "Port": 5432,
            "Address": "db-name.abcdefg.eu-west-1.rds.amazonaws.com"
        }
    ],
```

## List all RDS DB Instances that has backups enabled, and limit output:

```
$ aws --profile prod rds describe-db-instances --query 'DBInstances[?BackupRetentionPeriod>`0`].[DBInstanceArn,DBInstanceIdentifier,DBInstanceClass,Endpoint]'
[
    [
        "arn:aws:rds:eu-west-1:<customer_id>:db:db-name",
        "db-name",
        "db.t2.micro",
        {
            "HostedZoneId": "ABCDEFGHILKL",
            "Port": 5432,
            "Address": "db-name.abcdefg.eu-west-1.rds.amazonaws.com"
        }
    ],
```
