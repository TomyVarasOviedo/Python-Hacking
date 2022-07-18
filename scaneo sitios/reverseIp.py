import requests
from bs4 import BeautifulSoup

def main():
    sitio = 'www.cloudflare.com'
    agent = {'User-Agent':'Firefox'}
    peticion = requests.get('https://viewdns.info/reverseip/?host={}&t=1'.format(sitio), headers=agent)
    b = BeautifulSoup(peticion.text, 'html5lib')
    tablaId = b.find(id="null")
    tabla = tablaId.find(border="1")
    for fila in tabla.find_all("tr"):
        print("Sitios: "+ fila.td.string)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()