import boto3

aws_con = boto3.session.Session(profile_name="root")


######## resource ########

ec2_re = aws_con.resource(service_name="ec2", region_name="eu-west-2")

#volumes is a collection object
'''for i in ec2_re.volumes.all():
    print(i.id, i.state)'''

#only want unused volumes
f1 = {"Name":"status", "Values":['avaliable']}
for i in ec2_re.volumes.filter(Filters=[f1]):
    print(i.id, i.state)

#only want untagged 
f1 = {"Name":"status", "Values":['avaliable']}
for i in ec2_re.volumes.filter(Filters=[f1]):
    if i.tags == None:
        print(i.id, i.state)
    
#deleting unused & untagged volumes
f1 = {"Name":"status", "Values":['avaliable']}
for i in ec2_re.volumes.filter(Filters=[f1]):
    if i.tags == None:
        print(i.id, i.state)
        print("deleting volumes!")
        i.delete()


######## client ########

ec2_cli = aws_con.client(service_name="ec2", region_name="eu-west-2")
for i in ec2_cli.describe_volumes()['Volumes']:
    print(i)
    break
    if not "Tags" in i and i['State'] == 'avaliable':
        print(i['VolumeId'])

#deleting volumes via client
for i in ec2_cli.describe_volumes()['Volumes']:
    if not "Tags" in i and i['State'] == 'avaliable':
        print('Deleting ', i['VolumeId'])
        ec2_cli.delete_volume(VolumeId=i['VolumeId'])
print("Deleted all the untagged unused volumes")