import decimal
import json
import uuid
import boto3
import requests
import time
import os

dynamodb = boto3.resource('dynamodb',
                          region_name='us-west-2',
                          endpoint_url="https://dynamodb.us-west-2.amazonaws.com")

table = dynamodb.Table(os.environ["STAGE"]+'-crypto-table')


def query(event, context):
    response = {
        "statusCode": 500,
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    url = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"
    try:
        res = requests.get(url)
        payload = crypto_exchange_etl(res.json())

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
        response["error"] = str(e)

    return response


def crypto_exchange_etl(args):
    response = {
        "exchangeRate": args.get("bpi").get("USD").get("rate_float"),
        "cryptoCode": args.get("bpi").get("USD").get("rate_float"),
        "currencyCode": args.get("bpi").get("USD").get("code"),
        "updatedOn": time.strftime("%Y-%m-%d"),
        "itemId": str(uuid.uuid4())
    }
    return json.dumps(response)
