def main():
    intorducion = input("intorduce un valor: ")
    for i in range(1,11):
        text = "{0} * {1} : {2}"
        print(text.format(intorducion,i,int(intorducion)*i))

main()