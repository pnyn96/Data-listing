import boto3
import json

s3 = boto3.client("s3")

def read_json(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    return json.loads(response["Body"].read())

def read_csv(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    return response["Body"].read()
