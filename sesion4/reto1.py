class vehiculo:
    def __init__(self,modelo:str,velocidad:int,llantas:int,color:str,tipo:str=""):
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__llantas = llantas
        self.__color = color
        self.__tipo = tipo
    
    def __str__(self):
        return "el {4} {0} viaja a {1} km, tiene {2} llantas y es de color {3}".format(self.__modelo,self.__velocidad,self.__llantas,self.__color,self.__tipo)

    def __del__(self):
        pass
    
    def avanza(self):
        print( "el {2} {0} avanza a {1} km/h".format(self.__modelo,self.__velocidad,self.__tipo) )

    def getTipo(self):
        return self.__tipo


class avion(vehiculo):

    def __init__(self,modelo:str,velocidad:int,llantas:int,color:str,altura:int):
        super().__init__(modelo,velocidad,llantas,color,"avion")
        self.__altura = altura

    def vuela(self):
        print("el avion puede volar a una altitud de {0} pies".format(self.__altura))

class carro(vehiculo):

    def __init__(self,modelo:str,velocidad:int,llantas:int,color:str,anio:int):
        super().__init__(modelo,velocidad,llantas,color,"carro")
        self.__anio = anio

    def modelaje(self):
        print("el carro es del año {0}".format(self.__anio))

class barco(vehiculo):

    def __init__(self,modelo:str,velocidad:int,llantas:int,color:str,capacidad:int):
        super().__init__(modelo,velocidad,llantas,color,"barco")
        self.__capacidad = capacidad

    def Capacidad(self):
        print("es un barco que puede abarcar {0} personas".format(self.__capacidad))

def main():

    # vehiculos = [ vehiculo("mazda",100,4,"rojo") , vehiculo("nisam",150,3,"azul"),vehiculo("honda",94,2,"blanco") ]

    # vehiculos[0].__modelo = "ford"

    vehiculos = [carro("mazda",100,4,"rojo",2018),avion("boing",750,4,"blanco",3500),barco("jate",45,4,"azul",15)]

    for i in vehiculos:
        print(i)
        i.avanza()
        if i.getTipo() == "avion":
            i.vuela()
        elif i.getTipo() == "carro":
            i.modelaje()
        elif i.getTipo() == "barco":
            i.Capacidad()

main()