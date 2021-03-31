import json
import os


import boto3
dynamodb = boto3.resource('dynamodb')
from botocore.exceptions import ClientError
import encoder
def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch all todos from the database
    result = table.scan()
    try:
        result = table.scan()
    except ClientError as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": os.environ["DOMAIN_NAME"],
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            },
            "body": e.response['Error']['Message']
        }
    # create a response
    response = {
        "statusCode": 200,
        "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": os.environ["DOMAIN_NAME"],
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            },
        "body": json.dumps(result['Items'],
                           cls=encoder.DecimalEncoder)
    }
    return response
