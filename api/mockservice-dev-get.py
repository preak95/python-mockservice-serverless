import os
import json

import encoder
import boto3
dynamodb = boto3.resource("dynamodb")
from botocore.exceptions import ClientError

def get(event, context):
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    pathId = event["path"]
    queryParam = event["queryStringParameters"]
    # TODO validation required
    # fetch resource from the database
    try:
        result = table.get_item(
            Key={
                "id": pathId,
                "params": json.dumps(queryParam)
            }
        )
        if "Item" not in result:
             return {
                "statusCode": 404,
                "headers": {
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Origin": os.environ["DOMAIN_NAME"],
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                "body": ""
            }
    except ClientError as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": os.environ["DOMAIN_NAME"],
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            },
            "body": e.response["Error"]["Message"]
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": os.environ["DOMAIN_NAME"],
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            },
            "body": e.response["Error"]["Message"]
        }

    # create a response
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": os.environ["DOMAIN_NAME"],
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        "body": json.dumps(result["Item"]["out"],
                           cls=encoder.DecimalEncoder)
    }

    return response