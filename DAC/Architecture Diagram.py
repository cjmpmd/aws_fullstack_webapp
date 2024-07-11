from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.aws.network import Route53, ELB 
from diagrams.programming.framework import Laravel


def worker(x):
    wrk = []
    for i in range(x):
        wrk.append(ECS("worker" + str(i+1)))
    print(wrk)
    return wrk


with Diagram("Full Stack Web Architecture", show=False):

    dns = Route53('DNS Service')
    lb = ELB('LB')
    source = EKS("k8s source")

    with Cluster("AZ1"):
        with Cluster("Event Workers"):
            workers = worker(1)


    dns >> lb >> source
    source >> workers

    

with Diagram("WebApp Architecture", show=False):

    dns = Laravel('App')
    # lb = ELB('LB')
    # source = EKS("k8s source")

    # with Cluster("AZ1"):
    #     with Cluster("Event Workers"):
    #         workers = worker(1)


    # dns >> lb >> source
    # source >> workers