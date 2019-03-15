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
        self.objPcapFile = ""
        self.nameFile = ""
#==================  Setter functions  ======================#
    def set_timeWindow(self, interval):
        self.timeWindow = interval

    def set_pathPcap(self, path):
        self.pathPcap = path

    def set_nameFile(self):
        self.nameFile = os.path.basename(self.pathPcap)

    def set_objPcapFile(self):
        self.objPcapFile = pyshark.FileCapture(self.get_pathPcap(), only_summaries=False)

#==================  Getter functions  ======================#
    def get_timeWindow(self):
        return self.timeWindow

    def get_pathPcap(self):
        return self.pathPcap

    def get_nameFile(self):
        return self.nameFile

    def get_objPcapFile(self):
        return self.objPcapFile

#==================  Util functions  ======================#
    def get_timeStampPkt(self, num_rowPkt):
        return self.objPcapFile[num_rowPkt].sniff_timestamp
# =========================================================#

        #os.system("editcap -r " + self.get_pathPcap() + " PCAPs/tempPkt.pcap 0 - 1")
        #tempPkt = rdpcap("PCAPs/tempPkt.pcap")
        #for timestamp, buf in tempPkt:
            #print('Timestamp: ', str(datetime.utcfromtimestamp(timestamp)))


             #   print('Timestamp: ', str(datetime.utcfromtimestamp(timestamp)))

#==================  Split functions  ======================#
    def split_pcap(self):
        pktFromTime = self.get_timeStampPkt(0)
        pktToTime = round(float(pktFromTime)) + self.get_timeWindow()
        print(pktFromTime)
        print(pktToTime)
        print(type(pktFromTime))
        #editcap -A "2011-04-14 11:00:00" -B "2011-04-14 13:00:00" infile.cap outfile.cap
        cmdEditcap = 'editcap -A "' + str(datetime.utcfromtimestamp(float(pktFromTime))) + '" -B "' + str(datetime.utcfromtimestamp(float(pktToTime))) + '" '
        inFile = self.get_pathPcap()
        outFile = ' PCAPs/TimeWindowsPCAPs/outTest.pcap'
        cmdEditcap = cmdEditcap + inFile + outFile
        print(cmdEditcap)
        os.system(cmdEditcap)
        exit(0)
# ==================  Read PCAP  ======================#
        #pcapFile = rdpcap(self.get_pathPcap())

#        setRows = range(0, int(len(pcapFile)/self.__sizeOfGroup))


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
