import os
import json

import encoder
import boto3
dynamodb = boto3.resource('dynamodb')
from botocore.exceptions import ClientError

def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    pathId = event['path']
    queryParam = event['queryStringParameters']
    # TODO validation required
    # fetch resource from the database
    try:
        result = table.get_item(
            Key={
                'id': pathId,
                'params': json.dumps(queryParam)
            }
        )
        if 'Item' not in result:
             return {
                "statusCode": 404,
                "body": ""
            }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": e.response['Error']['Message']
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": e.response['Error']['Message']
        }

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item']['out'],
                           cls=encoder.DecimalEncoder)
    }

    return response