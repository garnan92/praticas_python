def operadorOr(a,b):
    print ( "el operador or es: ",bool(a) or bool(b))

def modulo(a,b):
    print ( "el modulo es: ",int(a)%int(b))

def resta(a,b):
    print ( "la resta es: ",int(a)-int(b))

def main():
    a = input("introducir primer valor: ")
    b = input("introducir segundo valor: ")
    resta(a,b)
    modulo(a,b)
    c = input("introducir true o false 1 ")
    d = input("introducir true o false 2 ")
    operadorOr(c,d)

main()