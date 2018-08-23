
## Describe All RDS DB Instances:

```
$ aws --profile prod rds describe-db-instances --query 'DBInstances[*].[DBInstanceArn,DBInstanceIdentifier,DBInstanceClass,Endpoint]'
```

## Describe a RDS DB Instance with a dbname:

```
$ aws --profile prod rds describe-db-instances --query 'DBInstances[?DBInstanceIdentifier==`db-staging`].[DBInstanceArn,DBInstanceIdentifier,DBInstanceClass,Endpoint]'
[
    [
        "arn:aws:rds:eu-west-1:<customer_id>:db:db-staging",
        "db-staging",
        "db.t2.micro",
        {
            "HostedZoneId": "ASKDJSAKDJBA",
            "Port": 5432,
            "Address": "db-staging.asdkjahsd.eu-west-1.rds.amazonaws.com"
        }
    ]
]
```

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

## Describe DB Snapshots for DB Instance Name:

```
$ aws --profile prod rds describe-db-snapshots --db-instance-identifier db --query 'DBSnapshots[?DBInstanceIdentifier==`db`].[DBInstanceIdentifier,DBSnapshotIdentifier,SnapshotCreateTime,Status]'
[
    [
        "db",
        "rds:db-2018-05-16-04-08",
        "2018-05-16T04:08:53.696Z",
        "available"
    ],
```

## Events for the last 24 Hours:

```
$ aws --profile prod rds describe-events --source-identifier "rds:db-2018-05-16-04-08" --source-type db-snapshot --duration 1440 --query 'Events[*]'
[
    {
        "EventCategories": [
            "creation"
        ],
        "SourceType": "db-snapshot",
        "SourceArn": "arn:aws:rds:eu-west-1:<customer_id>:snapshot:rds:db-2018-05-16-04-08",
        "Date": "2018-05-16T04:08:40.264Z",
        "Message": "Creating automated snapshot",
        "SourceIdentifier": "rds:db-2018-05-16-04-08"
    },
    {
        "EventCategories": [
            "creation"
        ],
        "SourceType": "db-snapshot",
        "SourceArn": "arn:aws:rds:eu-west-1:<customer_id>:snapshot:rds:db-2018-05-16-04-08",
        "Date": "2018-05-16T04:32:04.047Z",
        "Message": "Automated snapshot created",
        "SourceIdentifier": "rds:db-2018-05-16-04-08"
    }
]
```
## List Public RDS Instances:

```
$ aws --profile prod rds describe-db-instances --query 'DBInstances[?PubliclyAccessible==`true`].[DBInstanceIdentifier,Endpoint.Address]'

[
  [
    "name",
    "name.abcdef.eu-west-1.rds.amazonaws.com"
  ]
]
```
