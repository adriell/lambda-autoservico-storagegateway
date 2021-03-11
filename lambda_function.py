import boto3
import json
import sys
import urllib3
from src.activateStorageGateway import get_gateway_activation_key
from src.activateStorageGateway import create_instance
from src.activateStorageGateway import activate_gateway

def lambda_handler(event, context):
    print("SNS Event: " + json.dumps(event))
    
    event = json.loads(event['Records'][0]['Sns']['Message'])
    
    print("Lambda Event: " + json.dumps(event))

    try:
        type = event['RequestType']
        bucket = event['ResourceProperties']['BucketName']
        accountId = event['ResourceProperties']['AccountID']
        envName = event['ResourceProperties']['EnvName']
        ipSource = event['ResourceProperties']['IP']
    
        instance_ip = create_instance(event)
    
        key = get_gateway_activation_key(instance_ip)
    
        result = activate_gateway(key)

        responseStatus = 'SUCCESS'
        responseData = {'BucketName': bucket, 'AccountID':accountId}
        sendResponse(event, context, responseStatus, responseData)  
        
        

        return responseStatus
    except:
        print("Error:", sys.exc_info()[0])
        responseStatus = 'FAILED'
        responseData = {}
        sendResponse(event, context, responseStatus, responseData)

        
def sendResponse(event, context, responseStatus, responseData):
    data = json.dumps({
      'Status': responseStatus,
      'Reason': 'See the details in CloudWatch Log Stream: ' + context.log_stream_name,
      'PhysicalResourceId': context.log_stream_name,
      'StackId': event['StackId'],
      'RequestId': event['RequestId'],
      'LogicalResourceId': event['LogicalResourceId'],
      'Data': responseData
    })
    
    http = urllib3.PoolManager()
    encoded_data = json.dumps(data).encode('utf-8')
    req_headers = {'Content-Type':''}
    r = http.request('PUT',event['ResponseURL'], headers=req_headers, body=data)

    #opener = urllib3.build_opener(urllib3.HTTPHandler)
    #request = urllib3.Request(url=event['ResponseURL'], data=data)
    #request.add_header('Content-Type', '')
    #request.get_method = lambda: 'PUT'
    #url = opener.open(request)

