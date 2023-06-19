# Lambda Function - Resource Allocation

This is a Lambda function written in Python that provisions EC2 instances and allocates resources based on user requests. It exposes an API endpoint that accepts POST requests to allocate resources.

## Prerequisites

- AWS account with appropriate permissions to create EC2 instances.
- Postman or any API testing tool to send requests.

## Setup

1. Clone the repository:


2.Create a new AWS Lambda function in the AWS Management Console.

3.Configure the Lambda function:

  Runtime: Python 3.8
  Execution role: Choose an existing role with EC2 permissions or create a new one with the necessary permissions.
4.Deploy the code to Lambda:

  Zip the contents of the cloned repository.
  Upload the zip file to the Lambda function you created in step 3.
5.Set up API Gateway:

  Create a new REST API in the AWS Management Console.
  Add a new resource.
  Configure the resource to use the Lambda function as the integration.
6.Deploy the API:

  Create a new deployment stage in API Gateway.
  Note down the API endpoint URL.
  
  
API Usage
To allocate resources, send a POST request to the API endpoint URL using Postman or any API testing tool. Provide the request body in JSON format:

json
Copy code
{
    "resource_type": "t3.2xlarge",
    "quantity": 1,
    "user_info": {
        "name": "Avinash",
        "email": "avinash@gmail.com"
    }
}



Lambda Function Details
The Lambda function consists of the following files:

lambda_function.py: Contains the main logic for provisioning EC2 instances and allocating resources.
requirements.txt: Specifies the required Python dependencies.
lambda_function.py
This file contains the Python code for the Lambda function. It consists of the following functions:

allocate_resources(resource_type, quantity, user_info): Provisions EC2 instances based on the provided resource type, quantity, and user information. Returns a unique allocation ID.
lambda_handler(event, context): The entry point for the Lambda function. Parses the request body, calls allocate_resources, and prepares the response.
Request Flow
The Lambda function receives a POST request with a JSON request body.
The request body is parsed, and the resource type, quantity, and user information are extracted.
The allocate_resources function is called with the extracted parameters.
EC2 instances are provisioned using the AWS SDK (boto3), and a unique allocation ID is generated.
The allocation ID is included in the response body.
The response is returned as a JSON object.
Error Handling
If an exception occurs during the execution of the Lambda function, an error response with status code 500 and the message "Internal Server Error" is returned.






