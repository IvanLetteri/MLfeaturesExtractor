from dpkt.tcp import TCP
from scapy.all import *

'''PEP8 stardard - here description'''

class TCPpacket:
    FIN = 0x01
    SYN = 0x02
    RST = 0x04
    PSH = 0x08
    ACK = 0x10
    URG = 0x20

    dictFlags = {"syn": 0, "fin": 0, "psh": 0, "rst": 0, "urg": 0, "ack": 0}
    numPktsTCP = 0

    def __init__(self, pathPCAPfile = "PCAPs/default.pcap"):
        self.pathPCAPFile = pathPCAPfile  # instance variable unique to each instance

    def getNumTCPpkts(self):
        return self.numPktsTCP

    def getDictTCPflags(self):
        return self.dictFlags

    def flagTCPcounter(self):
        print("Reading TCP pkts %s" % self.pathPCAPFile)
        packets = rdpcap(self.pathPCAPFile)
        for pkt in packets:
            if TCP in pkt:
                self.numPktsTCP += 1
                F = pkt['TCP'].flags  # this should give you an integer
                # FIN flag activated
                if F & self.FIN: self.dictFlags["fin"] += 1
                # SYN flag activated
                if F & self.SYN: self.dictFlags["syn"] += 1
                # PSH flag activated
                if F & self.PSH: self.dictFlags["psh"] += 1
                # ACK flag activated
                if F & self.ACK: self.dictFlags["ack"] += 1
                # URG flag activated
                if F & self.URG: self.dictFlags["urg"] += 1
                # ACK flag activated
                if F & self.RST: self.dictFlags["rst"] += 1