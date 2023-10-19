import boto3
import requests
import datetime

dynamodb = boto3.resource('dynamodb')
timestamp = str(datetime.datetime.utcnow().timestamp())
response = requests.get("https://api.countapi.xyz/get/toyeafolabi-resume.com/f0becf7d-b511-4321-9c3d-5837846cc561").json()
print(response['value'])

table = dynamodb.Table('VisitorData')

table.put_item(
    Item={
        'VisitorID': 1,
        'TimeStamp': timestamp,
        'IpAddress': "",
        'WebsiteVisitCount': response['value'],
    }
)

print(table.item_count)