from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2Instance, AMI, EC2
from diagrams.aws.storage import S3
from diagrams.aws.network import Route53, ELB, InternetGateway, APIGateway
from diagrams.aws.general import InternetGateway as gIG
from diagrams.aws.management import AutoScaling

from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Apache, Nginx
from diagrams.onprem.database import MySQL
from diagrams.onprem.compute import Server
from diagrams.onprem.vcs import Github

from diagrams.programming.framework import Laravel

from diagrams.generic.os import Ubuntu


def nameSpace(index):
    
    if index < 0:
        return "Invalid input: x should be a non-negative integer."
    else:
        return "O" * index

with Diagram("Full Stack Web Architecture", show=False):
# with Diagram("Full Stack Web Architecture", show=False, direction="TB"):
    internet = gIG('internet')
    dns = Route53('DNS Service')
    with Cluster("VPC"):
        igw = InternetGateway('IGW')
        with Cluster("Public Network"):
            aLB = ELB('Application LB')
            with Cluster("ASG \n (Total workers: n > 1 < 7)"):
                AMI = AMI('Template')
                with Cluster("Service Cluster"):
                    ec2 = [
                        EC2('Worker'),
                        EC2('Worker'),
                        EC2('Worker'),
                        
                    ]
                ASG = AutoScaling('ASG')
        nLB = ELB('Network LB')
        with Cluster("Private Network"):
            s3 = S3('')
            apiGW = APIGateway('API GW')
            with Cluster("DB Cluster"):
                CDB = [
                    EC2Instance('DB Slave #1'),
                    # EC2Instance('DB Slave #1'),
                ]
                mDB = MySQL('DB Master')
                mDB >> CDB
            with Cluster("Monitoring"):
                metrics = Prometheus("metric")
                metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")
            
        # ubu  << Apache('') << Nginx('') << Laravel('App') << git
    
    
    with Cluster('Tech Stack'):
        ubu = Ubuntu('Template')
        # git = Github('Repo')
        ubu  << Nginx('') << Laravel('App') \
            #  << git
        
    with Cluster('On prem'):
        OnPremServ = Server('API')
        lrvl = Laravel('App')
        

               

    internet >> dns
    dns >> igw >> aLB 
    aLB >> ASG  >> AMI
    ASG >> ec2
    AMI >> ec2
    AMI << ubu
    ec2 >> nLB
    # nLB >> mDB
    nLB >> apiGW
    apiGW >> s3
    apiGW >> mDB
    apiGW >> metrics
    apiGW - OnPremServ << lrvl
    

with Diagram("WebApp Architecture", show=False):

    lrvl = Laravel('App')
    # lb = ELB('LB')
    # source = EKS("k8s source")

    # with Cluster("AZ1"):
    #     with Cluster("Event Workers"):
    #         workers = worker(1)


    lrvl 