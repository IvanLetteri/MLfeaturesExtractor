from dpkt.tcp import TCP
from scapy.all import *

'''PEP8 stardard - here description'''

class PacketsGroup:
    sizeOfGroup = 10
    pathPcap = ""
#==================  Constructor  ======================#
    def __init__(self):
        self.__sizeOfGroup = 10

#==================  Setter functions  ======================#
    def set_size(self, size):
        self.__sizeOfGroup = size

    def set_pathPcap(self, path):
        self.__pathPcap = path

#==================  Getter functions  ======================#
    def get_size(self):
        return self.__sizeOfGroup

    def get_pathPcap(self):
        return self.__pathPcap

#==================  Getter functions  ======================#
    def read_pcap(self, pathPcap):
        self.__pathPcap = pathPcap

    def split_pcap(self):
        size = range(0, self.get_size())
        for count in size:
            print("Reading TCP pkts %s" % self.pathPCAPFile)
            packets = rdpcap(self.pathPCAPFile)
            print(count)