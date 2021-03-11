import os
import boto3
import json
import time
import urllib.request
import http.client
import urllib.parse as urlparse
from urllib.parse import parse_qs
from urllib.parse import urlsplit

stg = boto3.client('storagegateway')

def list_file_shares(arn_gateway):
    
    response = stg.list_file_shares(
        GatewayARN=arn_gateway,
    )
    
    shares = len(response["FileShareInfoList"])
    print(shares)
    
    return shares

def list_gateways():
    response = client.list_gateways(
    )
    
    gateway = responses['Gateways'][-1]['GatewayName']
    
    print(gateway)
    return gateway