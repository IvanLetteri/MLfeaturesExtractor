from dpkt.tcp import TCP
from scapy.all import *
import os

'''PEP8 stardard - here description'''

class PacketsGroup:

#==================  Constructor  ======================#
    def __init__(self):
        self.__sizeOfGroup = 10
        self.__pathPcap = "PCAPs/default.pcap"
        self.__nameFile = ""

#==================  Setter functions  ======================#
    def set_size(self, size):
        self.__sizeOfGroup = size

    def set_pathPcap(self, path):
        self.__pathPcap = path

    def set_nameFile(self):
        self.__nameFile = os.path.basename(self.__pathPcap)

#==================  Getter functions  ======================#
    def get_size(self):
        return self.__sizeOfGroup

    def get_pathPcap(self):
        return self.__pathPcap

    def get_nameFile(self):
        return self.__nameFile

#==================  Split functions  ======================#
    def split_pcap(self):
        pktFrom = 0
        pktTo = self.get_size()
        rangePkts = str(pktFrom)+"-"+str(pktTo)
# ==================  Read PCAP  ======================#
        pcapFile = rdpcap(self.get_pathPcap())

        setRows = range(0, int(len(pcapFile)/self.__sizeOfGroup))

        self.set_nameFile()
# ==================  Splitting Directory  ======================#
        pathFolder = "PCAPs/" + self.get_nameFile()[0:len(self.get_nameFile())-5]
        try:
            os.mkdir(pathFolder)
        except OSError:
            print("Creation of the directory %s failed" % pathFolder)

        else:
            print("Successfully created the directory %s " % pathFolder)
# ==================  Splitting pcap functions  with tshark module ======================#
            for count in setRows:
                os.system("editcap -r " + self.get_pathPcap() + " " + pathFolder + "/" + str(count) + "_" + self.get_nameFile() +" "+ rangePkts)
                tmp = pktTo - 1
                pktFrom = pktTo
                pktTo = tmp + self.get_size()
                rangePkts = str(pktFrom)+"-"+str(pktTo)
