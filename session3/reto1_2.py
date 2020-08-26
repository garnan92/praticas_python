def agenda(**personas):
    personas_tmp = dict()
    for i in sorted(personas):
        personas_tmp[i] = personas[i] 
    print(personas_tmp)


def main():

    agenda(wham="45458974578945",ricardo="12871237819",zack="189789273",armando="1782937193",benito="390478203748",jojo="89675609",mary="893791278389")

main()