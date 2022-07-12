#--GLOSARIO--#
'''
    (dnsPython) : libreria para solitar informacion a DNS o paginas web
    (DNS) : Sistema de nombre de dominio, se usa para no usar la ip remota
    (dns.resolver.query) : funcion que realiza peticion al servidor de la pagina para obetener informacion, se pasa como parametros, la pagina y el tipo de peticion que se encuentra detallado en un sitio de IBM
'''
#--GLOSARIO--#
import dns.resolver

def main():
    tipoPeticion = ['A', #Direccion del host#
                    'AAAA', #Direccion IPv6
                    'NS' ,#Servidor de nombre de autorizacion#
                    'CNAME', #Nombre canocico para un alias#
                    'HINFO', #Informacion del host#
                    'TXT', #Cadenas de caracteres de texto#
                    'ANY' #Todos los registros#
                    ]
    try:
        peticion = dns.resolver.query('google.com', tipoPeticion[1])
        for p in peticion:
            print(p)
    except:
        print('No se pudo realizar o no hay respuesta')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
