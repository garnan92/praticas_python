class EntradaInvalidaException(Exception):
    pass


def Promedio(numeros:[int]):
    size = len(numeros)
    suma = 0

    for i in numeros:
        suma += i

    print(suma/size)



def main():

    print("entrada de numeros")

    numeros = list()

    while 1:
        try:

            num = input("introduce un numero: ")

            numeros.append(int(num))

            pregunta = input("quieres introducir otro numero 'y' para si 'n' para no: ")

            if pregunta != "y" and pregunta != "n":
                raise EntradaInvalidaException("no es una entrada valida de pregunta")
            elif pregunta == "n" :
                Promedio(numeros)
                break

        except EntradaInvalidaException:
            
            print("penalizacion numero borrado")
            numeros.pop()

        except ValueError:
            
            print("no es un numero tiene que ser un numero")



main()
