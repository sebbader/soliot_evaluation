import boto3


# Get all instances with tag "Name:solibot"
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': ['solibot']}])

for instance in instances:
    instance.terminate()

instances = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': ['solid']}])

for instance in instances:
    instance.terminate()