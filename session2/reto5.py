def fibonachi(n:int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)

def main():
    lista = []
    n = int (input("introduce un numero: "))
    
    for i in range(n+1):
        lista.append(fibonachi(i))
    print(lista)

main()

