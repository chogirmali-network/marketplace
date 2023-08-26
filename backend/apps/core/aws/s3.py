import boto3
import pandas as pd
# from configurations import AWS_DEFAULT_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from environs import Env

env = Env()
env.read_env()

AWS_DEFAULT_REGION = env('AWS_DEFAULT_REGION')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')


s3 = boto3.resource(
    service_name = 's3',
    region_name = AWS_DEFAULT_REGION,
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)
