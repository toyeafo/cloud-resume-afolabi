import boto3
import json

table = boto3.client('dynamodb')

def lambda_handler(event, context):

    get_data_from_table = table.get_item(
      TableName = "VisitorData",
      Key = {
        'VisitorID': { 'S': "visitor" },
        'TimeStamp': { 'S': "1699805157.373333" },
      },
      ProjectionExpression = "VisitorCount")
    
    
    put_data_in_table = table.update_item(
      TableName = "VisitorData",
      Key = {
        'VisitorID': { 'S': "visitor" },
        'TimeStamp': { 'S': "1699805157.373333" },
      },
      UpdateExpression = "SET VisitorCount = VisitorCount + :val",
      ExpressionAttributeValues = { ":val": { 'N': "1" } },
      ReturnValues = "UPDATED_NEW",
    )
    
    # response = json.dumps(get_data_from_table)
    
    return get_data_from_table["Item"]["VisitorCount"]["N"]