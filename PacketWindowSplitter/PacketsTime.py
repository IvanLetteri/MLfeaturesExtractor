import dpkt
import subprocess
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
        max_interv = self.get_endPcapTime() - self.get_startPcapTime()
        if (max_interv < interval):
            print("timewindows set: "+ str(self.get_timeWindow())+"sec.")
            print("Reduce timewindows, time exceded!!!")
            print("max seconds: ", max_interv)
            exit(0)
        else:
            self.timeWindow = interval

    def set_objPcapFile(self):
        self.objPcapFile = pyshark.FileCapture(self.get_pathPcap(), only_summaries=False)
        length = len([packet for packet in self.objPcapFile])

        #os.system("tshark -r " + self.get_pathPcap())
        self.pcapLenght = length

        self.startPcapTime = round(float(self.get_timeStampPkt(0)))
        self.endPcapTime = round(float(self.get_timeStampPkt(length-1)))

    def set_pathPcap(self, path):
        self.pathPcap = path
        self.set_nameFile()
        self.set_objPcapFile()

    def set_nameFile(self):
        self.nameFile = os.path.basename(self.get_pathPcap())
# read the pcap file

#==================  Getter functions  ======================#
    def get_pcapLength(self):
        return self.pcapLenght

    def get_timeWindow(self):
        return self.timeWindow

    def get_pathPcap(self):
        return self.pathPcap

    def get_nameFile(self):
        return self.nameFile

    def get_startPcapTime(self):
        return self.startPcapTime

    def get_endPcapTime(self):
        return self.endPcapTime

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
        try:
            os.system(cmd)
        except OSError:
            print('wrong command does not exist')
            exit(0)

#==================  Split functions  ======================#
    def split_pcap(self):
        #read the timestamp of the first packet
        pktFromTime = round(float(self.get_timeStampPkt(0)))
        #computes the delta time
        pktToTime = pktFromTime + round(self.get_timeWindow())

        # ==================  Splitting PcapTimeWindow Directory  ======================#
        nameFile = self.get_nameFile()[0:len(self.get_nameFile()) - 5]
        pathFolder = "PCAPs/TimeWindowsPCAPs/" + nameFile
        try:
            os.mkdir(pathFolder)
            print("================================================================")
            print("Successfully created the directory %s " % pathFolder)
            # ==================  Splitting pcap functions  with tshark module ======================#
            for count in range(0, 2000):
                if (pktToTime <= self.get_endPcapTime()):
                    self.execEditcap(self.cmdEditcap(pktFromTime, pktToTime, pathFolder + '/' + nameFile, count))

                    pktFromTime = pktToTime
                    # computes the delta time
                    pktToTime = pktFromTime + round(self.get_timeWindow())
                else:
                    print("Time pcap exceded")
                    print("Splitting finished !!!")
                    exit(0)

        except OSError:
            print("Creation of the directory %s failed" % pathFolder)
