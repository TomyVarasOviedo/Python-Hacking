#!/usr/bin/env python
#_*_coding: utf8 _*_

import nmap as np
def main():
    nmObject = np.PortScanner()
    ip = input("Ip: ") #Objetivo para scanear
    nmObject.scan(hosts=ip, arguments="--top-ports 1000 -sV --version-intensity 3")
    print(f'Comando ejecutado: {nmObject.command_line()}')
    # print(nmObject.scaninfo())
    print(f'Protocolos utilizados: {nmObject[ip].all_protocols()}')
    print(f'Estado de la maquina{nmObject[ip].state()}')
    print(nmObject[ip]['tcp'])
    for puerto in nmObject[ip]['tcp'].keys(): #Recorre y muestra la informacion de los puertos enocntrados
        print(puerto)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()