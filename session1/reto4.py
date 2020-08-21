def sabor(helad):
    text = "{0}. Helado con {1}: ${2}"
    if helad == "oreo":
        return text.format(1,helad,19)
    elif helad == "m&m":
        return text.format(2,helad,25)
    elif helad == "fresas":
        return text.format(3,helad,22)
    elif helad == "brownie":
        return text.format(4,helad,28)
    else:
        return "producto no disponible"

def main():
    helado = input("introducir un sabor de helado: ")
    print(sabor(helado))

main()