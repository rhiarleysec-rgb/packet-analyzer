# Packet Analyzer

Ferramenta de análise de tráfego de rede em tempo real desenvolvida em Python.
Captura pacotes TCP/UDP, monitora requisições DNS e detecta possíveis port scans,
gerando um relatório visual em HTML.

---

## Funcionalidades

- Captura pacotes TCP e UDP em tempo real
- Identifica IPs de origem e destino
- Monitora requisições DNS
- Detecta possíveis Port Scans
- Gera relatório visual automático em HTML

---

## Tecnologias

- Python 3
- Scapy
- Npcap (Windows)
- HTML

---

## Como rodar

### Requisitos
- Python 3.8+
- Npcap instalado (Windows): https://npcap.com/#download
  - Marcar: "Install Npcap in WinPcap API-compatible Mode"

### Instalação
pip install scapy

### Execução (como Administrador)
python sniffer.py

### Relatório
Após a execução, abra o arquivo report.html no navegador.

---

## Estrutura

packet-analyzer/
├── sniffer.py      # Captura os pacotes em tempo real
├── analyzer.py     # Classifica protocolo e detecta ameaças
├── report.py       # Gera relatório visual em HTML
└── report.html     # Dashboard gerado automaticamente

---

## O que foi detectado na captura

| Protocolo | Servidor | Identificado como |
|---|---|---|
| TCP | 140.82.112.26 | GitHub |
| TCP | 64.233.190.188 | Google |
| TCP | 52.97.12.114 | Microsoft |
| UDP | 160.79.104.10 | Meta/WhatsApp |
| DNS | browser-intake-us5-datadoghq.com | Ferramenta de monitoramento |

---

## Autor

Rhiarley — projeto desenvolvido para portfólio de Cybersegurança. 
