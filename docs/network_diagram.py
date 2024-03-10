from diagrams import Cluster, Diagram, Edge
from diagrams.generic.compute import Rack
from diagrams.generic.network import Firewall

with Diagram("Network", show=False):
    dummy = Rack("dummy\ninternal:192.168.203.101/24")
    
    with Cluster("Keepalived Cluster\nglobal:192.168.201.10/24\ndmz:192.168.202.10/24\ninternal:192.168.203.10/24"):
        extfw01 = Firewall("extfw01\nglobal:192.168.201.11/24\ndmz:192.168.202.11/24\ninternal:192.168.203.11/24")
        extfw02 = Firewall("extfw01\nglobal:192.168.201.12/24\ndmz:192.168.202.12/24\ninternal:192.168.203.12/24")

    dummy >> Edge(color="firebrick", label="internal") >> extfw01
    dummy >> Edge(color="firebrick", label="internal") >> extfw02
