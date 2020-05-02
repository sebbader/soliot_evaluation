import boto3


if __name__ == '__main__':
    ec2 = boto3.resource('ec2')

    user_data_script = """#!/bin/bash
        export SOLIOT_SERVER_URI="https://$(curl http://169.254.169.254/latest/meta-data/public-hostname 2>/dev/null)"
        export SOLIOT_EVALKEY='<YOUR_EVALKEY>'
        screen -S soliot -d -m
        screen -r soliot -X stuff $'cd /home/admin/SolIoT \n node bin/solid start \n'
       """

    # To ensure faster instance launches, break up large requests into smaller batches. For example, create five
    # separate launch requests for 100 instances each instead of one launch request for 500 instances.
    n = 10

    # create a new EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-0ab9ca8015970a6f3',
        MinCount=1,
        MaxCount=n,
        InstanceType='t2.micro',
        KeyName='SolIoT',
        SecurityGroups=['SolIoT-FRA'],
        TagSpecifications=[{'ResourceType': 'instance',
                            'Tags': [{'Key': 'Name', 'Value': 'solibot'}]}],
        UserData=user_data_script
    )
