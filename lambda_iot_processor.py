import json
import boto3
import os

aws_region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
dynamodb = boto3.resource('dynamodb', region_name=aws_region)
sns = boto3.client('sns', region_name=aws_region)

TABLE_NAME = os.environ.get('VEHICLE_TABLE')
ALERT_TOPIC = os.environ.get('ALERT_TOPIC')

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)
    
    # Assuming 'records' key in the incoming event contains telemetry data
    for record in event.get('records', []):
        vehicle_id = record.get('vehicleId', 'unknown')
        # ...process the record as needed...
        table.put_item(Item={'VehicleId': vehicle_id, 'Data': json.dumps(record)})
        
        # Check for anomaly flag in telemetry
        if record.get('anomaly', False):
            sns.publish(
                TopicArn=ALERT_TOPIC,
                Message=f'Alert: Anomaly detected for Vehicle {vehicle_id}'
            )
    return {"status": "Processed"}
