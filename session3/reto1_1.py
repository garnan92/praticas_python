def numericos(operacion,*numeros):
    result = 0
    a = 0
    for i in numeros:
        if operacion == "+":
            result += i
        elif operacion == "*":
            if a == 0 :
                result = 1
                a += 1
            result *= i
    print("el resultado es: ",result)


def main():
    numericos("+",1,2,3,5,10)

    numericos("*",5,4)

main()