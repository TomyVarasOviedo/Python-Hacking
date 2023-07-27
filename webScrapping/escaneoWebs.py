from urllib import request

def main():
    web = open('index.html', "w+")
    consulta = request.urlopen("https://lorem2.com/")
    consulta = consulta.read().decode('utf8')
    web.write(consulta)
    web.close()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()