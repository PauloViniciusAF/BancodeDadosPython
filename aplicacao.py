from GUI import *
import backend as core

app = None

def view_command():
    rows = core.view()
    app.listClientes.delete(0,END)

    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    app.listClientes.delete(0, END)

    rows = core.search(app.txtNome.get(), app.txtSobre.get(), app.txtEmail.get(), app.txtCpf.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    core.insert(app.txtNome.get(), app.txtSobre.get(), app.txtEmail.get(), app.txtCpf.get())
    view_command()

def update_command():
    core.update(app.txtNome.get(), app.txtSobre.get(), app.txtEmail.get(), app.txtCpf.get())
    view_command()

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()

def getSelectedRow(event):
    global selected
    index= app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
    app.entNome.delete(0,END)
    app.entNome.insert(END,selected[1])
    app.entSobre.delete(0,END)
    app.entSobre.insert(END,selected[2])
    app.entEmail.delete(0,END)
    app.entEmail.insert(END,selected[3])
    app.entCpf.delete(0,END)
    app.entCpf.insert(END,selected[4])

    return selected

if __name__ == "__main__":
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnAtualizar.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnFechar.configure(command=app.window.destroy)
    app.run()
