import os
import json
import boto3
import urllib.request
import http.client
import urllib.parse as urlparse
from urllib.parse import parse_qs
from urllib.parse import urlsplit


ec2 = boto3.client('ec2')
stg = boto3.client('storagegateway')

def lambda_handler(event, context):
    
    instance_ip = create_instance(event)
    
    key = get_gateway_activation_key(instance_ip)
    
    result = activate_gateway(key)
    
    return key

def activate_gateway(key):
    
    response = stg.activate_gateway(
        ActivationKey=key,
        GatewayName="StorageGateway",
        GatewayTimezone="GMT+3:00",
        GatewayRegion="us-east-1",
        GatewayType="FILE_S3",
        Tags=[
            {
                'Key': 'Name',
                'Value': 'StorageGateway'
            }
        ]
    )
    
    return response

def get_gateway_activation_key(instance_ip):

   conn = http.client.HTTPConnection(instance_ip)
   conn.request("GET","/?activationRegion=us-east-1")
   response = conn.getresponse()
   parsed = urlparse.urlparse(response.msg["Location"])
   result = parse_qs(parsed.query)["activationKey"]
   print(response.msg["Location"])
  
   return result[0]

def create_instance(self):
    con = ec2.run_instances(
        InstanceType="t2.micro",
        MaxCount=1,
        MinCount=1,
        ImageId="ami-03ae10098c64188a7",
        SecurityGroupIds=[
            "sg-123456"
        ],
        SubnetId="subnet-123456",
        TagSpecifications=[
            {
                'ResourceType':'instance',
                'Tags': [
                    {
                        'Key':'Name',
                        'Value':'StorageGateway'
                    }
                ]
            }
        ]
    )
    instance = con['Instances'][0]['PrivateIpAddress']

    return instance