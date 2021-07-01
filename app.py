from tkinter import font
from tkinter.constants import CENTER
from model import Model
import tkinter as tk


class Aplicacion(Model):
    def __init__(self):
        super().__init__()
        # Here start the GUI
        self.window = tk.Tk()

        self.window.title("Gestión de productos")

        icon = tk.PhotoImage(file='logo.png')
        self.window.iconphoto(True, icon)
        self.window.configure(padx=20, pady=20)

        # Title initial
        label = tk.Label(self.window,
                        text="Bienvenido al sistema de gestión de productos",
                        font=('Rockwell', 16, 'bold'),
                        padx=20,
                        image=icon,
                        compound='top',
                        )
        label.grid(row=0, column=0, columnspan=5, pady=(0, 20))
        label.configure(anchor=CENTER)

        btn = tk.Button(self.window,text="Empezar",bg="black",fg="#fff",font=('Rockwell', 12, 'bold'),command=self.getAll)
        btn.grid(row=1,column=0,columnspan=5)

        self.window.mainloop()
    
    def getAll(self):

        self.window.destroy()

        window = tk.Tk()

        window.title("Gestión de productos")

        # icon2 = tk.PhotoImage(file='logo.png')
        # window.iconphoto(True, icon2)
        window.configure(padx=20, pady=20)

        # Table Thead
        thead_data = ['ID', 'NOMBRE', 'CANTIDAD', 'PRECIO', 'ACCIONES']
        h = 0
        for j in thead_data:
            thead = tk.Label(window, text=j, font=('Rockwell', 14, 'bold'))
            if j != "ACCIONES":
                thead.grid(row=1, column=h)
            else:
                thead.grid(row=1, column=h, columnspan=2)
            h += 1

        # Table Tbody
        datos = Model().select()
        row = 2
        col = 0
        for i in datos:
            for j in i:
                tbody = tk.Label(window, text=j, font=('Rockwell', 14))
                tbody.grid(row=row, column=col)
                tbody_btn = tk.Button(window, text="Editar", font=(
                    'Rockwell', 14), anchor=CENTER, background="#12355B", fg="#fff")
                tbody_btn.grid(row=row, column=4)
                tbody_btn = tk.Button(window, text="Eliminar", font=(
                    'Rockwell', 14), anchor=CENTER, background="#5C1A1B", fg="#fff")
                tbody_btn.grid(row=row, column=5)
                col += 1
            row += 1
            col = 0

        window.mainloop()
    
    def add(self,*args):
        print(args)

    def edit(self,*args):
        print(args)

    def delete(self,*args):
        print(args)

resultado = Aplicacion()
