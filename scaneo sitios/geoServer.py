import urllib.request
import json

def main():
    ip = str(input("Ingresa una IP\n"))
    peticion = urllib.request.urlopen("https://ipinfo.io/{}/json".format(ip))
    j = json.loads(peticion.read())
    info = [i for i in j.values() ]

    for dato in info:
        print(dato)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()