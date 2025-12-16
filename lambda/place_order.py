
import boto3
import json
import uuid
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
cart_table = dynamodb.Table('Cart')
order_table = dynamodb.Table('Orders')

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def lambda_handler(event, context):
    body = json.loads(event['body'])
    userId = body['userId']

    cart_items = cart_table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('userId').eq(userId)
    )['Items']

    if not cart_items:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Cart is empty"})
        }

    total = sum(item['price'] * item['quantity'] for item in cart_items)

    orderId = str(uuid.uuid4())

    order_table.put_item(
        Item={
            "orderId": orderId,
            "userId": userId,
            "items": cart_items,
            "totalAmount": total
        }
    )

    for item in cart_items:
        cart_table.delete_item(
            Key={
                "userId": userId,
                "productId": item['productId']
            }
        )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "message": "Order placed successfully",
            "orderId": orderId,
            "total": total
        }, default=decimal_default)
    }





Test Event
{
  "body": "{\"userId\":\"U001\"}"
}
