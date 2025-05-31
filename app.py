import json

def hello(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello Lambda!!',
            'version': '1.0'
        })
    }
