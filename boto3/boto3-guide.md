# Boto3
+ AWS SDK (software developement kit) for python
+ enables create, configure & management of aws services
+ object-oreintated api 


## Concepts:
    1. Sessions
    2. Resource
    3. Client
    4. Meta
    5. Collections
    6. Waiters
    7. Paginators


## Sessions
+ Sessions typically store: 
    1. credentials
    2. region
    3. other configurations

+ Two types:
    1. Default Session
        - aws configure (the credientials are stored under default)
        - immediately go ahead and run 
            ``` 
            sqs = boto3.client('sqs') 
            OR
            s3 = boto3.resource('s3')
        
        - useful for when you are only going to be using one user account

    2. Custom Session
        - aws configure --profile [add IAM user name] 
        - you can build a console from that
        - aws_con = boto3.session.Session()
        - ``` 
            sqs = aws_con.client('sqs')
            OR
            sqs = aws_con.resource('s3')


## Resource & Client
- Resource & Client are concepts that creates service console for aws services such as:
    1. IAM
    2. EC2
    3. S3 & etc

- Two ways to access aws services:
    1. Resource
        -   ``` 
            iam_con_res = aws_con.resource(service_name="iam", region_name="eu-west-2")
        - region_name doesn't need to be specified but if you'd like to access the service in another region then that's how you'd do it. 

    2. Client
        -   ``` 
            iam_con_cli = aws_con.client(service_name="iam", region_name="eu-west-2")

- So which is better if they both do the same thing?
    -   ``` 
        aws_con = boto3.session.Session(profile_name="root")
        print(dir(aws_con))
    
    - This will show you the a list of attributes associated with aws console

    -   ``` 
        print(aws_con.get_available_resources())

    - This will show you a list of services out of 100s that can be accessed by resource.

    - Output: 
        ```
        ['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']

- By default, you can access all aws services via Client. So why don't we just stick to client? What's the need for resource?
    - Resource is high-level object oreintated service access. The output is an object
    - Client is low-level service access. The output is a dictionary so more work to play around with


## Waiter
- A way to block until a certain state has been reached
- Waiters are avaliable for both resource and client but client waiters are better to use in real time


## Meta
- Useful to enter into client object from resource 
- We have every required operation via client object. This isn't the same for resource object. So let's say you started a code with resource object and then realised later on that the operation you wanted to perform isn't avaliable. Through Meta, you don't have to start your code from scratch again. 

