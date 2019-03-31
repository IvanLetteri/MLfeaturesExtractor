from Utils.layer4.TCPpacket import TCPpacket
from Utils.layer4.UDPpacket import UDPpacket
from Utils.layer5.DNSpacket import DNSpacket

#from Utils.layer3.ICMPpacket import ICMPpacket
#from Utils.ReadWriteFile.WriteCSV import WriteCSV

from PacketWindowSplitter.PacketsGroup import PacketsGroup
from PCAPmanager.PCAPiterator import PCAPiterator
from PacketWindowSplitter.PacketsTime import PacketsTime

import sys

def main():

    '''
    pkts4pcap_split = 300
    pcapsIterator = PCAPiterator()
    pcapsIterator.set_folderPCAPs("PCAPs")
    pcapsIterator.iteratePCAPs(pkts4pcap_split)
    '''
    test = PacketsTime()
    test.set_timeWindow(15*60)
    test.set_objPcapFile()
    test.split_pcap()
    #pktGroup = PacketsGroup()
    #pktGroup.set_size(100)
    #pktGroup.split_pcap()

    #=============================================#
    '''
    pktTcp = TCPpacket()
    pktTcp.flagTCPcounter()

    pktUdp = UDPpacket()
    pktUdp.pktUDPcounter()

    pktDns = DNSpacket()
    pktDns.typeDNScounter()

    #structure of dictionary flag in TCP pkt has:
    #dictflags = {"syn": 0, "fin": 0, "psh": 0, "rst": 0, "urg": 0, "ack": 0}
    print(pktUdp.numPktsUDP)
    print(pktTcp.numPktsTCP)
    print(pktTcp.getDictTCPflags())
    '''

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nExit\n')
        sys.exit()
    except SystemExit:
        pass