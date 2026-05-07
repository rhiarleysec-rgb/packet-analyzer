from scapy.all import IP, TCP, UDP, DNS, DNSQR
from collections import defaultdict
from report import save_log

port_scan_tracker = defaultdict(set)
log = []

def analyze_packet(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        proto = "TCP" if TCP in packet else "UDP" if UDP in packet else "OTHER"

        entry = f"[{proto}] {src} -> {dst}"

        if TCP in packet:
            port = packet[TCP].dport
            port_scan_tracker[src].add(port)
            if len(port_scan_tracker[src]) > 10:
                entry += f"  [ALERTA] POSSIVEL PORT SCAN ({len(port_scan_tracker[src])} portas)"

        if DNS in packet and packet[DNS].qr == 0:
            query = packet[DNSQR].qname.decode()
            entry += f"  [DNS] {query}"

        print(entry)
        log.append(entry)
        save_log(log)