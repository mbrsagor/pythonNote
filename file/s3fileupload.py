import boto3
s3 = boto3.client('s3')
s3.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')

"""
pip3 install boto3
"""

# Another Way

REGION = 'us-east-1' 
ACCESS_KEY_ID = 'paste_here_your_key_id' 
SECRET_ACCESS_KEY = 'paste_here_your_secret_access_key' PATH_IN_COMPUTER = 'path/in/computer/namefile.txt' 
BUCKET_NAME = 'vperezb' 
KEY = 'path/in/s3/namefile.txt' # file path in S3 

s3_resource = boto3.resource(
    's3', 
    region_name = REGION, 
    aws_access_key_id = ACCESS_KEY_ID,
    aws_secret_access_key = SECRET_ACCESS_KEY
) 
s3_resource.Bucket(BUCKET_NAME).put_object(
    Key = KEY, 
    Body = open(PATH_IN_COMPUTER, 'rb')
)


