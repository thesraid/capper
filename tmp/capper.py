#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# joriordan@alienvault.com
# 2017 - 01 - 03
#
# Dependencies: apt install tcpreplay tcpdump scapy
#
#
# A script to take a pcap file, replace an IP with another IP and replay it over the network
#
# Usage:
#       Put a PCAP file in the pcap directory (From http://malware-traffic-analysis.net/ for example)
#       Duplicate one of the lines at the bottom of this script and point it to your pcap
#       Replace the IP at the end of the line with the IP in your pcap you want to subsitute for the local IP
#       By default the local IP will be 192.168.250.13 unless changed at run time.
#
#   Your PCAP                           Local IP variable       The IP in the PCAP you want to replace
#   inject("pcaps/mail-cc.pcap",        ip,                     "192.168.56.103")


from scapy.all import *
import commands
import socket
import ast


with open("ips.txt", "r") as data:
   #print (data)
   dictionary = ast.literal_eval(data.read())

if len(sys.argv) == 2:
        if sys.argv[1] == "--help":
                print " "
                print "Default usage: capper.py"
                sys.exit()
        ip = sys.argv[1]

def inject(fname):
        packets=rdpcap(fname)
        p2 = []
        #for p in packets:
        #        if p.haslayer("IP"):
        #                if p[IP].src == template:
        #                        p[IP].src = target
        #                if p[IP].dst == template:
        #                        p[IP].dst = target
        for p in packets:
                if p.haslayer("IP"):
                        if p[IP].src in dictionary:
                                p[IP].src = dictionary[p[IP].src]
                        if p[IP].dst in dictionary:
                                p[IP].dst = dictionary[p[IP].dst]
                if len(p) > 1480:
                        p3 = fragment(p, fragsize=1480)
                        for pp in p3:
                                p2.append(pp)
                else:
                        p2.append(p)

        wrpcap("/tmp/tmp.pcap", p2)
        (_, msg) = commands.getstatusoutput("tcpreplay -t -i enx9cebe8299368 /tmp/tmp.pcap")
        print msg


print " "
print " "
print " "

# From here you can add new pcaps
# Use Wireshark to find the IP you want to replace with the local IP
# Enter that IP at the end of each of these functions

inject("home.pcap")
