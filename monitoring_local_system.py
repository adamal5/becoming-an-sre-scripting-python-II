import psutil
import boto3

# Define the metrics we will monitor using a dictionary
def get_current_system_metrics():
    return {
        'CPU': psutil.cpu_percent(interval=1),
        'Memory': psutil.virtual_memory().percent,
        'Disk': psutil.disk_usage('/').percent
    }

# Define the thresholds in a dictionary
def define_metric_thresholds():
    return {
        'CPU': 1.0,
        'Memory': 1.0,
        'Disk': 1.0
    }

# Define a message template
message_template = '''Hey SRE,

It looks like your system is experiencing some issues. 
Please see the details below:
'''

signature = '''Kind regards,
The SRE Team
'''

# Conditional alerting using dictionaries
def check_metric_thresholds(metrics, thresholds):
    message = message_template
    is_breached = False

    for metric_name, metric_value in metrics.items():
        threshold_value = thresholds[metric_name]
        if metric_value > threshold_value:
            message += f"\n{metric_name} usage: {metric_value}%, Threshold: {threshold_value}%"
            is_breached = True

    if not is_breached:
        print('There has been no breach')
        return ''
    print(message)
    return message + "\n\n" + signature

# Send an alert using AWS SNS
def send_message_via_sns(alert_message):
    client = boto3.client('sns')
    response = client.publish(
        TopicArn='ADD YOUR AWS TOPIC ARN HERE',
        Message=alert_message,
        Subject='System Threshold Breach',
        MessageAttributes={
            'myAttributes': {
                'DataType': 'String',
                'StringValue': 'myValue',
            }
        }
    )
    print(response)

# Print the Outcomes to check 
metrics = get_current_system_metrics()
thresholds = define_metric_thresholds()
alert_message = check_metric_thresholds(metrics, thresholds)
# response_message = send_message_via_sns(alert_message)
