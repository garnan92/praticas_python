def mcm(lista) -> int:

    i = 1

    inter = 0

    set1 = set()
    set2 = set()
    set3 = set()

    set1_2 = set()

    set1_2_3 = set()

    while 1:
        set1.add(i*lista[0])
        set2.add(i*lista[1])
        set3.add(i*lista[2])
        i += 1

        set1_2 = set1.intersection(set2)

        set1_2_3 = set1_2.intersection(set3)

        inter = len (set1_2_3)

        if inter > 0:
            break

    listafinale = list(set1_2_3)

    print(listafinale)
    


def main():
    lista = [3,4,5]
    mcm(lista)

main()