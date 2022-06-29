import json
from unittest import installHandler
import boto3

client = boto3.client('ec2')
instance1 = 'i-0b2c69b9e2789466e'

def check_status(client, instance1):
    res = client.describe_instances(
        InstanceIds = [instance1]
    )
    print(json.dumps(res, indent=2, default=str))


check_status(client, instance1)
