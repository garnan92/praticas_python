def main():
    while True:
        valor1 = input("valor 1: ")
        if valor1 == "exit":
            break
        valor2 = input("valor 2: ")

        operdador = input("suma +\nresta -\nmultiplicacion *\ndivision /\nmodulo %\ntipo de operador: ")

        finale = 0

        if operdador == "+":
            finale = int(valor1) + int(valor2)
        elif operdador == "-":
            finale = int(valor1) - int(valor2)
        elif operdador == "*":
            finale = int(valor1) * int(valor2)
        elif operdador == "/":
            finale = int(valor1) / int(valor2)
        elif operdador == "%":
            finale = int(valor1) ** int(valor2)
        else:
            print("operador no disponible")
            continue

        text = "{0} {1} {2} = {3}"

        print(text.format(valor1,operdador,valor2,finale))


main()