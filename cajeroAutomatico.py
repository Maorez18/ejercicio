def menu(op):
    while(op<1 or op>4):
        print("\n1. Ver saldo")
        print("2. Consignar")
        print("3. Retirar")
        print("4. Salir")
        op=int(input("Digite una opcion: "))
        if(op<1 or op>4):
            print("Digite una opcion valida\n")
        else:
            return op
def salida():
    print("Muchas gracias por usar nuestros servicios, te esperamos de vuelta pronto. Adios")
    exit
def consignacion(saldo, movimientos):
    con=float(0.0)
    while(con<=0):
        con=float(input("Digite la cantidad a consignar: "))
        if(con<=0):
            print("Digite un valor valido.")
    saldo=saldo+con
    movimientos.append("c")
    movimientos.append(con)
    return saldo
def retiro(saldo, movimientos):
    ret=float(0.0)
    while(ret<=0):
        ret=float(input("Digite la cantidad a retirar: "))
        if(ret<=0):
            print("Digite un valor valido.")
    if(saldo-ret>=10000):
        saldo=saldo-ret
        movimientos.append("r")
        movimientos.append(ret)
        return saldo
    else:
        print("Cantidad a retirar no valida. No puede quedar menos de 10000 en la cuenta\n")
        return saldo
def verSaldo(saldo, movimientos):
    print("El saldo total de la cuenta es ",saldo)
    if (saldo!=0.0):
        for i in movimientos:
            if (i=="c"):
                print("Consignacion: ")
            elif (i=="r"):
                print("Retiro: ")
            else:
                print(i)
#Main
saldo=float(0.0)
movimientos=[]
op=0
while(op==0):
    op=menu(op)
    match op:
        case 1:
            verSaldo(saldo, movimientos)
            op=0
        case 2:
            saldo=consignacion(saldo, movimientos)
            op=0
        case 3:
            saldo=retiro(saldo, movimientos)
            op=0
        case 4:
            salida()