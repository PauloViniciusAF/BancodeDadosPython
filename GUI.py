import pandas as pd
from tkinter import *

class Gui():
    x_pad = 5
    y_pad = 3
    witdh_entry = 30

    window = Tk()
    window.wm_title("PYSQL")

    txtNome = StringVar()
    txtSobre = StringVar()
    txtEmail = StringVar()
    txtCpf = StringVar()

    lblNome = Label(window, text="Nome")
    lblSobre = Label(window, text="Sobrenome")
    lblEmail = Label(window, text="Email")
    lblCpf = Label(window, text="CPF")
    entNome = Entry(window, textvariable=txtNome, width=witdh_entry)
    entSobre = Entry(window, textvariable=txtSobre, width=witdh_entry)
    entEmail = Entry(window, textvariable=txtEmail, width=witdh_entry)
    entCpf = Entry(window, textvariable=txtCpf, width=witdh_entry)

    listClientes = Listbox(window, width = 100)
    scrollClientes = Scrollbar(window)
    btnViewAll = Button(window, text="Ver Todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnAtualizar = Button(window, text="Atualizar Selecionados")
    btnDel = Button(window, text="Deletar Selecionados")
    btnFechar = Button(window, text="Fechar")



    lblNome.grid(row=0, column=0)
    lblSobre.grid(row=1, column=0)
    lblEmail.grid(row=2, column=0)
    lblCpf.grid(row=3, column=0)

    entNome.grid(row=0, column=1, padx=50, pady =50)
    entSobre.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCpf.grid(row=3, column=1)

    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=2, columnspan=2)
    btnBuscar.grid(row=5, column=2, columnspan=2)
    btnInserir.grid(row=6, column=2, columnspan=2)
    btnAtualizar.grid(row=7, column=2, columnspan=2)
    btnDel.grid(row=8, column=2, columnspan=2)
    btnFechar.grid(row=9, column=2, columnspan=2)

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(padx=x_pad,pady=y_pad,sticky='WE')
        elif widget_class == "ListBox":
            child.grid_configure(padx=0,pady=0,sticky='NS')
        elif widget_class == "Button":
            child.grid_configure(padx=0,pady=0,sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady = y_pad, stick = 'N')

    def run(self):
        Gui.window.mainloop()


  