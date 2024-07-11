from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2Instance, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

from diagrams.onprem.database import MySQL
from diagrams.aws.network import Route53, ELB 
from diagrams.programming.framework import Laravel
from diagrams.onprem.storage import CEPH_OSD
from diagrams.generic.virtualization import Virtualbox
from diagrams.generic.os import Ubuntu

from diagrams.generic.network import Firewall, Router


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

    dns = Route53('DNS Service')
    lb = ELB('LB')

    with Cluster("Virtual Machine"):
        with Cluster("Services"):
            workers = worker(1)
        with Cluster("DB"):
            db = MySQL('State')
        with Cluster("File Storage"):
            storage = CEPH_OSD('Storage')
            


    dns >> lb >> workers >> db
    workers >> storage
    db >> workers
    storage >> workers

    

with Diagram("WebApp Architecture", show=False):

    lrvl = Laravel('App')
    # lb = ELB('LB')
    # source = EKS("k8s source")

    # with Cluster("AZ1"):
    #     with Cluster("Event Workers"):
    #         workers = worker(1)


    lrvl 