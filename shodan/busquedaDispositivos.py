from imp import reload
from imp import reload
import sys
from shodan import Shodan

reload(sys)
#sys.setdefaultencoing('utf8')
key_user = 'xWjoSzQDLMBSVetXYSNAiAirySJFleAn'

motor = Shodan(key_user)
try:
    query = motor.search("struts") #Busca todos los servidores con esa especificacion
    print(f"Total  de resultados: {query['total']}")
    for host in query['matches']:
        print(f'''IP: {host['ip_str']}
                Puerto: {host['port']}
                ORG: {host['org']}''')
        try:
            print(f"ASN: {host['asn']}")
        except:
            pass
        for i in host['location']:
            print(f"{i}: {str(host['location'][i])}")
except:
    print("Ocurrio un error")