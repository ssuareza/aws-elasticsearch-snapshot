import boto3
import requests
from requests_aws4auth import AWS4Auth

# Your values here
host = 'https://my-es-cluster/'
region = 'us-east-1'
bucket = 'my-repository-name' 
role = 'arn:aws:iam::111111111111:role/es-snapshot-results'
snapshot = 'my-snapshot-name'

service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# Register repository
path = '_snapshot/' + snapshot
url = host + path

payload = {
  "type": "s3",
  "settings": {
    "bucket": bucket,
    "region": region,
    "role_arn": role
  }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r.status_code)
print(r.text)