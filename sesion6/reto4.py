import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",help="nombre del archivo")
parser.add_argument("-n","--number",help="linea solicitada")
args = parser.parse_args()

if args.number:
    linea = int(args.number)

if args.file:
    filler = args.file

if args.number and args.file:
    lineas = 0
    with open(filler,"r") as archivo:
        for i in archivo:
            if lineas == linea:
                print(i)
            lineas += 1

