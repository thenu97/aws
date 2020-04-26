import boto3

#creating aws console
aws_con=boto3.session.Session(profile_name="root")
ec2_res=aws_con.resource(service_name="ec2", region_name="eu-west-2")
ec2_cli=aws_con.client(service_name="ec2", region_name="eu-west-2")

''' #### all ####
for i in ec2_res.instances.all():
    print(i)

#### limit ####
for i in ec2_res.instances.limit(1):
    print(i)

#### filter ####
f1={"Name": "instance-state-name", "Values":['running', 'stopped']}
f2={"Name": "instance-type", "Values":['t2.micro']}
for i in ec2_res.instances.filter(Filters=[f1, f2]):
    print(i)

#### start ####
#collecting all the instance_id
instance_id = []
for i in ec2_res.instances.all():
    instance_id.append(i.id)

print("starting your instances")
ec2_res.instances.start()
waiter.wait(InstanceIds=instance_id)
print("instances are now up and running")'''

#### create_tags ####
# want to start an instance with a certain name

np_sers_id = []
f1 = {"Name": "tag:Name", "Values":['ubuntu']}
for i in ec2_res.instances.filter(Filters=[f1]):
    np_sers_id.append(i.id)

print(np_sers_id)
for j in ec2_cli.describe_instances()['Reservations']:
    for i in j['Instances']:
        print(i['InstanceId'])

#apply filters
for j in ec2_cli.describe_instances(Filters=[f1])['Reservations']:
    for i in j['Instances']:
        print(i['InstanceId'])