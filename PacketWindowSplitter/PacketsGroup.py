from dpkt.tcp import TCP
from scapy.all import *
import os

'''PEP8 stardard - here description'''

class PacketsGroup:
    #sizeOfGroup = 10
    #pathPcap = "PCAPs/default.pcap"
#==================  Constructor  ======================#
    def __init__(self):
        self.__sizeOfGroup = 10
        self.__pathPcap = "PCAPs/default.pcap"

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
    def split_pcap(self):
        pktFrom = 0
        pktTo = self.get_size()
        rangePkts = str(pktFrom)+"-"+str(pktTo)
        packets = rdpcap(self.get_pathPcap())

        setRows = range(0, int(len(packets)/self.__sizeOfGroup))
        for count in setRows:
            os.system("editcap -r "+ self.get_pathPcap() +" PCAPs/"+str(count)+".pcap "+rangePkts)
            tmp = pktTo
            pktFrom = pktTo
            pktTo = tmp + self.get_size()
            rangePkts = str(pktFrom)+"-"+str(pktTo)

            #os.system(
         #   "tshark  -T fields -e  data.data -e frame.time -w Eavesdrop_Data.pcap > Eavesdrop_Data.txt -F pcap -c 1000")
        #packets = rdpcap(self.get_pathPcap())
        #size = range(0, self.get_size())
        #for count in size:
            #print(packets[count])
