n= int(input("ingrese lado de cuadrado: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")

        
print("segunda forma de realizar el problema")


for fila in range(1,n+1,1):
    if (fila==1 or fila == n):
        print('* '*n)
    else:
        print('* '+ '  ' * (n-2) + '*')

        
    


