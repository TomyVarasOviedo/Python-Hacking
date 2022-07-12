import requests
from bs4 import BeautifulSoup


def main():
    # try:
    peticion = requests.get('https://who.is/whois/reldsec.org')
    codigo = BeautifulSoup(peticion.text, 'html5lib')
    for info in codigo.find_all('pre'):
        print(info.get_text())
    # except:
    #     print('No se pudo realizar la consulta')
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()