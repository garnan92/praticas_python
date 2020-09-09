archivo = open("./ejemplow.txt","w")


archivo.write("linea 1\n")

archivo.writelines(["linea 2\n","linea 3\n","linea 4\n"])

archivo.close()


archivo = open("ejemplow.txt","r")

linea = archivo.readline()

print(linea)

lineas = archivo.readlines()

print(lineas)

archivo.close()

with open("ejemplow.txt","r") as archivo:
    for i in archivo:
        print(i)
