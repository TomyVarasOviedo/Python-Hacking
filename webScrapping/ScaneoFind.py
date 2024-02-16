#!usr/bin/env python
#_*_ coding: utf8 _*_

def main():
    web = open('./index.html','r')
    inicio = '<li>'
    final = '</li>'
    for i in web.readlines():
        if inicio in i:
            if not 'a href' in i:
                ini = i.find(inicio)
                ini = ini + len(inicio)
                fin = i.find(final)
                print(i[ini:fin])

if __name__ == '__main__':
    main()
