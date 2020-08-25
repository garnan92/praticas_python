def imprimirMarco():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def getData(option,deuda = 0,pago = 0,cargo = 0,tasa_decimal = 0.0):
    if option != 6 and option != 7:
        imprimirMarco()
    introduccion = "+Intodusca {0}: "
    if option == 1:
        return input(introduccion.format("su nombre"))
    elif option == 2:
        while 1:
            try:
                intereses = float(input(introduccion.format("intereses de la tarjeta")))/100
                if 0.0 < intereses < 1.0 :
                    return intereses
                else:
                    print("introdusca un numero entre 0 y 100")
            except:
                print("introdusca un numero porfavor")
    elif option == 3:
        while 1:
            try:
                return int(input(introduccion.format("la deuda de la tarjeta en el ultimo mes de corte")))
            except:
                print("introdusca un numero porfavor")
    elif option == 4:
        while 1:
            try:
                pagos = int(input(introduccion.format("monto total de pagos realizados en el ultimo mes")))
                if deuda > pagos:
                    return pagos
                else:
                    print("no se pude realizar un pago mayor a la deuda actual")
            except:
                print("introdusca un numero porfavor")
    elif option == 5:
        while 1:
            try:
                return int(input(introduccion.format("monto total de pagos realizados despues del corte")))
            except:
                print("introdusca un numero porfavor")
    elif option == 6 or option == 7:
        interes_mensual = tasa_decimal/12
        deuda_recalculada = (deuda - pago ) * (1 + interes_mensual)
        n_deuda = (deuda_recalculada + cargo)
        if option == 6:
            return deuda_recalculada
        else:
            return n_deuda

def pagoRecurrente(tarjeta,cantidad=0):
    tarjeta['pagos'] = cantidad
    tarjeta['cargos'] = 0
    while tarjeta['deuda'] > 0:
        if tarjeta['deuda'] < tarjeta['pagos']:
            tarjeta['pagos'] = tarjeta['deuda']
        imprimirResumen(tarjeta)
        tarjeta['deuda'] = getData(7,deuda=tarjeta["deuda"],pago=tarjeta["pagos"],cargo=tarjeta["cargos"])

def imprimirResumen(tarjeta):
    print("+Resumen de la informacion de: ",tarjeta["nombre"])
    print("+tasas de interes de ",tarjeta["tasa"]*100,"%")
    print("+saldo antes del corte: ",tarjeta["deuda"])
    print("+pagos realizados: ",tarjeta["pagos"])
    print("+deuda despues del corte: ",getData(6,deuda=tarjeta["deuda"],pago=tarjeta["pagos"],cargo=tarjeta["cargos"]))
    print("+cargos realizados despues de corte: ",tarjeta["cargos"])
    print("+deuda actual: ",getData(7,deuda=tarjeta["deuda"],pago=tarjeta["pagos"],cargo=tarjeta["cargos"]))

def main():

    tarjetas = []

    while 1:
        tarjeta = dict()
        tarjeta["nombre"] = getData(1)
        tarjeta["tasa"] = getData(2)
        tarjeta["deuda"] = getData(3)
        tarjeta["pagos"] = getData(4,deuda=tarjeta["deuda"])
        tarjeta["cargos"] = getData(5)
        tarjetas.append(tarjeta)
        ex = input("quieres seguir s 'si' o n 'no': ")
        if ex == "n":
            break
    
    for a in tarjetas:
        imprimirMarco()
        imprimirResumen(a)

    imprimirMarco()
    pagoRecurrente(tarjetas[0],400)


main()