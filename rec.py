# Check AWS resources
# Configure AWS credentials
import boto3

client = boto3.client('resourcegroupstaggingapi')

response = client.get_resources()

for resource in response['ResourceTagMappingList']:
    print(resource['ResourceARN'])