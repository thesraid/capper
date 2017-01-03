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

ip = "192.168.250.13"

if len(sys.argv) == 2:
        if sys.argv[1] == "--help":
                print " "
                print " "
                print "Default usage: capper.py"
                print "Uses the IP default address"
                print " "
                print " "
                print "Custom IP usage: capper.py <IP>"
                print "Uses the specified IP "
                print " "
                print " "
                print "Adding new PCAPS: "
                print " Put a PCAP file in the pcap directory"
                print " Duplicate one of the lines at the bottom of this script and point it to your pcap"
                print " Replace the IP at the end of the line with the IP in your pcap you want to subsitute for the local IP"
                print "    "
                print "   Your PCAP                             Local IP variable       The IP in the PCAP you want to replace"
                print "   inject(\"pcaps/mail-cc.pcap\",        ip,                     \"192.168.56.103\")"
                print "    "
                print "    "
                sys.exit()
        ip = sys.argv[1]

def inject(fname, target, template):
        packets=rdpcap(fname)
        p2 = []
        for p in packets:
                if p.haslayer("IP"):
                        if p[IP].src == template:
                                p[IP].src = target
                        if p[IP].dst == template:
                                p[IP].dst = target
                if len(p) > 1480:
                        p3 = fragment(p, fragsize=1480)
                        for pp in p3:
                                p2.append(pp)
                else:
                        p2.append(p)

        wrpcap("/tmp/tmp.pcap", p2)
        (_, msg) = commands.getstatusoutput("tcpreplay -t -i eth0 /tmp/tmp.pcap")
        print msg


print " "
print " "
print " "
print "Using IP: " + ip
print " "
print " "
print " "

# From here you can add new pcaps
# Use Wireshark to find the IP you want to replace with the local IP
# Enter that IP at the end of each of these functions

inject("pcaps/xtrat.pcap", ip, "192.168.56.101")
inject("pcaps/mail-cc.pcap", ip, "192.168.56.103")
inject("pcaps/2014-04-14-Magnitude-EK-traffic.pcap", ip, "192.168.204.226")
inject("pcaps/heart2.pcap", ip, "98.138.253.109")
inject("pcaps/2014-03-29-FlashPack-EK-traffic.pcap", ip, "172.16.2.156")
inject("pcaps/14aa553c7a3eace5d7940c6e305133b6_20140330.pcap", ip, "192.168.86.10")
inject("pcaps/krol.pcap", ip, "192.168.56.103")
inject("pcaps/2014-04-24-fake-flash-updater.pcap", ip, "172.16.223.131")
inject("pcaps/2014-03-28-Fiesta-EK-traffic.pcap", ip, "192.168.204.193")
inject("pcaps/sality.pcap", ip, "192.168.56.102")
inject("pcaps/20140320.pcap", ip, "192.168.18.10")
inject("pcaps/yoyo.pcap", ip, "192.168.56.104")
inject("pcaps/2014-05-03-fake-Flash-updater-traffic.pcap", ip, "192.168.204.223")
inject("pcaps/2014-05-03-fake-Flash-player-sandbox-analysis.pcap", ip, "192.168.204.223")
inject("pcaps/nikto2.pcap", ip, "192.168.1.222")
inject("pcaps/sqlmap2.pcap", ip, "192.168.1.223")
inject("pcaps/a80e570d4d6ad39afc02877e6eb3431f.pcap", ip, "192.168.1.110")
inject("pcaps/bffed17758cd47caea11cf4766f21b991a96e4ad468f7e00c18c03b8f9028f5c.pcap", ip, "10.0.2.15")
