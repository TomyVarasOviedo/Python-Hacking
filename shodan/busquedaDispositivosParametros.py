from imp import reload
import sys
from shodan import Shodan
import argparse

reload(sys)
#sys.setdefaultencoing('utf8')
key_user = 'xWjoSzQDLMBSVetXYSNAiAirySJFleAn'
parse = argparse.ArgumentParser()
parse.add_argument('-q', '--query', help="Busqueda")
parse.add_argument('-a', '--api', help="Tu api")
parse = parse.parse_args()
def main():
    if parse.query != '':
        if parse.api != '':
            api = Shodan(parse.api)
            try:
                b = api.search(parse.query)
                print(f"Total de objetivos: {b['total']}")
                for i in b['matches']:
                    print(f'Objetivos encontrados: {i["ip_str"]}')
            except :
                print("Error en la consulta")
        else:
            print("Introduzca su api key")
    else:
      print("Introduzca algun carater de busqueda")
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
