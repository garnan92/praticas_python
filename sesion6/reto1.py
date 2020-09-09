import json 

def main():

    with open("autos.txt","w") as archivo:
        archivo.write( "[" )
        while 1:

            modelo =str(input("modelo del auto: "))
            anio = str(input("de que año es: ")) 
            marca=str(input("de que consesionaria es: "))
            color=str(input("de que color es: "))

            auto = {
                "modelo" : modelo,
                "anio" : anio,
                "marca" : marca,
                "color" : color
            }

            archivo.write( json.dumps(auto) )

            pregunta = input("quieres introducir otro numero 'y' para si 'n' para no: ")

            if pregunta == "n" :
                break

            archivo.write( "," )
            
        archivo.write( "]" )


main()