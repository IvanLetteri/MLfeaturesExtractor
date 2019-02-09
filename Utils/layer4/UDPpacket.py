from dpkt.udp import UDP
from scapy.all import *

'''PEP8 stardard - here description'''

class UDPpacket:

    numPktsUDP = 0

    def __init__(self, pathPCAPfile = "PCAPs/default.pcap"):
        self.pathPCAPFile = pathPCAPfile  # instance variable unique to each instance

    def getNumUDPpkts(self):
        return self.numPktsUDP

    def pktUDPcounter(self):
        print("Reading UDP pkts %s" % self.pathPCAPFile)
        packets = rdpcap(self.pathPCAPFile)
        for pkt in packets:
            if UDP in pkt: self.numPktsUDP += 1