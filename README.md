# System Monitoring and Alerting Tool

## Overview
This tool is designed for Site Reliability Engineers (SREs) and system administrators to monitor key system metrics such as CPU usage, memory utilization, and disk space. When any of these metrics exceed predefined thresholds, an alert message is generated and sent via AWS Simple Notification Service (SNS).

## Features
- **System Metrics Monitoring:** Tracks CPU, memory, and disk usage.
- **Threshold-Based Alerting:** Triggers alerts when metrics exceed certain thresholds.
- **AWS SNS Integration:** Sends alert messages through AWS Simple Notification Service.

## Prerequisites
- Python 3.x
- `psutil` library
- `boto3` library
- AWS account with configured AWS SNS Topic

## Installation
1. **Clone the Repository:**
2. **Install Required Libraries:**
3. **Configuration:**
- Update the AWS SNS Topic ARN in the script where indicated (If you intend on sending the alerts).

## Usage
Run the script using Python:

The script will monitor the system metrics and, if any threshold is breached, it will send an alert to the configured AWS SNS Topic.

## Functionality

1. **Metrics Monitoring:**
   - The script uses `psutil` to gather system metrics.

2. **Alerting Logic:**
   - If any metric exceeds the predefined threshold, an alert message is constructed.

3. **Sending Alerts:**
   - Alerts are sent via AWS SNS, using credentials configured in the AWS CLI or boto3.

## Customization
You can customize the threshold values and add more system metrics as per your requirements by editing the `define_metric_thresholds` and `get_current_system_metrics` functions.

## Note
Ensure that your AWS credentials are properly configured for `boto3` to send notifications through SNS.

## License
This project is licensed under the [MIT License](LICENSE).
