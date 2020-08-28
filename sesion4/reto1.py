class vehiculo:
    def __init__(self,modelo:str,velocidad:int,llantas:int,color:str):
        self.modelo = modelo
        self.velocidad = velocidad
        self.llantas = llantas
        self.color = color
    
    def __str__(self):
        return "el auto {0} viaja a {1} km, tiene {2} llantas y es de color {3}".format(self.modelo,self.velocidad,self.llantas,self.color)

    def __del__(self):
        pass

    def avanza(self):
        print( "el auto {0} avanza a {1} km/h".format(self.modelo,self.velocidad) )

def main():

    vehiculos = [ vehiculo("mazda",100,4,"rojo") , vehiculo("nisam",150,3,"azul"),vehiculo("honda",94,2,"blanco") ]

    for i in vehiculos:
        print(i)
        print(i.avanza())

main()