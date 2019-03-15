import dpkt
import datetime
import pyshark
from scapy.all import *
import os

'''PEP8 stardard - here description'''

class PacketsTime:

#==================  Constructor  ======================#
    def __init__(self):
        # interval time in minutes - default 15 minutes
        self.timeWindow = (15*60)
        self.pathPcap = "PCAPs/1stExercise.pcap"
        self.__nameFile = ""

#==================  Setter functions  ======================#
    def set_timeWindow(self, interval):
        self.timeWindow = interval

    def set_pathPcap(self, path):
        self.pathPcap = path

    def set_nameFile(self):
        self.__nameFile = os.path.basename(self.pathPcap)

#==================  Getter functions  ======================#
    def get_timeWindow(self):
        return self.timeWindow

    def get_pathPcap(self):
        return self.pathPcap

    def get_nameFile(self):
        return self.__nameFile

    def get_firstPcap(self):
        cap = pyshark.FileCapture(self.get_pathPcap(), only_summaries=True)
        print(cap[0])
        #os.system("editcap -r " + self.get_pathPcap() + " PCAPs/tempPkt.pcap 0 - 1")
        #tempPkt = rdpcap("PCAPs/tempPkt.pcap")
        #for timestamp, buf in tempPkt:
            #print('Timestamp: ', str(datetime.utcfromtimestamp(timestamp)))

        #for timestamp, buf in pcap:
             #   os.system("editcap -A " + str(datetime.utcfromtimestamp(timestamp)) + " -B " + str(datetime.utcfromtimestamp(timestamp+self.get_timeWindow())) + " infile.cap outfile.cap")

             #   print('Timestamp: ', str(datetime.utcfromtimestamp(timestamp)))

#==================  Split functions  ======================#
    def split_pcap(self):
        pktFrom = 0
        pktTo = self.get_timeWindow()
        rangePkts = str(pktFrom)+"-"+str(pktTo)
# ==================  Read PCAP  ======================#
        pcapFile = rdpcap(self.get_pathPcap())

        setRows = range(0, int(len(pcapFile)/self.__sizeOfGroup))

        self.set_nameFile()
# ==================  Splitting Directory  ======================#
        pathFolder = "PCAPs/TimeWindowsPCAPs/" + self.get_nameFile()[0:len(self.get_nameFile())-5]
        try:
            os.mkdir(pathFolder)
        except OSError:
            print("Creation of the directory %s failed" % pathFolder)

        else:
            print("================================================================")
            print("Successfully created the directory %s " % pathFolder)
# ==================  Splitting pcap functions  with tshark module ======================#
            #read the time of the first pkt
            #print('Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp)))
            for count in setRows:
                os.system("editcap -r " + self.get_pathPcap() + " " + pathFolder + "/" + str(count) + "_" + self.get_nameFile() +" "+ rangePkts)
                tmp = pktTo - 1
                pktFrom = pktTo
                pktTo = tmp + self.get_size()
                rangePkts = str(pktFrom)+"-"+str(pktTo)
            print("number of split files %d in %s folder " % ((count+1), pathFolder))
            print("================================================================")
