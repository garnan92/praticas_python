from stat import S_ISREG, ST_CTIME, ST_MODE, ST_SIZE
import os, sys, time
from datetime import datetime
import json

def obtiene_archivos(d):
    archivos = os.listdir(d)
    archivos = [
        {
            "nombre": a,
            "tamanio": os.path.getsize(os.path.join(d,a)),
            "fecha": os.path.getmtime(os.path.join(d,a)),
        }
        for a in archivos
    ]
    for archivo in archivos:
        fecha = datetime.fromtimestamp(archivo['fecha'])
        archivo['fecha'] = fecha.strftime("%c")
    return archivos

# print(obtiene_archivos(sys.argv[1] if len(sys.argv) == 2 else r'.'))

with open ("fodler.json","w") as archivo:

    lista = dict()

    lista["lista"] = obtiene_archivos(sys.argv[1] if len(sys.argv) == 2 else r'.')

    print(lista)

    json.dump( lista , archivo,  indent=4  )

