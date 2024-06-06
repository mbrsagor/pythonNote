import boto3
import botocore


# def lambda_handler(event, context):
#    print(f'boto3 version: {boto3.__version__}')
#    print(f'botocore version: {botocore.__version__}')


import json

def lambda_handler(event, context):
    print("Hello from Lambda!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

