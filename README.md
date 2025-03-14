# IoT for Theft-proof Vehicles

## Overview
This project leverages AWS IoT Core using the MQTT protocol to create an anti-theft system for vehicles.

## Deployment
1. Deploy the CloudFormation stack:
   ```sh
   aws cloudformation deploy --template-file cloudformation.yaml --stack-name IoTTheftProofSystem
   ```

2. Register and manage device certificates:
   ```sh
   aws iot create-keys-and-certificate --set-as-active
   ```

## Usage
1. Connect your device to AWS IoT Core using the generated certificates.
2. Publish telemetry data to the MQTT topic.
3. Monitor logs and alerts in AWS CloudWatch.

## Troubleshooting
- Ensure your device certificates are valid and active.
- Check CloudWatch logs for detailed error messages.

## Future Enhancements
- Add a user interface for real-time monitoring.
- Implement OTA firmware updates for devices.
