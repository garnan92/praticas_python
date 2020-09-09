def imprenta_de_numeros(funcion):
    def operador(args:[int]):
        
        funcion(args)

        print ("la lista de reversa")

        args.reverse()

        funcion(args)

        print("remuevo el ultimo elemento de la lista")

        args.reverse()
        args.remove(len(args))

        funcion(args)


        return args

    return operador


@imprenta_de_numeros
def lista(numeros:[int]):
    print("la lista de numeros es")
    print(numeros)



lista([1,2,3,4])