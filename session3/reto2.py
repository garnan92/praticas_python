# factorial mcd y sqrt
from math import factorial
from math import sqrt
from math import gcd as mcd

def main():

    numeros = [5,64,45,10]

    print("el factorial de ",numeros[0]," es ",factorial(numeros[0]))
    print("la raiz cuadrada de ",numeros[1]," es ",sqrt(numeros[1]))
    print("el minimo conmun multiplo de ",numeros[2]," y ",numeros[3]," es ",mcd(numeros[2],numeros[3]))

main()
