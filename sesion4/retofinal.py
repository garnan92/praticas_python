class Mercado:
    def __init__(self,nombre:str="",precio:float=0.0,cantidad=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return "{0} precio unitario ${1}  cantidad {2} precio total por producto ${3}".format(self.nombre,self.precio,self.cantidad,(self.cantidad*self.precio))

class Carrito:

    def __init__(self):
        self.__lista = []

    def agregar(self,objeto:Mercado):
        self.__lista.append(objeto)
    
    def remover(self):
        pass

    def cobrar(self):
        subtotal = 0.0
        for i in self.__lista:
            subtotal += i.precio
            print(i)


def main():
    pass

main()
