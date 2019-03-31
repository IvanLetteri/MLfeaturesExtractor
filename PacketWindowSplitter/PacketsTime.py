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
        self.startPcapTime = ""
        self.endPcapTime = ""
        self.pcapLength = 0

#==================  Setter functions  ======================#
    def set_timeWindow(self, interval):
        self.timeWindow = interval

    def set_pathPcap(self, path):
        self.pathPcap = path

    def set_nameFile(self):
        self.nameFile = os.path.basename(self.pathPcap)
# read the pcap file
    def set_objPcapFile(self):
        self.objPcapFile = pyshark.FileCapture(self.get_pathPcap(), only_summaries=False)

    def set_startPcapTime(self):
        self.endPcapTime = round(float(self.get_timeStampPkt(0)))

    def set_endPcapTime(self):
        self.endPcapTime = round(float(self.get_timeStampPkt(self.get_PcapLength())))

    def set_pcapLenght(self):
        self.pcapLenght = len(self.objPcapFile)

#==================  Getter functions  ======================#
    def get_PcapLength(self):
        return len(self.objPcapFile)

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
    #generate the command string
    def cmdEditcap(self, pktFromTime, pktToTime, outputFile, part):
        #ex. ->  editcap -A "2011-04-14 11:00:00" -B "2011-04-14 13:00:00" infile.cap outfile.cap
        fromTime = str(datetime.utcfromtimestamp(float(pktFromTime)))
        toTime = str(datetime.utcfromtimestamp(float(pktToTime)))
        cmdPart1 =  'editcap -A "' + fromTime + '" -B "' + toTime + '" '
        cmd = cmdPart1 + self.get_pathPcap() + " " + outputFile + 'Part'+ str(part) +'.pcap'
        print("|=======================================   Splitting time command   ================================================|")
        print(cmd)
        print("|===================================================================================================================|")
        return cmd

    def execEditcap(self, cmd):
        os.system(cmd)

#==================  Split functions  ======================#
    def split_pcap(self):
        #read the timestamp of the first packet
        pktFromTime = round(float(self.get_timeStampPkt(0)))
        print(self.get_PcapLength())
        #computes the delta time
        pktToTime = pktFromTime + round(self.get_timeWindow())

        self.set_nameFile()
        # ==================  Splitting PcapTimeWindow Directory  ======================#
        nameFile = self.get_nameFile()[0:len(self.get_nameFile()) - 5]
        pathFolder = "PCAPs/TimeWindowsPCAPs/" + nameFile
        try:
            os.mkdir(pathFolder)
            print("================================================================")
            print("Successfully created the directory %s " % pathFolder)
            # ==================  Splitting pcap functions  with tshark module ======================#

            # for count in setRows:
            self.execEditcap(self.cmdEditcap(pktFromTime, pktToTime, pathFolder+'/'+nameFile, 1))

            exit(0)

        except OSError:
            print("Creation of the directory %s failed" % pathFolder)


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
