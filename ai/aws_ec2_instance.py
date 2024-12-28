import boto3

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-east-1'  # or any other region of your choice
)

# Create an EC2 client
ec2_client = session.client('ec2')

# Launch EC2 instance
def launch_ec2_instance():
    try:
        response = ec2_client.run_instances(
            ImageId='ami-0c55b159cbfafe1f0',  # Amazon Linux 2 AMI (replace with a valid AMI ID for your region)
            InstanceType='t2.micro',  # Instance type (adjust as needed)
            MinCount=1,  # Minimum number of instances to launch
            MaxCount=1,  # Maximum number of instances to launch
            KeyName='your-key-pair',  # Your SSH key pair name for EC2 login
            SecurityGroupIds=['sg-xxxxxxxx'],  # Replace with your Security Group ID
            SubnetId='subnet-xxxxxxxx',  # Replace with your Subnet ID
            TagSpecifications=[  # Optional: add tags
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Name', 'Value': 'MyEC2Instance'}
                    ]
                }
            ]
        )

        instance_id = response['Instances'][0]['InstanceId']
        print(f'EC2 Instance {instance_id} launched successfully.')
        
        # You can also check the public IP address of the instance after it launches
        instance_details = ec2_client.describe_instances(InstanceIds=[instance_id])
        public_ip = instance_details['Reservations'][0]['Instances'][0].get('PublicIpAddress', 'No Public IP assigned')
        print(f'Public IP Address: {public_ip}')

    except Exception as e:
        print(f'Error launching EC2 instance: {e}')

# Call the function to launch EC2
launch_ec2_instance()

