from tkinter import*
from tkinter import messagebox


def saludar():
    print("Hola mundo tk")
    messagebox.showinfo("mensaje","hola " + txtNombre.get())
app = Tk()
app.title("mi primer interfaz")
app.geometry('300x100')
frame = LabelFrame(app, text='ventana')
frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20)
lbNombre=Label(frame,text='Nombre: ')
lbNombre.grid(row=1,column=0)

#caja de texto

txtNombre=Entry(frame)
txtNombre.grid(row=1,column=1)

#boton

btnSaludo = Button(frame,text='saludar',command=saludar)
btnSaludo.grid(row=1,column=2)
app.mainloop()