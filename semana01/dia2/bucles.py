tab= int (input("Ingrese la tabla d emultiplicar que desea mostrar . "))


v2=tab*2
v1=tab*1
v3=tab*2
v4=tab*2


print(str(tab) + 'x 1 = ' + str(v1))
print(str(tab) + 'x 2 = ' + str(v2))
print(str(tab) + 'x 3 = ' + str(v3))


print("tabla for")

cont = 1

for cont in range(1,20):

    # for cont in range(1,20):
    val = tab * cont
    print(str(tab) + ' x ' + str(cont) + ' = ' + str(val))    


