#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse
import os

def banner():
    os.system ("cls")

    print(chr(27)+"[1;31m"+"░█████╗░██╗░░░██╗░█████╗░██╗░░██╗██╗██╗░░░░░██╗░░░░░░█████╗░")
    print(chr(27)+"[1;31m"+"██╔══██╗██║░░░██║██╔══██╗██║░░██║██║██║░░░░░██║░░░░░██╔══██╗")
    print(chr(27)+"[1;31m"+"██║░░╚═╝██║░░░██║██║░░╚═╝███████║██║██║░░░░░██║░░░░░██║░░██║")
    print(chr(27)+"[1;31m"+"██║░░██╗██║░░░██║██║░░██╗██╔══██║██║██║░░░░░██║░░░░░██║░░██║")
    print(chr(27)+"[1;31m"+"╚█████╔╝╚██████╔╝╚█████╔╝██║░░██║██║███████╗███████╗╚█████╔╝")
    print(chr(27)+"[1;31m"+"░╚════╝░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝░╚════╝░")
    print()
    print()
    print(chr(27)+"[1;37m"+"Scanner de cabeceras web")
    print()

parser = argparse.ArgumentParser(description=banner())
parser.add_argument('-w','--web',help="Indica la página web")
parser = parser.parse_args()

def main():
    if parser.web:
        try:
            url = requests.get(url=parser.web)
            cabeceras = dict(url.headers)
            for x in cabeceras:
                print(x,' : ', cabeceras[x])
        except:
            print("ERROR: No me he podido acceder :c")
    else:
        print("Indica alguna página web :v")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")
        exit()