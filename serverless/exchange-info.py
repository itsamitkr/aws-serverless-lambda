import os
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb',
                          region_name='us-west-2',
                          endpoint_url="https://dynamodb.us-west-2.amazonaws.com")


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


def get_items(table_name):
    table = dynamodb.Table(table_name)
    items = []
    response = table.scan()

    for i in response['Items']:
        items.append(json.dumps(i, cls=DecimalEncoder))

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])

        for i in response['Items']:
            items.append(json.dumps(i, cls=DecimalEncoder))
    return items


def get_exchange_rate(table_name):
    response = {
        "statusCode": 500,
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    try:
        items = get_items(table_name)

        if items:
            response["statusCode"] = 200
            response["body"] = json.dumps(items[0], cls=DecimalEncoder)
        else:
            response["statusCode"] = 204
    except Exception as e:
        print(e)
        response["error"] = e

    return response


def crypto(event, context):
    return get_exchange_rate(os.environ["STAGE"]+'-crypto-table')


def currency(event, context):
    return get_exchange_rate(os.environ["STAGE"]+'-currency-table')
