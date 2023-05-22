from scapy.all import *

# Replace the values with the appropriate source and destination IP addresses
spoofed_ip = "192.168.1.100"
target_ip = "172.20.242.29"

# Create an IP packet with a spoofed source IP
ip_packet = IP(src=spoofed_ip, dst=target_ip)

# Create a ICMP (ping) packet
icmp_packet = ICMP()

# Combine the IP and ICMP packets
packet = ip_packet / icmp_packet

# Send the spoofed packet
send(packet)
