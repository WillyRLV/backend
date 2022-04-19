dias=["lunes", "martes", "miercoles"]

print(dias)

#para inprimir un o varios datos en un arreglo nuevamente se usa el " : " ,"[valor:valor"]
print(dias[1:2])
#para añadir un nuevo elemento al arreglo
dias.append("jueves")
#paa eliminar un elemento de un arreglo se usa pop(), ahora si lo dejamos sin dato interno por defecto elimina el ultimo
#pero si especifica el dato(indice), lo removerá.
#dias.pop(0) -> esto borrará el primer elementi
#dias.pop() -> esto borrará el ultimo
print(dias)

