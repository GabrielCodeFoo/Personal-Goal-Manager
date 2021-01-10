import json
import datetime
import boto3


def handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    # metrics = [{e.metric_name, e.metric_value} for e in event]
    if not event.metric_name:
        raise Exception('Missing metric_name parameter')
    if not event.metric_value:
        raise Exception('Missing metric_value parameter')
    if not event.user_id:
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
