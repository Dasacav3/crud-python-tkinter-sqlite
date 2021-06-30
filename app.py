from tkinter.constants import CENTER, SOLID
from model import Model
import tkinter as tk


class Aplicacion(Model):
    def __init__(self):
        super().__init__()
        print("Bienvenido al sistema de productos\n\n¿Que opción, desea seleccionar?\n\n1. Añadir productos.\n2. Consultar productos existentes\n3. Editar productos\n4. Eliminar productos")
        try:
            option = int(input("->"))
            self.main(option)
        except ValueError:
            print("Error solo se permiten valores numericos")

    def main(self, option):
        if option == 1:
            print(self.add("Papas", 100, 100))
        elif option == 2:
            print(self.select())
        elif option == 3:
            print(self.update("Portatil HP 14 pulgadas FULL HD", 250, 3700000, 3))
        elif option == 4:
            print(self.delete(3))
        elif option == 0:
            print("Gracias, feliz dia")
        else:
            print("Opción no existente")

# resultado = Aplicacion()


window = tk.Tk()

window.title("Gestión de productos")

icon = tk.PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.configure(padx=20,pady=20)

label = tk.Label(window,
                 text="Bienvenido al sistema de gestión de productos",
                 font=('Arial', 16, 'bold'),
                 padx=20,
                 image=icon,
                 compound='left',
                 )
label.grid(row=0, column=0, columnspan=5,pady=(0,20))
label.configure(anchor=CENTER)

thead_id = tk.Label(window, text="ID", font=('Arial', 14, 'bold'))
thead_id.grid(row=1, column=0)

thead_name = tk.Label(window, text="NOMBRE", font=('Arial', 14, 'bold'))
thead_name.grid(row=1, column=1)

thead_quantity = tk.Label(window, text="CANTIDAD", font=('Arial', 14, 'bold'))
thead_quantity.grid(row=1, column=2)

thead_price = tk.Label(window, text="PRECIO", font=('Arial', 14, 'bold'))
thead_price.grid(row=1, column=3)

thead_actions = tk.Label(window, text="ACCIONES", font=('Arial', 14, 'bold'))
thead_actions.grid(row=1, column=4, columnspan=2)

datos = Model().select()

row = 2
col = 0
for i in datos:
    for j in i:
        tbody = tk.Label(window, text=j, font=('Arial', 14))
        tbody.grid(row=row, column=col)
        tbody_btn = tk.Button(window, text="Editar", font=(
            'Arial', 14), anchor=CENTER, background="#12355B", fg="#fff")
        tbody_btn.grid(row=row, column=4)
        tbody_btn = tk.Button(window, text="Eliminar", font=(
            'Arial', 14), anchor=CENTER, background="#5C1A1B", fg="#fff")
        tbody_btn.grid(row=row, column=5)
        col += 1
    row += 1
    col = 0

window.mainloop()
