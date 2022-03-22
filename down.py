import boto3
import botocore

BUCKET_NAME = 'testbucket30' # replace with your bucket name
KEY = 'batman.jpg' # replace with your object key

s3 = boto3.resource(service_name='s3',region_name ='us-east-1',aws_access_key_id='',aws_secret_access_key='')
# download a file stored in s3 bucket from ec2 instance.
try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'bat.jpg')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise