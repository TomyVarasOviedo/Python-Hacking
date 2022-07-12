#!/usr/bin/env python
import requests
import argparse
parser = argparse.ArgumentParser(description="Detector de cabeceras")
parser.add_argument('-t', '--target', help="Objetivo")
parser = parser.parse_args()

def main():
	if parser.target:
		try:
			url = requests.get(url=parser.target)
			cabeceras = dict(url.headers)
			for i in cabeceras:
				print(i + " : " + cabeceras[i])
		except:
			print("No se pudo")
	else:
		print("No hay objetivo")

if __name__ == '__main__':
	main()
