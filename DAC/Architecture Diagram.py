from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2Instance, EKS, Lambda, AMI ,EC2Instances, EC2
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.aws.network import Route53, ELB, InternetGateway, APIGateway
from diagrams.aws.general import InternetGateway as gIG


from diagrams.onprem.monitoring import Grafana, Prometheus

from diagrams.aws.management import AutoScaling





from diagrams.programming.framework import Laravel
from diagrams.onprem.database import MySQL
from diagrams.onprem.storage import CEPH_OSD
from diagrams.onprem.compute import Server


from diagrams.generic.virtualization import Virtualbox
from diagrams.generic.os import Ubuntu


from diagrams.generic.network import Firewall, Router
import prometheus_client

def nameSpace(index):
    
    if index < 0:
        return "Invalid input: x should be a non-negative integer."
    else:
        return "O" * index
def worker(x):
    wrk = []
    for i in range(x):
        wrk.append(EC2Instance("EC2"))
    return wrk


# with Diagram("Refactor App", show=False):

#     rtr = Router('Router')
#     fw = Firewall('FW')
#     # lb = ELB('LB')
#     vm = Virtualbox('Hypervisor t-1')

#     with Cluster("Virtual Machine"):
#         with Cluster("Services"):
#             workers = Ubuntu('OS')
#         with Cluster("DB"):
#             db = MySQL('State')
#         with Cluster("File Storage"):
#             storage = CEPH_OSD('Storage')
            


#     rtr >> fw >> vm >> workers >> db
#     workers >> storage
#     db >> workers
#     storage >> workers


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
                ]
                mDB = MySQL('DB Master')
                mDB >> CDB
            with Cluster("Monitoring"):
                metrics = Prometheus("metric")
                metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")
            
        ubu = Ubuntu('Template')
        
    with Cluster('On prem'):
        lrvl = Laravel('App')
        OnPremServ = Server('API')
    AMI << ubu

            
    

    internet >> dns
    # internet >> OnPremServ
    dns >> igw >> aLB 
    aLB >> ASG  >> AMI
    ASG >> ec2
    AMI >> ec2
    ec2 >> nLB
    nLB >> mDB
    nLB >> apiGW
    apiGW >> s3
    apiGW >> metrics
    apiGW >> lrvl >> OnPremServ
    # # internet >> lrvl >> OnPremServ
    # lb >> igw2 >> igw2pb >> igw2pr 

    # igw1pr << OnPremServ
    # igw2pr << OnPremServ
    # workers >> storage

    

with Diagram("WebApp Architecture", show=False):

    lrvl = Laravel('App')
    # lb = ELB('LB')
    # source = EKS("k8s source")

    # with Cluster("AZ1"):
    #     with Cluster("Event Workers"):
    #         workers = worker(1)


    lrvl 