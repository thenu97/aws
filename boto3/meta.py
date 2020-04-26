## listing the regions avaliable for ec2 instance

import boto3

aws_con=boto3.session.Session(profile_name="root")

ec2_res=aws_con.resource(service_name="ec2")

# we're unable to find an attribute associated with resource that will provide us the regions 

# but client has an attribute
print(dir(ec2_res))
print(ec2_res.meta.client.describe_regions()['Regions'])

for each_item in ec2_res.meta.client.describe_regions()['Regions']:
    print(each_item['RegionName'])