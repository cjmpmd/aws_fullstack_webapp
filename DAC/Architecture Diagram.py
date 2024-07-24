from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2Instance, AMI, EC2
from diagrams.aws.network import NATGateway, ELB, InternetGateway
from diagrams.aws.general import InternetGateway as gIG
from diagrams.aws.management import AutoScaling

from diagrams.onprem.database import MySQL

with Diagram("Full Stack Web Architecture", show=False):
    internet = gIG('internet')
    # dns = Route53('DNS Service')
    with Cluster("Security VPC"):
        igwSec = InternetGateway('IGW')
        with Cluster("Public Network"):
            basti = EC2Instance('Bastion Host')
    with Cluster("VPC"):
        with Cluster("AZ #n"):
            igw = InternetGateway('IGW')
            with Cluster("Public Network"):
                aLB = ELB('Application LB')
                with Cluster("Service Cluster \n (Total workers: n > 2 < 7)"):
                    ec2 = [
                        EC2('Worker (n)'),
                        EC2('Worker (n)')
                    ]
                    sCluster =EC2Instance('DB Slave #1')
                    
            with Cluster("Private Network"):
                with Cluster("DB Cluster"):
                    CDB = [
                        MySQL('DB Master')
                                        ]
                    mDB = EC2Instance('DB Slave #1')
                    mDB << CDB
        with Cluster("ASG"):
            AMI = AMI('AMI Image')
            ASG = AutoScaling('ASG')
            # nLB = ELB('Network LB')
                    
    internet >> igw
    internet >> igwSec >> basti 
    basti >> ec2
    basti >> mDB

    igw >> aLB 
    ASG  >> AMI
    aLB >> ec2
    sCluster >> ec2
    AMI >> sCluster
    ec2 >> mDB
    