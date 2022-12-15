from imp import reload
import sys
from shodan import Shodan

reload(sys)
#sys.setdefaultencoing('utf8')
key_user = 'xWjoSzQDLMBSVetXYSNAiAirySJFleAn'

def main():
    motor = Shodan(key_user)
    busqueda = motor.host('123.57.0.34')
    file = open('scaneoServidor.txt', 'a+')
    print(f'''Direccion: {busqueda['ip_str']}
    Cuidad: {busqueda['city']}
    ISP: {busqueda['isp']}
    Org: {busqueda['org']}
    Puertos: {busqueda['ports']}''')

    for data in busqueda['data']:
        llaves = data.keys()
        for i in llaves:
            file.write(str(data[i]))
    file.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()