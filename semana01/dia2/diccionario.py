#similar a json

capitales = {
    'Perú': 'lima',
    'Ecuador': 'Quito',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
}

print(capitales)
newCapital = { 'Brasil': 'Brasilia'}

capitales.update(newCapital)
print(capitales)

#eliminar valores

x = capitales.pop('Colombia','no existe ese pais en mi diccionario')
print(x)
