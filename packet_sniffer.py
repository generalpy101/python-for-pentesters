from scapy.all import *

def packet_sniffer(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip}  -->  Destination IP: {dst_ip}")

    if packet.haslayer(TCP):
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print(f"Source Port: {src_port}  -->  Destination Port: {dst_port}")

    if packet.haslayer(Raw):
        raw_data = packet[Raw].load
        print(f"Raw Data: {raw_data}")

sniff(filter="tcp", prn=packet_sniffer, store=0)
