#tabla de multiplicar

from calendar import c
from turtle import st


n= int(input("ingrese  la tabla d emultiplicar que desea mostrar: "))
c=1
while(c <=12):
    valor = n * c
    print(str(n)+ "X" + str(c) + " = " + str(valor))
    c+=1 

#area del cuadrado 



