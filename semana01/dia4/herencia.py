from audioop import add
from operator import mod


class Persona:
    def __init__(self, nomb,ema):
        self.nombre = nomb
        self.email=ema

    def mostrar(self):
        print("Nombre : " + self.nombre + " Email : " + self.email )



class Alumno(Persona):
    pass

# class Profesor:
#     def __init(self, nom,ema,mod):
#         self.nombre = nom
#         self.email=ema
#         self.modulo= mod

#     # def mostrar(self):
#     #     print("Nombre : " + self.nombre + "Email : " + self.email + "Modulo" + self.modulo)


class Profesor(Persona):
    
    def __init__(self, nom,ema,mod):
        super().__init__(nom,ema)
        self.modulo = mod


    def mostrar(self):
        super().mostrar()
        print("dicta el modulo de : " + self.modulo)




alu1 = Alumno('carlos tello','ctello@gmail.com')
alu1.mostrar()


profe1 = Profesor('cesar mayta','mayta@gmail.com','backend')
profe1.mostrar()

        