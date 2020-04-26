import boto3

#creating aws console
aws_con=boto3.session.Session(profile_name="root")




ec2_res=aws_con.resource(service_name="ec2", region_name="eu-west-2")
ec2_cli=aws_con.client(service_name="ec2", region_name="eu-west-2")
print(dir(aws_con))

print(aws_con.get_available_resources())