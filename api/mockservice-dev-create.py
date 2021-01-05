import json
import logging
import os
import time

import boto3
dynamodb = boto3.resource('dynamodb')
from botocore.exceptions import ClientError

def create(event, context):
    data = json.loads(event['body']) 
    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    pathId = event['path']
    queryParam = event['queryStringParameters']

    item = {
        'id': str(pathId),
        'params': json.dumps(queryParam),
        'out': data,
        'createdAt': timestamp,
    }

    # write the resource to the database
    try:
        table.put_item(Item=item)
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": "Error: "+e.response['Error']['Message']
        }
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
