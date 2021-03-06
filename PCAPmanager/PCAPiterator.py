import glob
import errno

from PacketWindowSplitter.PacketsGroup import PacketsGroup

class PCAPiterator:

# ==================  Constructor  ======================#
    def __init__(self):
        self.folderPCAPs = "PCAPs/*.pcap"

#==================  Setter functions  ======================#
    def set_folderPCAPs(self, folder):
        self.folderPCAPs = folder + "/*.pcap"

#==================  Getter functions  ======================#
    def get_folderPCAPs(self):
        return self.folderPCAPs

# ==================  Iterator  ======================#
    def iteratePCAPs(self, split_size):
        files = glob.glob(self.get_folderPCAPs())
        for name in files:
            try:
                pktGroup = PacketsGroup()
                pktGroup.set_pathPcap(name)
                pktGroup.set_size(split_size)
                pktGroup.split_pcap()
            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise