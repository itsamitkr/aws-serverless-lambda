import decimal
import json
import uuid
import requests
import time
import os
import boto3

dynamodb = boto3.resource('dynamodb',
                          region_name='us-west-2',
                          endpoint_url="https://dynamodb.us-west-2.amazonaws.com")

table = dynamodb.Table(os.environ["STAGE"]+'-currency-table')


def query(event, context):
    response = {
        "statusCode": 500,
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    url = "https://api.exchangeratesapi.io/latest?base=USD"
    try:
        res = requests.get(url)
        payload = currency_exchange_etl(res.json())
        try:

            table.put_item(
                Item=json.loads(payload, parse_float=decimal.Decimal)
            )

            response["statusCode"] = 200
            response["body"] = payload
        except Exception as e:
            print(e)
            response["error"] = str(e)

    except Exception as e:
        response["error"] = e

    return response


def currency_exchange_etl(args):
    response = {
        "exchangeRate": args.get("rates").get("EUR"),
        "exchangeCode": "EUR",
        "baseCode": "USD",
        "updatedOn": time.strftime("%Y-%m-%d"),
        "itemId": str(uuid.uuid4())
    }
    return json.dumps(response)
