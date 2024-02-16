import re
from urllib import request

def findAll():
    pagina = open("index.hmtml","r")
    for i in pagina,readlines():
        """
        Expresiones regulares:
            ^: indica que la busqueda debe empezar con el caracter de delante
            $: inidica que la busqueda debe terminar en el caracter de detras
            .*: indica que la busqueda devolvera lo que esta entre los dos caracteres
            .: Hace referencia todos los caracteres de delante
            *: Indica que algo se va a repetir un n cantidad de veces
            (): Establecen prioridad sobre que texto mostrar
            +: indica que la cantidad de elementos debe ser mayor a cero
        """
        busqueda = re.findall('<li>.*</li>',i)
        if busqueda:
            print(busqueda)
def search():
    pagina = open('index.html', 'r')
    for i in pagina.readlines():
        #1ºParametro: Lo que se va a buscar
        #2ºParametro: Donde se va buscar
        busqueda = re.search('lorem', i)
        if busqueda:
            print(i)
        else:
            pass
def get_li():
    code = request.urlopen('https://lorem2.com/')
    code = code.read().decode('utf8')
    todo = re.findall('<li>(.+?)</li>', code)
    for i in todo:
        if not '<a href=' in i:
            print(i+"\n")
def main():
    get_li()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

