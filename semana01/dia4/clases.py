# alumnos = {
#     'nombre':'william ricardo',
#     'email':'william@gmail.com'
# }


# insertarAlumno(){ 
#     print("ssd")
# }

# class Alumno:
#     def FunctionName(args):

#crear clase

class Automovil:
    def __init__(self ,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color=col
        self.marca=mar

    def encender(self):
        print('encender ' + self.marca)

    def avanzar(self):
        print('avanzar ' + self.marca)

    def acelerar(self):
        print('acelerar ' + self.marca)

    def frenar(self):
        print('frenar ' + self.marca)



#creacion de objetos

vw = Automovil(1978,'CH-1234', 'Amarillo', 'Volkswagen')
print("se creo el objeto vw con los datos")
print("año : " + str(vw.año))
print("placa : " + vw.placa)
print("color : " + vw.color)
print("marca : " + vw.marca)

vw.encender()

tico = Automovil(1985,'EJ-2345', 'Rojo', 'TICO')
tico.encender()
tico.frenar()


lamborghini = Automovil(2018,'E7P-367', 'Azul', 'Lamborghini')
lamborghini.acelerar()


        
        
        