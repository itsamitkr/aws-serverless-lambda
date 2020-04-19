import boto3
import json
import decimal
import os

dynamodb = boto3.resource('dynamodb',
                          region_name='us-west-2',
                          endpoint_url="https://dynamodb.us-west-2.amazonaws.com")


def update_exchange_rate(table_name, data):
    response = {
        "statusCode": 500,
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    try:
        table = dynamodb.Table(table_name)
        put_data = json.loads(data, parse_float=decimal.Decimal)
        table.put_item(Item=put_data)
        response["statusCode"] = 201
        response["body"] = "Created"
    except Exception as e:
        response["body"] = str(e)
    return response


def crypto(event, context):
    data = json.loads(event.get("body"))
    return update_exchange_rate(os.environ["STAGE"]+'-crypto-table', data)


def currency(event, context):
    data = json.loads(event.get("body"))
    return update_exchange_rate(os.environ["STAGE"]+'-currency-table', data)
