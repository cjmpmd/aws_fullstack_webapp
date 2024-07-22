from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2Instance, AMI, EC2
from diagrams.aws.network import Route53, ELB, InternetGateway
from diagrams.aws.general import InternetGateway as gIG
from diagrams.aws.management import AutoScaling

from diagrams.onprem.database import MySQL

with Diagram("Full Stack Web Architecture", show=False):
    internet = gIG('internet')
    dns = Route53('DNS Service')
    with Cluster("Security VPC"):
        igwSec = InternetGateway('IGW')
        with Cluster("Public Network"):
            basti = EC2Instance('Bastion Host')
    with Cluster("VPC"):
        igw = InternetGateway('IGW')
        with Cluster("Public Network"):
            aLB = ELB('Application LB')
            with Cluster("ASG"):
                AMI = AMI('Template')
                with Cluster("Service Cluster \n (Total workers: n > 1 < 7)"):
                    ec2 = [
                        EC2('Worker 6'),
                        EC2('Worker (n)'),
                        EC2('Worker 1'),
                        
                    ]
                ASG = AutoScaling('ASG')
        nLB = ELB('Network LB')
        with Cluster("Private Network"):
            with Cluster("DB Cluster"):
                CDB = [
                    MySQL('DB Master')
                                    ]
                mDB = EC2Instance('DB Slave #1')
                mDB << CDB
                
    internet >> dns
    igwSec >> basti 
    basti >> ec2
    basti >> mDB

    dns >> igw >> aLB 
    aLB >> ASG  >> AMI
    ASG >> ec2
    AMI >> ec2
    ec2 >> nLB
    
    nLB >> mDB