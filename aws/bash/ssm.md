# AWS SSM

## Get Parameters By Path:

```
$ aws ssm get-parameters-by-path --path '/global/devops/app01/' | jq '.Parameters[]' | jq -r '.Name'
/team/devops/app01/fqdn-hostname
/team/devops/app01/app-username
```

## Get Paramaters:

```
$ aws ssm get-parameters --names '/team/devops/app01/fqdn-hostname' --with-decryption | jq -r '.Parameters[]' | jq -r '.Value'
app01.domain.com
```

## Describe Parameters:

```
$ aws prod ssm describe-parameters --filters "Key=Name,Values='/team/devops/app01/fqdn-hostname'"
{
    "Parameters": [
        {
            "KeyId": "alias/devops-app01-prod-ssm",
            "Name": "/team/devops/app01/fqdn-hostname",
            "LastModifiedDate": 1520853940.496,
            "Version": 1,
            "LastModifiedUser": "arn:aws:iam::0123456789012:user/ruanb",
            "Type": "SecureString"
        }
    ]
}
```
