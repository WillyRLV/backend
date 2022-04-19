
from msvcrt import getch, getche
from queue import Empty
import tabulate
#PROGRAMA PARA
# CREATE - C
# READ - R
# UPDATE - U
# DELETE - D
print("-" * 50)
print("|" + " " * 9 + "MATRICULA DE ALUMNOS EN CODIGO " + " "* 8 + "|")
print("-" * 50)
print("|" + " " * 9 + "MENU DE OPCIONES     " + " "* 18 + "|")
print("|" + " " * 9 + "[1] REGISTRAR ALUMNO " + " "* 18 + "|")
print("|" + " " * 9 + "[2] MOSTRAR ALUMNOS  " + " "* 18 + "|")
print("|" + " " * 9 + "[3] ACTUALIZAR ALUMNO" + " "* 18 + "|")
print("|" + " " * 9 + "[4] ELIMINAR ALUMNO  " + " "* 18 + "|")
print("|" + " " * 9 + "[5] SALIR            " + " "* 18 + "|")
print("-" * 50)
opcion = 0
alumnos = [{'nombre':'','email':'','celular':''}]
while(opcion != 5):
    opcion = int(input("INGRESE OPCIÓN DEL MENU :"))  
    if(opcion == 1):
        print("NUEVO ALUMNO ")
        nombre  = input("NOMBRE  : ")
        email   = input("EMAIL   : ")
        celular = input("CELULAR : ")
        dictAlumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos.append(dictAlumno)
        print("ALUMNO REGISTRADO CON EXITO!!!")
        getch()
    elif(opcion == 2):
        print("RELACIÓN DE ALUMNOS")
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]
        print(tabulate.tabulate(registros,cabeceras))


    elif(opcion == 3):
    
        print("ACTUALIZAR ALUMNO")
        #PASO 1 BUSCAR EL ALUMNO A EDITAR
        valorBusqueda = input("Ingrese el email del alumno a actualizar : ")
        indexAlumno = -1

        #si no hay valor monstrará el mensaje
        if  not valorBusqueda:
            print("ingrese un dato valido porfavor")


        else:    
                
            for i in range(len(alumnos)):
                dicAlumnoBusqueda = alumnos[i]
                for clave,valor in dicAlumnoBusqueda.items():


                    if(valor == valorBusqueda and clave == 'email'):
                        indexAlumno=i
                        break
                        
            print(dicAlumnoBusqueda.items())
            # if indexAlumno>=0:
            #     print("el alumno está en el indice" + str(indexAlumno-1))
                
            #     print(" se encontró el dato")
            #     nombre  = input("NOMBRE  : ")
            #     email   = input("EMAIL   : ")
            #     celular = input("CELULAR : ")
            #     dictAlumnoEditar = {
            #     'nombre':nombre,
            #     'email':email,
            #     'celular':celular}
            #         #PASO 3 ACTUALIZAR LOS DATOS DEL ALUMNO A EDITAR
            #     alumnos[indexAlumno] = dictAlumnoEditar
            #     print("ALUMNO ACTUALIZADO !!!")    
                        
            # else:
            #     print("no se encontró el dato")

                
                            
    elif(opcion == 4):
        print("ELIMINAR ALUMNO")
        #PASO 1 BUSCAR EL ALUMNO A ELIMINAR
        valorBusqueda = input("Ingrese el email del alumno a eliminar : ")
        indexAlumno = -1
        for i in range(len(alumnos)):
            dicAlumnoBusqueda = alumnos[i]
            for clave,valor in dicAlumnoBusqueda.items():
                if(valor == valorBusqueda and clave == 'email'):
                    indexAlumno = i
                    break
        #PASO 2 INGRESAR LOS NUEVOS VALORES PARA EL ALUMNO A ELIMINAR
        if(indexAlumno == -1):
            print("No se encontro el email del alumno")
        else:
            #ELIMINAR EL ALUMNO
            alumnos.pop(indexAlumno)
            print("ALUMNO ELIMINADO !!!")
    elif(opcion == 5):
        print("FINALIZANDO PROGRAMA")
    else:
        print("OPCION INCORRECTA")

    