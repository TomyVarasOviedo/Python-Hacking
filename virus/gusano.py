import shutil
import sys
#--GLOSARIO--#
'''
    (sys.argv()) : convierte los elementos que se pasa por consola en una lista
    (shutil.copy()) : funcion que replica un archivo, pasando como paramentro el archivo que se va a copiar y la ruta
'''
#--GLOSARIO--#
def main():
    if len(sys.argv) == 2:
        for x in range(0, int(sys.argv[1])):
            shutil.copy(sys.argv[0], sys.argv[0]+str(x)+'.py')
    else:
        print('algo salio mal')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()        