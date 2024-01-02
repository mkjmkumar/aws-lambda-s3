import boto3
from boto3.session import Session
from datetime import datetime


session = Session(aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

s3 = session.resource(
    service_name='s3', 
    endpoint_url='http://host.docker.internal:4566'
)

def lambda_handler(event, context):

    bucket = 'test-bucket'    # TEST MUKESH
    key = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
    file_contents = 'Lambda Save File'

    s3.Bucket(bucket).put_object(Key=key, Body=file_contents)

    return 'create file'+ key

