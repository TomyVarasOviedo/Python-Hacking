from imp import reload
import sys
from shodan import Shodan
key_user = 'xWjoSzQDLMBSVetXYSNAiAirySJFleAn'

motor = Shodan(key_user)
busqueda = input("Busqueda:  ")
try:
    consulta = motor.search(busqueda)
    print("     Resultados: {}".format(consulta['total']) )
    parametros = []
    print("Escribir exit para dejar de agregar para metros")
    parametrosInput = ''
    while str(parametrosInput) != 'exit':
        parametrosInput = str(input("Parametros: "))
        if parametrosInput != 'exit':
            parametros.append(parametrosInput)
    print(parametros)
    numb = 0
    for host in consulta['matches']:
        for i in parametros:
            if i == 'location':
                print('LOCATION: ')
                for l in host['location']:
                    print(f'     {l.upper()}: ' + str(host['location'][l]))
            else:
                print(f'''{i.upper()}: {str(host[i])}''')
            numb = numb+1
            print('//--------------//' if numb % len(parametros) == 0 else '')
        
except KeyboardInterrupt:
    print("Ocurrio un error")

