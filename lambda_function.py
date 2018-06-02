from __future__ import print_function
import json
import boto3
print('Loading function')

def lambda_handler(event, context):
    sns = boto3.client('sns')
    numbers = event['PhoneNumber']
    for i in numbers:
        sns.publish(
            MessageAttributes= {
    
                        'AWS.SNS.SMS.SMSType': {
                                                     'DataType': 'String',
                                                     'StringValue': 'Transactional'   
    											},
    											
    				            'AWS.SNS.SMS.SenderID': {
                                                     'DataType': 'String',
                                                     'StringValue': 'ABCDEF'   
    											}
    					},
            PhoneNumber = i,
            Message = event['Message']
        )
    return {'code': 0, 'Message': 'success'}
 
