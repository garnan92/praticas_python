import csv


with open("ejemplo.csv","w") as archivo:
    write = csv.writer(archivo)

    write.writerow(["nombre","Apellido"])
    write.writerow(["ricardo","pacheco"])


campos = ("nombre","apellido")
with open("ejemplo2.csv","w") as archivo:

    write = csv.DictWriter(archivo,fieldnames=campos)

    write.writerow({"nombre":"ricardo","apellido":"pacheco"})

with open("ejemplo2.csv","r") as archivo:
    reader = csv.DictReader(archivo,fieldnames=campos)
    for row in reader:
        print(row)


