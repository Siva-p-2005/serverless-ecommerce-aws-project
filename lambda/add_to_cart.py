import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Cart')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    userId = body['userId']
    productId = body['productId']
    quantity = body['quantity']
    price = body['price']

    table.put_item(
        Item={
            "userId": userId,
            "productId": productId,
            "quantity": quantity,
            "price": price
        }
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"message": "Product added to cart"})
    }




Test Event
{
  "body": "{\"userId\":\"U001\",\"productId\":\"P001\",\"quantity\":2,\"price\":500}"
}
