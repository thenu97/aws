import boto3
import time

#creating aws console
aws_con=boto3.session.Session(profile_name="root")

ec2_res=aws_con.resource(service_name="ec2", region_name="eu-west-2")

my_inst_ob = ec2_res.Instance("instanceid")
print("starting given instance....")
print(dir(my_inst_ob))
my_inst_ob.start()

'''#using python
while True:
    my_inst_ob = ec2_res.Instance("instanceid")
    print("the current status of ec2 is: ", my_inst_ob.state['Name'])
    if my_inst_ob.state['Name'] == 'running':
        break
    print("waiting for the status to change to running from pending")
    time.sleep(5)
print("Now your instance is up and running")'''

#this can be achieved through the concept of waiters in boto3
my_inst_ob.wait_until_running() #resource waiter waits for 200secs(40 checks, check every 5 seconds)
print("Now your instance is up and running")

######################################################################

#using client
aws_con=boto3.session.Session(profile_name="root")

ec2_cli=aws_con.client(service_name="ec2", region_name="eu-west-2")

print("starting given instance....")
ec2_cli.start_instances(InstanceIds=["instance_id"]) 
waiter = ec2_cli.get_waiter('instance_running') # (40 checks, check every 15 seconds)
waiter.wait(InstanceIds=["instance_id"])
print("Now your instance is up and running")

#########################################################################

#start instance using resource and attach waiter from client 
#we'd want to do this because in real time, it might take longer so waiting 15 seconds is better than 5

my_inst_ob=ec2_res.Instance("instance_id")
print("starting given instance....")
my_inst_ob.start()
waiter = ec2_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=["instance_id"])
print("Now your instance is up and running")