import os
#--GLOSARIO--#
#(os.getcwd) : trae la ruta actual de donde se ejecuta en programa
#(os.rwdir) : elimina el archivo que esta en la ruta del proceso y con un nombre como argumento
#(os.chdir) : cambia la ruta durante la ejecucion del programa
#(os.mkdir) : crea una carpeta en la ruta que se le pasa como parametro
#(os.listdir) : lista los archivos y carpetas de la ruta que se le pasa como parametro
#(os.rename) : cambia el nombre de un archivo, recibe: nombre viejo y el nombre nuevo como parametros
#(os.stat) : se usa para mostrar estadisticas de un archivo, como quien lo creo.
#(os.system) : funcion que ejecuta cualquier comando de consola que se pase como parametros
#--GLOSARIO--#

#print("Ruta: {}".format(os.getcwd()))
#os.chdir("C:/Users/Usuario01/Desktop/Hacking Python/archivos")
#print("Ruta Actual: {}".format(os.getcwd()))
#os.mkdir("pruebaOS")
#os.chdir("C:/Users/Usuario01/Desktop/Hacking Python/archivos/pruebaOS")
#print(os.listdir(os.getcwd()))
#os.rename("prueba.txt", "test.txt")
#print(os.stat("test.txt"))
os.system("ping www.google.com")