import argparse
import csv


parser = argparse.ArgumentParser()
parser.add_argument("-fi","--file_in",help="nombre del archivo de entrada")
parser.add_argument("-fo","--file_out",help="nombre del archivo de salida")
args = parser.parse_args()


if args.file_in and args.file_out:

    campos = ["nombre","edad","ciudad"]
    lista = []
    with open(args.file_in,"r") as archivo:
        reader = csv.DictReader(archivo,fieldnames=campos)
        for row in reader:
            print(row)
            lista.append( "Nombre = {0}, Edad = {1}, Ciudad = {2}\n".format(row["nombre"],row["edad"],row["ciudad"]) )

    with open(args.file_out,"w") as archivo:
        for dato in lista:
            print(dato)
            archivo.write(dato)
