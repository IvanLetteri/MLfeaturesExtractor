from dpkt.udp import UDP
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR

class DNSpacket:
    types = {0: 'ANY', 255: 'ALL', 1: 'A', 2: 'NS', 3: 'MD', 4: 'MD', 5: 'CNAME',
             6: 'SOA', 7: 'MB', 8: 'MG', 9: 'MR', 10: 'NULL', 11: 'WKS', 12: 'PTR',
             13: 'HINFO', 14: 'MINFO', 15: 'MX', 16: 'TXT', 17: 'RP', 18: 'AFSDB',
             28: 'AAAA', 33: 'SRV', 38: 'A6', 39: 'DNAME'}

    dictTypes = {"syn": 0, "fin": 0, "psh": 0, "rst": 0, "urg": 0, "ack": 0}
    numPktsDNS = 0

    def __init__(self, pathPCAPfile = "PCAPs/default.pcap"):
        self.pathPCAPFile = pathPCAPfile  # instance variable unique to each instance

    def getNumDNSpkts(self):
        return self.numPktsDNS

    def typeDNScounter(self):
        print("Reading DNS pkts %s" % self.pathPCAPFile)
        packets = rdpcap(self.pathPCAPFile)
        for pkt in packets:
            if UDP in pkt and DNSQR in pkt:
                self.numPktsDNS += 1
                #print(pkt.show())
                #dst = pkt[IP].dst
                rec_type = pkt[DNSQR].qtype
                #print(types[rec_type])
        print(self.numPktsDNS)