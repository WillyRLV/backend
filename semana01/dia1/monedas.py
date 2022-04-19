# programa para convertir monedas

# version 1.0 -convertir soles a dolares
#inputs - entradas
# proceso
#outputs - slaidas


aor = input("ingrese el monto en soles : ")
d:float =3.72
e:float =4.05

# proces
op = "0"
while (op=="0"):
    print("opcion 1 - soles a dolares")
    print("opcion 2 - dolares a soles")
    print("opcion 3 - euros a soles")
    print("opcion 4 - soles a euros")
    op = input("elija una opcion :")

    if op=="1":
#soles a dolares
        adolar = float(aor) / d
        bdolarF = "$ {:,.5f}".format(adolar)
        print("el monto es:" + str(bdolarF))


    elif op=="2":
#dolares a soles
        asoles = float(aor) * d
        bsolesF = "S/. {:,.5f}".format(asoles)

        print("el monto es:" + str(bsolesF))

    elif op=="3":
#soles a euros        
        aeuros = float(aor) / e
        beurosF = "€ {:,.5f}".format(aeuros)

        print("el monto es:" + str(beurosF))

    elif op=="4":
#euros a soles      
        asolesE = float(aor) * e
        bsolesEF = "S/. {:,.5f}".format(asolesE)

        print("el monto es:" + str(bsolesEF)) 

    else:
        print("debe seleccionar una opcion valida")
        op="0"

    