import mechanize
from bs4 import BeautifulSoup


nav = mechanize.Browser()
nav.set_handle_robots(False)
nav.set_handle_equiv(False)
nav.addheaders = [{'User-Agent','Firefox'}]
nav.open("URL del sitio") #Detecta si el sitio contiene formulario
nav.select_form(nr=0)

#Colocar los campos que aparecen en el formulario
nav['username'] = 'admin' #Campos del formulario
nav.submit()
soup = BeautifulSoup(nav.response().read(),'html5lib')
print(soup.pre.string)
#Una vez colocada la inyeccion devolvera si tiene o no una vulnerabilidad en el sitio
