from Utils.layer4.TCPpacket import TCPpacket
from Utils.layer4.UDPpacket import UDPpacket
from Utils.layer5.DNSpacket import DNSpacket
#from Utils.layer3.ICMPpacket import ICMPpacket
#from Utils.ReadWriteFile.WriteCSV import WriteCSV

import sys

def main():
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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nExit\n')
        sys.exit()
    except SystemExit:
        pass