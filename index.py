import json
import datetime
import boto3


def handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    # metrics = [{e.metric_name, e.metric_value} for e in event]
    if event is None:
        data = {
            'output': 'Hello World',
            'timestamp': datetime.datetime.utcnow().isoformat()
        }
        return {'statusCode': 200,
                'body': json.dumps(data),
                'headers': {'Content-Type': 'application/json'}}
    if event.metric_name is None:
        raise Exception('Missing metric_name parameter')
    if event.metric_value is None:
        raise Exception('Missing metric_value parameter')
    if event.user_id is None:
        raise Exception('Missing user_id parameter')

    response = cloudwatch.put_metric_data(
        MetricData=[
            {
                'MetricName': event.metric_name,
                'Dimensions': [
                    {
                        'Name': 'Name',
                        'Value': event.user_id
                    },
                ],
                'Unit': 'None',
                'Value': event.metric_value
            },
        ],
        Namespace='AWS/PGM'
    )
