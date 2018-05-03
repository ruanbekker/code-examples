## AWS SSM Get Paramaters:

```
$ aws ssm get-parameters --names '/team/devops/app01/fqdn-hostname' --with-decryption | jq -r '.Parameters[]' | jq -r '.Value'
app01.domain.com
```
