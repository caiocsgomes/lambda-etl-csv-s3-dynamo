# lambda-etl-csv-s3-dynamo

This is a project to convert a csv file inside a s3 bucket into a dynamo db table using lambda.

![Demo Animation](../assets/![Cloud formation designer image](../assets/demo.gif?raw=true))

The image above is from the cloudformation template that creates the components necessary for the job. When a file is uploaded to the S# bucket an event starts the lambda function that will read the csv from the bucket and insert the data on the dynamodb table. The cloudformation creates the permissions and the role needed for the lambda function log to cloudwatch, access the S3 bucket and insert data on the table.