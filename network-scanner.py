#!/usr/bin/env python
from colorama import init
from termcolor import colored

import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-a", "--arp", dest="optscan", help="fottiti, sei stupido.")

options= parser.parse_args()
optscan = options.optscan
import scapy.all as scapy #rinomino la funzione scapy.all con scapy.



#ANIMEMAZION!1!1!
print("                                   ")
import sys, time
lowerstr = "SCANNING THE NETWORK ԅ(≖‿≖ԅ)"
upperstr = lowerstr.lower()
for x in range(len(lowerstr)):
     s = '\r' + lowerstr[0:x] + upperstr[x] + lowerstr[x+1:] + '\r'
     sys.stdout.write(s)
     sys.stdout.flush()
     time.sleep(0.1)



def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("""
      
    """)
    print(colored(" _________________________________________", "blue"))
    print(colored("|    IP           |     MAC Address       |\n|_________________|_______________________|", "blue",))
    for element in answered_list:
        print(colored("|  " + element[1].psrc + "\t" + "  |" + "    " + element[1].hwsrc + "  |", "blue"))
    print(colored("|_________________|_______________________|", "blue"))
    print("                                       ")
scan(optscan)

