from cgitb import text
from platform import win32_edition
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Treeview


class Alumno:
    # def registrarAlumno(self):
    #     pass

    def registrarAlumno(self):
        self.trvAlumnos.insert('',0,text=self.Nombre.get(),values=self.Email.get())
        
    def __init__(self, window):
        self.wind = window
        self.wind.title('CRUD DE ALUMNOS')
        self.wind.geometry('450x100')

    

        #FRAME
        frame = LabelFrame(self.wind, text='Registro de nuevo Alumno')
        frame.grid(row=0, column=0,columnspan=3,pady=10)

    
        ##CAMPO NOMBRE
        ##LABEL NOMBRE


        lbNombre = Label(frame,text='Nombre : ')
        lbNombre.grid(row=1,column=0)

        self.Nombre = Entry(frame)
        self.Nombre.grid(row=1,column=1)


        ##campo email

        lbEmail = Label(frame,text='Email : ')
        lbEmail.grid(row=2,column=0)

        self.Email = Entry(frame)
        self.Email.grid(row=2,column=1)

        

        ##boton nuevo alumno##
        btnNuevoAlumno = Button(frame,text='Registrar',command=self.registrarAlumno)
        btnNuevoAlumno.grid(row=4,columnspan=2,sticky=W + E)


        #####TRERVIEW

        self.trvAlumnos = Treeview(height=10,columns=2)
        self.trvAlumnos.grid(row=5,column=00,columnspan=2,padx=10)
        self.trvAlumnos.heading('#0',text='Nombre',anchor=CENTER)
        self.trvAlumnos.heading('#1',text='Email',anchor=CENTER)

        



window = Tk()
app = Alumno(window)
window.mainloop()