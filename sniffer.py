from scapy.all import sniff
from analyzer import analyze_packet

print("[*] Iniciando captura de pacotes... (Ctrl+C para parar)\n")

def packet_handler(packet):
    analyze_packet(packet)

sniff(prn=packet_handler, store=False, count=100)