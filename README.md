# lambda-etl-csv-s3-dynamo

This is a project to convert a csv file inside a S3 bucket into a dynamodb table using lambda.

![Cloud formation designer image](../assets/cloudformation-designer.png?raw=true)

The image above is from the cloudformation template that creates the components necessary for the job. When a file is uploaded to the S3 bucket an event starts the lambda function that will read the csv from the bucket and insert the data on the dynamodb table. The cloudformation creates the permissions and the role needed for the lambda function log to cloudwatch, access the S3 bucket and insert data on the table.

The project was developd using the aws serverless application model ([sam](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)). Sam is a framework to build serverless applications and makes it easier to test serverless applications locally with it's cli.

## Getting started

* [Install](https://docs.docker.com/get-docker/) docker (if you want to test it locally)
* [Install](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) aws cli
* [Install](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) aws sam cli

## Deploying the application on aws

```bash
git clone https://github.com/caiocsgomes/lambda-etl-csv-s3-dynamo.git
cd lambda-etl-csv-s3-dynamo
sam deploy --guided
```

## Testing the application locally

```bash
sam local invoke -e events/s3-put-event.json
```