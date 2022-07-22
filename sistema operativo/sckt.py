#--GLOSARIO--#
'''
    (socket) : Estructura de datos que permite que dos maquinas con distintos SO, puedan comunicarse entre si
    (socket connect) : funcion de conexion, recibe una tupla con el puerto y el host 
    (socket recv): especifica tamaño de lo que recibe de la conexion para imprimirlo
'''
#--GLOSARIO--#
import socket

s = socket.socket()
sitio = input("Ingresar sitio:  ")
puerto = input("Puerto:  ")
lista = (str(sitio), int(puerto))
try:
    s.connect(lista)
    banner = s.recv(1024)
    print(banner)
except:
    print("*ERROR*")