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
from diagrams.onprem.vcs import Gitlab, Github

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
            s3 = S3('')
            apiGW = APIGateway('API GW')
            with Cluster("DB Cluster"):
                CDB = [
                    MySQL('DB Master')
                    
                    # EC2Instance('DB Slave #1'),
                ]
                mDB = EC2Instance('DB Slave #1')
                mDB << CDB
            # with Cluster("Monitoring"):
            #     metrics = Prometheus("metric")
            #     metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")
            
        # ubu  << Apache('') << Nginx('') << Laravel('App') << git
    
    
    with Cluster('On prem'):
        with Cluster('API'):
            OnPremServ = Server('API')
            lrvl = Laravel('API')
        with Cluster('Tech Stack'):
            ubu = Ubuntu('Template')
            # git = Github('Repo')
            site = Laravel('Web site') 
            ubu  << Nginx('') << site
                
        with Cluster('VCS'):
            Repo = [
                # Gitlab('Internal VCS'),
                Github('External VCS'),
            ]

        
        

               

    internet >> dns
    igwSec >> basti 
    # basti >> aLB
    basti >> ec2
    basti >> mDB

    dns >> igw >> aLB 
    aLB >> ASG  >> AMI
    ASG >> ec2
    AMI >> ec2
    ec2 << ubu
    ec2 >> nLB
    # nLB >> mDB
    nLB >> apiGW
    nLB >> mDB
    apiGW >> s3
    # apiGW >> mDB
    # apiGW >> metrics
    ec2 - OnPremServ << lrvl 
    lrvl << Repo
    site << Repo
    

with Diagram("WebApp Architecture", show=False):

    lrvl = Laravel('App')
    with Cluster('DevCycle'):
        site = [
            Server('Prod'),
            Server('Test'),
            Server('Dev'),
        ]
    with Cluster('MVC Architecture'):
        arch = Server('')
    with Cluster('Workflow'):
        with Cluster('Auth'):
            reg = Server('Register')
            login = Server('Login') 
            workflow = login - reg
        with Cluster('User'):
            acc = Server('Account') 
            rsm = Server('rsm') 
            hist = Server('history') 
    with Cluster('Controller'):
        with Cluster('Database'):
            db = MySQL('DB')
        with Cluster('Storage'):
            storage = MySQL('DB')


    # lb = ELB('LB')
    # source = EKS("k8s source")

    # with Cluster("AZ1"):
    #     with Cluster("Event Workers"):
    #         workers = worker(1)


    lrvl >> site >> arch
    arch >> login
    arch << db
    arch << storage
    login >> rsm
    rsm - acc
    rsm - hist