import requests

def main():
    word = input()
    url = requests.get('https://www.{}.com/es-es/'.format(word))
    cabeceras = dict(url.headers)
    verificacion = False
    for c in cabeceras:
        if word in cabeceras[c].lower():
            verificacion = True
            break
    print("Hay cloudflare" if (verificacion == True) else "No hay cloudflare")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()