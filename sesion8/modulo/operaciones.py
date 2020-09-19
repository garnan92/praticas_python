def suma (n1,n2):
    return n1+n2

def promedio(*numeros):
    i = 0
    suma = 0
    for n in numeros:
        suma += n
        i += 1
    return suma / i