# import json

# def lambda_handler(event, context):
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }

import boto3
import json
import uuid

def allocate_resources(resource_type, quantity, user_info):
    # Provision EC2 instances using the AWS SDK (boto3)
    ec2_client = boto3.client('ec2')
    response = ec2_client.run_instances(
        ImageId='ami-02dfa54cfb2a5d6c2',
        InstanceType='t2.micro',
        MinCount=quantity,
        MaxCount=quantity
    )

    # Generate a unique resource allocation ID
    allocation_id = str(uuid.uuid4())

    # Return the allocation ID
    return allocation_id


def lambda_handler(event, context):
    # Print the request body for debugging
    print(event['body'])

    try:
        # Parse the JSON request
        request_body = json.loads(event['body'])
        resource_type = request_body['resource_type']
        quantity = request_body['quantity']
        user_info = request_body['user_info']

        # Allocate the resources
        allocation_id = allocate_resources(resource_type, quantity, user_info)

        # Prepare the response
        response_body = {
            'status': 'success',
            'allocation_id': allocation_id
        }

        return {
            'statusCode': 200,
            'body': json.dumps(response_body)
        }
    except Exception as e:
        # Print the exception for debugging
        print(str(e))
        # Return an error response
        return {
            'statusCode': 500,
            'body': 'Internal Server Error'
        }
