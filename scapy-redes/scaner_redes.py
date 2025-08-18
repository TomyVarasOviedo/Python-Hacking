from scapy.all import ARP, Ether, srp
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-r",
    "--range",
)

args = parser.parse_args()


def ip_scan(ip):
    range_ip = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    final_packet = broadcast / range_ip
    rest = srp(final_packet, timeout=2, verbose=False)
    for i in rest:
        print(f"HOST: {i[1].psrc} - MAC: {i[1].hwsrc}")


def main():
    if args.range != "":
        ip_scan(args.range)
    else:
        print("Please provide an IP range using the -r option.")
        return


if __name__ == "__main__":
    pass
