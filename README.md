# Python Mockservice Serverless

## Summary of what the non-serverless application does and looks like. 

    The app exposes 3 APIs to interact with a DynamoDB table.  

### Create 

You make a request to the API endpoint and a single item looks like the following:

```
    {
        'id': str(pathId),
        'params': json.dumps(queryParam),
        'out': data,
        'createdAt': timestamp,
    }
```

- pathId: Obtained from the path following the API endpoint.

    `eg: https://xxxxxx.execute-api.us-east-1.amazonaws.com/dev/endpointpath`

    The ID here would be: __endpointpath__

- params: All the queryString parameters that were passed along the request

- out: Any body (eg. JSON) that might have been sent in the request

- createdAt: Just the timestamp of when the item was added

### GET

To get an item, make a request to the endpoint with 'id' and 'params' specified as querystring params.

### LIST

Now if you want to get a list of all the items that have been created, you make a call to the API endpoint in the following manner:

` https://xxxxxx.execute-api.us-east-1.amazonaws.com/dev/all `
