import json
import boto3
import csv
import codecs
import os

BATCH_SIZE = int(os.environ['BATCH_SIZE'])
TABLE_NAME = os.environ['TABLE_NAME']
s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    print(event)
    KEY = event['Records'][0]['s3']['object']['key']
    BUCKET_NAME = event['Records'][0]['s3']['bucket']['name']

    try:
        obj = s3.Object(BUCKET_NAME, KEY).get()['Body']
    except:
        print('S3 Object could not be opened. Check environment variable.')

    batch = []
    for row in csv.DictReader(codecs.getreader('utf-8')(obj)):
        if len(batch) >= BATCH_SIZE:
            write_to_dynamo(batch)
            batch.clear()
        batch.append(row)

    if batch:
        write_to_dynamo(batch)

    return {
        'statusCode': 200,
        'body': json.dumps('Uploaded file to dynamo')
    }

def write_to_dynamo(rows):
    try:
        table = dynamodb.Table(TABLE_NAME)
    except:
        print('Error loading the table')

    try:
        with table.batch_writer() as batch:
            for i in range(len(rows)):
                batch.put_item(Item=rows[i])
    except Exception as e:
        print('Error executing batch writer')
        print(e)