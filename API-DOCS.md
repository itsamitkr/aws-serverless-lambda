# API Docs

## Currency Exchange Rate APIs
~~~
[GET] https://{hostName}/{stageName}/currency-exchange-rate
~~~
This endpoint will pull in currency exchange data from a public API and store it in the DynamoDB. 
####Request
* Headers
~~~
x-api-key: yourApiKey
~~~
####Response

* Status Code
~~~
200:Success
403: Forbidden
500:Internal Server Error
~~~
* Body
~~~
{
    "exchangeRate": 0.9208103131, 
    "exchangeCode": "EUR", 
    "baseCode": "USD", 
    "updatedOn": "2020-04-17", 
    "itemId": "55bfd47c-f329-4998-8612-43324a1f761f"
}
~~~
---
~~~
[GET] https://{hostName}/{stageName}/currency
~~~
This endpoint will fetch the most recent item from the dynamoDB.
####Request
* Headers
~~~
x-api-key: yourApiKey
~~~
####Response
 * Status Codes
~~~ 
200: Success
204: No Content
400: Bad Request
403: Forbidden
~~~
 * Body
~~~
{ 
    "message|error": "message| error summary"
}
~~~ 
---
~~~
[PUT] https://{hostName}/{stageName}/currency
~~~
This endpoint will allow users to update an item in the dynamoDB.
####Request
* Headers
~~~
x-api-key: yourApiKey
~~~
* Body
~~~
{
    "exchangeRate": 0.9208103131, 
    "exchangeCode": "EUR", 
    "baseCode": "USD", 
    "updatedOn": "2020-04-17", 
    "itemId": "55bfd47c-f329-4998-8612-43324a1f761f"
}
~~~
####Response
 * Status Code
~~~ 
200: Success
201: Created
400: Bad Request
403: Forbidden
~~~
 * Body
~~~
{ 
    "message|error": "message| error summary"
}
~~~ 
***
## Crypto Currency Exchange Rate APIs
~~~
[GET] https://{hostName}/{stageName}/crypto-exchange-rate
~~~
This endpoint will pull in currency exchange data from a public API and store it in the DynamoDB. 
####Request
* Headers
~~~
x-api-key: yourApiKey
~~~
####Response
* Status Code
~~~
200:Success
403: Forbidden
500:Internal Server Error
~~~
* Body
~~~
{
    "exchangeRate": 7051.595,
    "cryptoCode": 7051.595,
    "currencyCode": "USD",
    "updatedOn": "2020-04-16",
    "itemId": "7b91417a-4c7e-4a32-9add-890eb6cdeac9"
}
~~~
---
~~~
[GET] https://{hostName}/{stageName}/crypto
~~~
This endpoint will fetch the most recent item from the dynamoDB.
####Request
* Headers
~~~
x-api-key: yourApiKey
~~~
####Response
 * Status Code
~~~ 
200: Success
204: No Content
400: Bad Request
403: Forbidden
~~~
 * Body
~~~
{ 
    "message|error": "message| error summary"
}
~~~ 
---
~~~
[PUT] https://{hostName}/{stageName}/crypto
~~~
This endpoint will allow users to update an item in the dynamoDB.
####Request
* Headers
~~~
x-api-key: yourApiKey
~~~
* Body
~~~
{
    "exchangeRate": 7051.595,
    "cryptoCode": 7051.595,
    "currencyCode": "USD",
    "updatedOn": "2020-04-16",
    "itemId": "7b91417a-4c7e-4a32-9add-890eb6cdeac9"
}
~~~

####Response
 * Status Code
~~~ 
200: Success
201: Created
400: Bad Request
403: Forbidden
~~~
 * Body
~~~
{ 
    "message|error": "message| error summary"
}
~~~ 