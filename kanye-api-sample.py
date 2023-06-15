import json
import requests# has a problem in runtime even tho i uploaded layers error in python 3.10
#from botocore.vendored import requests
import boto3

bucket = "bucket-name"
file_name = "kanye_test.json"


def kanye_api():
    url = "https://api.kanye.rest"
    r = requests.get(url)
    return r.json()

#json file creation
kanye = kanye_api()

#saving to s3
s3 = boto3.resource('s3')
s3object = s3.Object(bucket, file_name)
s3object.put(
    Body=(bytes(json.dumps(kanye).encode('UTF-8')))
)
    

# This is important, to handle the "lambda function" in this UI section
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


