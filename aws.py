import json
from unittest import installHandler
import boto3

client = boto3.client('ec2')
res = client.describe_instances(
    InstanceIds = ['i-0b2c69b9e2789466e']
)
print(json.dumps(res, indent=2, default=str))