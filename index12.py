from tkinter import *
from tkinter import ttk
import random
from turtle import width
import random
import sqlite3
import mysql.connector
from tkinter import messagebox


root = Tk()

############### Titulo de la App#################
root.title("Phyxture Qatar 2022")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(width=0, height=0)
#################################################

equipo_val = StringVar()
pj_val = StringVar()
grupo_val = StringVar()
copas_val = IntVar()
el_id = 0
equipos = []
grupos = ["A", "B", "C", "D", "E", "F", "G", "H"]

# imagen
img = PhotoImage(file="qatar_2.png")
img = img.subsample(1, 1)
lbl_img = Label(root, image=img)
lbl_img.grid(column=0, row=0, columnspan=4, pady=(10, 10))
root.configure(background="#FFFFFF")

team = Label(root, text="Equipo")
team.grid(row=1, column=0)
equipo = Entry(root, textvariable=equipo_val)
equipo.grid(row=1, column=1)

pj = Label(root, text="Continente")
pj.grid(row=2, column=0)
jogadores = Entry(root, textvariable=pj_val)
jogadores.grid(row=2, column=1)

grupo = Label(root, text="Grupo")
grupo.grid(row=3, column=0)
grupo_e = Entry(root, textvariable=grupo_val)
grupo_e.grid(row=3, column=1)

copas = Label(root, text="Copas")
copas.grid(row=4, column=0)
copas_e = Entry(root, textvariable=copas_val)
copas_e.grid(row=4, column=1)


def conexion():
    con = sqlite3.connect("databasetp.db")
    return con


try:
    miConexion = sqlite3.connect("databasetp.db")
    cursor = miConexion.cursor()
    cursor.execute(
        "CREATE TABLE equipo(id INT(7) NOT NULL PRIMARY KEY, nombre VARCHAR(128), grupo VARCHAR(1), copas INT(1), continente VARCHAR(30))"
    )
except Exception as ex:
    print(ex)


def crear():
    global el_id
    data = (str(el_id), str(equipo_val.get()), str(grupo_val.get()), str(copas_val.get()), str(pj_val.get()))
    sql = "INSERT INTO equipo(id, nombre, grupo, copas, continente) VALUES(?,?,?,?,?)"
    cursor.execute(sql, data)
    miConexion.commit()

    tree.insert("", "end", text=(el_id), values=(equipo_val.get(), pj_val.get(), grupo_val.get(), copas_val.get()))
    equipos.append(equipo_val.get())
    el_id += 1
    print(equipos)
    # messagebox.showinfo(message="El registro se creó con exito!", title="Agregar")


crear_b = Button(
    root, text="Crear", command=crear, relief=RAISED, fg="white", bg="blue", width=10
)
crear_b.grid(row=1, column=2)


def eliminar():
    valor = tree.focus()
    item = tree.item(valor)
    el_id = item["text"]

    data = (el_id,)
    sql = "DELETE FROM equipo WHERE id = ?;"
    cursor.execute(sql, data)
    miConexion.commit()
    tree.delete(valor)
    # messagebox.showinfo(message="El registro se eliminó con exito!", title="Eliminar")


eliminar_b = Button(
    root,
    text="Eliminar",
    relief=RAISED,
    fg="white",
    bg="red",
    command=eliminar,
    width=10,
)
eliminar_b.grid(row=2, column=2)


tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4")
tree.column("#0", width=30, minwidth=50, anchor=W)
# tree.column("#1", width=50, minwidth=50, anchor=W)
tree.column("col1", width=150, minwidth=80)
tree.column("col2", width=70, minwidth=50, anchor=W)
tree.column("col3", width=50, minwidth=40, anchor=W)
tree.column("col4", width=50, minwidth=40, anchor=W)
tree.heading("#0", text="ID")
tree.heading("col1", text="Equipo")
tree.heading("col2", text="Continente")
tree.heading("col3", text="Grupo")
tree.heading("col4", text="Copas")
tree.grid(row=10, column=0, columnspan=4)


equipo_val1 = StringVar()
pj_val1 = StringVar()
grupo_val1 = StringVar()
copas_val1 = IntVar()
global data
data = equipo_val1.get(), pj_val1.get()


team1 = Label(root, text="Equipo")
team1.grid(row=11, column=0)
equipo1 = Entry(root, textvariable=equipo_val1)
equipo1.grid(row=11, column=1)

pj1 = Label(root, text="Continente")
pj1.grid(row=11, column=2)
jogadores1 = Entry(root, textvariable=pj_val1)
jogadores1.grid(row=11, column=3)

grupo1 = Label(root, text="Grupo")
grupo1.grid(row=12, column=0)
grupo1_e = Entry(root, textvariable=grupo_val1)
grupo1_e.grid(row=12, column=1)

copas1 = Label(root, text="Copas")
copas1.grid(row=12, column=2)
copas1_e = Entry(root, textvariable=copas_val1)
copas1_e.grid(row=12, column=3)


def editar2():
    valor = tree.focus()
    item1 = tree.item(valor)
    el_id = item1["text"]
    tree.item(valor, values=(equipo_val1.get(), pj_val1.get()))
    data = (str(equipo_val1.get()), el_id)
    sql = "UPDATE equipo SET nombre = ? WHERE id = ?"
    cursor.execute(sql, data)
    miConexion.commit()
    # messagebox.showinfo(message="El registro se editó con exito!", title="Agregar")


editar_b2 = Button(
    root,
    text="Editar",
    relief=RAISED,
    fg="white",
    bg="green",
    command=editar2,
    width=10,
)
editar_b2.grid(row=1, column=3)


def agrupar_f():
    if len(grupos) != 0:
        gruposOut = []
        grupoElegido = random.choice(grupos)

        gruposOut.append(grupoElegido)
        grupos.remove(grupoElegido)
    else:
        print("----No hay mas grupos----")

    if len(equipos) != 0:
        equipoElegido = []
        for i in range(4):
            equipoRandom = random.choice(equipos)

            equipoElegido.append(equipoRandom)
            equipos.remove(equipoRandom)

        print("Grupo:")
        print(gruposOut)
        print("Equipos:")
        print(equipoElegido)

    else:
        print("----No hay mas equipos----")


def mostrar():
    cursor = miConexion.cursor()
    sql = "SELECT * FROM equipo"
    cursor.execute(sql)

    resultado = cursor.fetchall()
    miConexion.commit()
    for x in resultado:
        print(x)


agrupar = Button(
    root,
    text="Mostrar",
    relief=RAISED,
    fg="white",
    bg="purple",
    command=mostrar,
    width=10,
)
agrupar.grid(row=2, column=3)


root.mainloop()
