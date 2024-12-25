import boto3

# Initialize RDS client
rds = boto3.client('rds')

# Modify DB instance
response = rds.modify_db_instance(
    DBInstanceIdentifier='your-db-instance-identifier',
    MasterUserPassword='your-new-password',
    ApplyImmediately=True
)

print("Password reset initiated:", response)

