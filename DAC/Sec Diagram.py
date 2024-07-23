from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2Instance, AMI, EC2
from diagrams.aws.network import ELB, InternetGateway
from diagrams.aws.general import InternetGateway as gIG
from diagrams.onprem.client import Users, Client

from diagrams.onprem.database import MySQL

with Diagram("Security Architecture Diagram", show=False):
    
    users = Users('End Users')
    client = Client('Maintenance Client')
    with Cluster("VPC: Security"):
        igwSec = InternetGateway('IGW')
        with Cluster("Maintenance Endpoint \n (Public Network)"):
            basti = EC2Instance('Bastion Host')
    with Cluster("VPC: Production"):
        igw = InternetGateway('IGW')
        with Cluster("ALB SG \n (Public Network) \n Public IP \n Bastion whitelist"):
            aLB = ELB('Application LB')
        with Cluster("EC2 workers SG \n (Public Network) \n No Public IP \n Bastion whitelist"):
            with Cluster("Service Cluster \n (Total workers: n > 2 < 7)"):
                ec2 = [
                    EC2('Workers'),   
                    EC2('Workers'),   
                ]
        with Cluster("DB SG \n (Private Network) \n No Public IP \n Bastion whitelist"):
    # nLB = ELB('Network LB')
            CDB = MySQL('DB Master')
            mDB = EC2Instance('DB Slave #1 ')
            mDB << CDB
                    
    users >> igw
    client >> igwSec >> basti 
    # basti >> ec2
    basti >> aLB

    igw >> aLB 
    aLB >> ec2
    
    ec2 >> mDB
    