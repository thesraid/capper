import scapy.all as scapy

arptable = {}

class scan:
    def Arp(self, ip):
        self.ip = ip
        print(ip)
        arp_r = scapy.ARP(pdst=ip)
        br = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        request = br/arp_r
        answered, unanswered = scapy.srp(request, timeout=1)
        print('\tIP\t\tMAC')
        print('_' * 37)
        for i in answered:
            ip, mac = i[1].psrc, i[1].hwsrc
            print(ip,mac)
            print('-' * 37)
            arptable[ip] = mac

arp = scan() # create an instance of the class
arp.Arp('192.168.0.1/24') # call the method

print (arptable)

