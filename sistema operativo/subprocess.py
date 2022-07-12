#!/usr/bin/env python
import os
#import subprocess

#--GLOSARIO Y REFERENCIA--#
''' 
	(os.devnull): un archivo del arbol del SO al cual no se puede acceder {Poso sin fondo}
	(subprocess.call) : llamada al sistema para que ejecute un comando {!!CADA ESPACIO SE SEPARA COMO ELEMENTOS DE UN ARRAY!!}
	(stdout) : salida estandar de la consola, {en este caso es mandada al archivo que usamos como poso sin fondo}
	(stderror) : salida de error estandar, igualmente a un poso sin fondo

'''
#--GLOSARIO Y REFERENCIA--#
# file = open(os.devnull, 'w')
# proceso = subprocess.call(['ping', '1.1.1.1'], stdout=file, stderr=subprocess.STDOUT)
# if proceso == 0:
# 	print("Se ejecuto correctamente")
# else:
# 	print("Algo salio mal maestro")