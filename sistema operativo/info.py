#!/usr/bin/env python
#--GLOSARIO--#
'''
    (check output): modulo de subprocess, se coloca como argumento el comando y el standar error
    (sisteminfo) : comando que muestra informacion sobre el dispoistivo
    (w+) : modo de escritur y en caso de que no exista que cree el archivo
'''
#--GLOSARIO--#

from subprocess import check_output
import subprocess

proceso = check_output('systeminfo' , stderr=subprocess.STDOUT)

file = open('text.txt', 'w+')
file.write(str(proceso))
print('hecho')
file.close()
