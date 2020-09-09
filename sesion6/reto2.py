import csv
from enum import Enum
from datetime import datetime

class Equipamiento(Enum):
    BAJO = 1
    MEDIO = 2
    ALTO = 3

def conversion_a_diccionario(**kwargs):
    
    if kwargs['Equipamiento'] is Equipamiento.BAJO:
        kwargs['Equipamiento'] = "bajo"
    elif kwargs['Equipamiento'] is Equipamiento.MEDIO:
        kwargs['Equipamiento'] = "medio"
    elif kwargs['Equipamiento'] is Equipamiento.ALTO:
        kwargs['Equipamiento'] = "alto"

    kwargs['Fecha'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return kwargs


def main():

    campos = ("Modelo","Color","Equipamiento","Fecha")
    with open("ejemplo2.csv","w") as archivo:

        write = csv.DictWriter(archivo,fieldnames=campos)

        write.writerow(conversion_a_diccionario(Modelo=input("modelo del carro "),Color=input("color: "),Equipamiento=input("1 bajo 2 medio 3 alto ")))


main()