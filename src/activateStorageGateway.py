import os
import boto3
import json
import time
import urllib.request
import http.client
import urllib.parse as urlparse
from urllib.parse import parse_qs
from urllib.parse import urlsplit


ec2 = boto3.client('ec2')
stg = boto3.client('storagegateway')

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

   while True:
       try:
           # TODO: write code...
           conn = http.client.HTTPConnection(instance_ip)
           conn.request("GET","/?activationRegion=us-east-1")
       
           response = conn.getresponse()
           print(instance_ip)

           parsed = urlparse.urlparse(response.msg["Location"])
           print(parsed)
       
           result = parse_qs(parsed.query)["activationKey"]
           print(result)
       
           print(response.msg["Location"])
       
           return result[0]
           
       except Exception:
           print("Passou aqui!")
         
           return False
    
       

            
            

def create_instance(self):
    con = ec2.run_instances(
        InstanceType="m5.xlarge",
        BlockDeviceMappings=[
            {
                'DeviceName': 'xvdb',
                'Ebs': {
                    'DeleteOnTermination': True,
                    'VolumeSize': 1024,
                    'VolumeType': 'gp3',
                }
            }
        ],
        MaxCount=1,
        MinCount=1,
        ImageId="ami-03ae10098c64188a7",
        SecurityGroupIds=[
            "sg-0bf30e4fe9a689471"
        ],
        SubnetId="subnet-09778846a4a409dc6",
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