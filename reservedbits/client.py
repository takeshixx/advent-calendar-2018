#!/usr/bin/env python3
import sys
import socket
import random

from scapy.all import sr1, TCP, IP


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} host port interface'.format(sys.argv[0]))
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    interface = sys.argv[3]
    # RSTs to this port must be blocked
    #sport = random.randint(1024,65535)
    sport = 49113
    ip = IP(dst=host)
    syn = TCP(sport=sport, dport=port, reserved=15, flags='S', seq=1000)
    synack = sr1(ip / syn, iface=interface)
    ack = TCP(sport=sport, dport=port, reserved=15, flags='A', seq=synack.ack, ack=synack.seq + 1)
    resp = sr1(ip / ack, iface=interface)
    if resp:
        print(resp.show2())
    else:
        print('no response')
