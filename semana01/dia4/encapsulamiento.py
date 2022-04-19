# clase para administrar

class Usuario:
    def __init__(self , nom,pwd):
        self.nombre = nom
        self._password = pwd


    def iniciarSesion(self):
        if (self.nombre == 'admin' and self._password == '12345'):
            print('Bienvenido ' + self.nombre)

        else:
            print('Datos de acceso incorrectos')


##usando mi clase usuario

usuario1 = Usuario('admin', 'admin')
usuario1.iniciarSesion()
print(usuario1._password)

usuario2 = Usuario('admin', '12345')
usuario2.iniciarSesion()
# print(usuario2._password)


# usuario1.nombre='jorge'
# print("nuevo nombre de usuario" + usuario1.nombre)
# usuario1._password ='12345'
            
    
        