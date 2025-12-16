import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Cart')

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def lambda_handler(event, context):
    userId = event['queryStringParameters']['userId']

    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('userId').eq(userId)
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(response['Items'], default=decimal_default)
    }



Test Event
{
  "queryStringParameters": {
    "userId": "U001"
  }
}
