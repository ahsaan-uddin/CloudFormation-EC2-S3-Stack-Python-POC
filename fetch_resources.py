import boto3

def fetch_stack_resources(stack_name):
    cf = boto3.client('cloudformation', region_name='ap-south-1')
    ec2 = boto3.client('ec2')
    s3 = boto3.client('s3')

    print(f"Fetching resources for stack: {stack_name}")

    try:
        response = cf.describe_stack_resources(StackName=stack_name)
        resources = response['StackResources']

        print("\n--- Stack Resources ---")
        for res in resources:
            print(f"{res['LogicalResourceId']} - {res['ResourceType']}")

        print("\n--- EC2 Instances ---")
        ec2_instances = ec2.describe_instances()
        for reservation in ec2_instances['Reservations']:
            for instance in reservation['Instances']:
                print(f"Instance ID: {instance['InstanceId']} | State: {instance['State']['Name']}")

        print("\n--- S3 Buckets ---")
        s3_buckets = s3.list_buckets()
        for bucket in s3_buckets['Buckets']:
            print(f"Bucket Name: {bucket['Name']}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    stack_name = input("Enter your CloudFormation Stack Name: ")
    fetch_stack_resources(stack_name)
