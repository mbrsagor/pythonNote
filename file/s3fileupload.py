import boto3
s3 = boto3.client('s3')
s3.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')

