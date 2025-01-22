import pynput.keyboard

teclas = []

def tecla(key):
    tecla = convertir(key)
    if tecla == "Key.esc":
        imprimir()
        return False
    elif tecla == "Key.space":
        teclas.append(" ")
    else:
        teclas.append(tecla)

def imprimir():
    print(f"{''.join(teclas)}")

def convertir(key):
    if isinstance(key, pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)

with pynput.keyboard.Listener(on_press=tecla) as listen:
    listen.join()

