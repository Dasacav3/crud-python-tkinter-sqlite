from tkinter import StringVar, font, ttk
from tkinter.constants import CENTER, W, E, N, S
from model import Model
import tkinter as tk


class Aplicacion(Model):
    def __init__(self, window):
        super().__init__()
        # Here start the GUI
        self.window = window

        self.window.title("Gestión de productos")

        icon = tk.PhotoImage(file='logo.png')
        self.window.iconphoto(True, icon)
        self.window.configure(padx=20, pady=20)

        self.btn_style = ttk.Style().configure(
            "TButton", padding=6, background="#5E503F", foreground="#fff", font=("Bahnschrift", 12, 'bold'))

        # Title initial
        label = tk.Label(self.window,
                         text="Bienvenido al sistema de gestión de productos",
                         font=('Bahnschrift', 16, 'bold'),
                         padx=20,
                         image=icon,
                         compound='top',
                         )
        label.grid(row=0, column=0, columnspan=5, pady=(0, 20))
        label.configure(anchor=CENTER)

        btn = ttk.Button(self.window, text="Empezar",
                         command=self.getAll, style=self.btn_style)
        btn.grid(row=1, column=0, columnspan=5)

        self.window.mainloop()

    def getAll(self):

        self.window.destroy()

        self.window_list = tk.Tk()
        self.window_list.title("Gestión de productos")
        self.window_list.configure(padx=20, pady=20)

        self.modal_list_title = tk.Label(self.window_list, text="Listado de productos", font=("Bahnscrift",14,'bold'))
        self.modal_list_title.grid(row=0,column=0,columnspan=4)

        btn_add = ttk.Button(
            self.window_list, text="Añadir", command=self.modalAdd, style=self.btn_style)
        btn_add.grid(row=1, column=0, columnspan=4)

        # Table Thead
        thead_data = ['ID', 'NOMBRE', 'CANTIDAD', 'PRECIO']
        h = 0
        self.table = ttk.Treeview(columns=("#1", "#2", "#3"), height=10)
        for j in thead_data:
            self.table.grid(row=2, column=h)
            self.table.heading('#{}'.format(h), text=j, anchor=CENTER)
            h += 1

        self.get()

        self.btn_edit = ttk.Button(
            self.window_list, text="Editar", command=self.modalEdit)
        self.btn_edit.grid(row=3, column=0, columnspan=4, sticky=W+E)
        self.btn_delete = ttk.Button(
            self.window_list, text="Eliminar", command=self.deleteProduct)
        self.btn_delete.grid(row=4, column=0, columnspan=4, sticky=W+E)

        self.window_list.mainloop()

    def get(self):
        # Table Tbody
        records = self.table.get_children()
        for element in records:
            self.table.delete(element)
        datos = Model().select()
        for i in datos:
            self.table.insert('', 0, text=i[0], values=(i[1], i[2], i[3]))

    def addProduct(self):
        self.add(self.product_name.get(), self.product_cant.get(),
                 self.product_price.get())
        self.window_add.destroy()
        self.get()

    def modalAdd(self):
        self.window_add = tk.Toplevel()
        self.window_add.title("Añadir productos")
        self.window_add.configure(padx=20, pady=20)
        self.modal_add_label = ttk.Label(
            self.window_add, text="Añade un producto",font=("Bahnschrift", 14, 'bold'))
        self.modal_add_label.grid(row=0, column=1, columnspan=5)
        self.product_name_label = ttk.Label(
            self.window_add, text="Nombre", width=20)
        self.product_name_label.grid(row=1, column=1, columnspan=2)
        self.product_name = ttk.Entry(self.window_add, width=40)
        self.product_name.grid(row=1, column=3, columnspan=3)
        self.product_cant_label = ttk.Label(
            self.window_add, text="Cantidad", width=20)
        self.product_cant_label.grid(row=2, column=1, columnspan=2)
        self.product_cant = ttk.Entry(self.window_add, width=40)
        self.product_cant.grid(row=2, column=3, columnspan=3)
        self.product_price_label = ttk.Label(
            self.window_add, text="Precio", width=20)
        self.product_price_label.grid(row=3, column=1, columnspan=2)
        self.product_price = ttk.Entry(self.window_add, width=40)
        self.product_price.grid(row=3, column=3, columnspan=3)
        self.btn_add_product = ttk.Button(
            self.window_add, text="Registrar producto", command=self.addProduct)
        self.btn_add_product.grid(row=4, column=1, columnspan=5)
        self.window_add.mainloop()

    def edit(self):
        cod = self.product_id.get()
        name = self.product_name.get()
        cant = self.product_cant.get()
        price = self.product_price.get()
        self.update(name, cant, price, cod)
        self.window_edit.destroy()
        self.get()

    def modalEdit(self):
        cod = self.table.item(self.table.selection())['text']
        name = self.table.item(self.table.selection())['values'][0]
        cant = self.table.item(self.table.selection())['values'][1]
        price = self.table.item(self.table.selection())['values'][2]
        self.window_edit = tk.Toplevel()
        self.window_edit.title("Editar productos")
        self.window_edit.configure(padx=20, pady=20)
        self.modal_edit_label = ttk.Label(
            self.window_edit, text="Edición de producto",font=("Bahnschrift", 14, 'bold'))
        self.modal_edit_label.grid(row=0, column=0, columnspan=2)
        self.product_id_label = tk.Label(self.window_edit, text="Id")
        self.product_id_label.grid(row=1, column=0)
        self.product_id = tk.Entry(self.window_edit, textvariable=StringVar(
            self.window_edit, value=cod), state='readonly', width=30)
        self.product_id.grid(row=1, column=1)
        self.product_name_label = tk.Label(self.window_edit, text="Nombre")
        self.product_name_label.grid(row=2, column=0)
        self.product_name = tk.Entry(self.window_edit, textvariable=StringVar(
            self.window_edit, value=name), width=30)
        self.product_name.grid(row=2, column=1)
        self.product_cant_label = tk.Label(self.window_edit, text="Cantidad")
        self.product_cant_label.grid(row=3, column=0)
        self.product_cant = tk.Entry(self.window_edit, textvariable=StringVar(
            self.window_edit, value=cant), width=30)
        self.product_cant.grid(row=3, column=1)
        self.product_price_label = tk.Label(self.window_edit, text="Precio")
        self.product_price_label.grid(row=4, column=0)
        self.product_price = tk.Entry(self.window_edit, textvariable=StringVar(
            self.window_edit, value=price), width=30)
        self.product_price.grid(row=4, column=1)
        self.btn = ttk.Button(
            self.window_edit, text="Actualizar", command=self.edit).grid(row=5, column=0, columnspan=2)
        self.window_edit.mainloop()

    def deleteProduct(self):
        print(self.table.item(self.table.selection())['text'])
        self.delete(self.table.item(self.table.selection())['text'])
        self.get()


if __name__ == '__main__':
    window = tk.Tk()
    app = Aplicacion(window)
