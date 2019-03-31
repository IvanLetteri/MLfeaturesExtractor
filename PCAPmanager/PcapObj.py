from PCAPmanager import PacketObj
class PcapObj:
# ==================  Constructor  ======================#
    def __init__(self):
        self.numOfPkts = 0
        self.pathPcap = ""
        self.nameFilePcap = ""
        self.startingTime = ""
        self.endingTime = ""
        self.listOfPkts = []

#==================  Setter functions  ======================#
    def set_lengthPcap(self, lengthPcap):
        self.lengthPcap = lengthPcap

    def set_nameFilePcap(self, nameFilePcap):
        self.nameFilePcap = nameFilePcap

    def set_size(self, nameFilePcap):
        self.nameFilePcap = nameFilePcap

    def set_startingTime(self, startingTime):
        self.startingTime = startingTime

    def set_endingTime(self, endingTime):
        self.endingTime = endingTime

#==================  Getter functions  ======================#
    def get_lengthPcap(self):
        return self.lengthPcap


    def get_nameFilePcap(self):
        return self.nameFilePcap


    def get_size(self):
        return self.nameFilePcap


    def get_startingTime(self):
        return self.startingTime


    def get_endingTime(self):
        return self.endingTime
