def agregar(diccionario,nombre,telefono):
    diccionario[nombre] = telefono
    return diccionario

def main():
    diccionario = dict()
    while 1:
        nombre = input("nombre: ")
        if nombre == "exit":
            break
        telefono = input("telefono: ")
        diccionario = agregar(diccionario,nombre,telefono)

        for key,value in diccionario.items():
            print( "nombre: ",key," telefono:",value )


main()                 