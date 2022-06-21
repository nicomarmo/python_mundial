from tkinter import *
from tkinter import ttk
import random
from turtle import width
import random
import sqlite3
import mysql.connector
from tkinter import messagebox
import re


root = Tk()

############### Titulo de la App#################

root.title("Phyxture Qatar 2022")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(width=0, height=0)

#################################################

equipo_val = StringVar()
conti_val = StringVar()
grupo_val = StringVar()
copas_val = IntVar()
el_id = 0
equipos = []
grupos = ["A", "B", "C", "D", "E", "F", "G", "H"]

###################   Imagen  ##########################

img = PhotoImage(file="qatar_2.png")
img = img.subsample(1, 1)
lbl_img = Label(root, image=img)
lbl_img.grid(column=0, row=0, columnspan=10, pady=(5, 5), padx=(1, 1))
root.configure(background="#FFFFFF")

################# Tittulo para Entrys ###################

l1 = Label(
    root,
    text="INGRESE LOS DATOS SOLICITADOS",
    font=("bold", 8),
    fg="white",
    bg="#573CDE",
)
l1.grid(row=1, column=0, columnspan=6, padx=1, pady=1, sticky=W + E)

##################### Entrys ############################

team = Label(root, text="Equipo")
team.grid(row=2, column=0)
equipo = Entry(root, textvariable=equipo_val)
equipo.grid(row=2, column=1, padx=(5, 5), sticky=W)

conti = Label(root, text="Continente")
conti.grid(row=2, column=3)
continente = Entry(root, textvariable=conti_val)
continente.grid(row=2, column=4, padx=(5, 5), sticky=W)

grupo = Label(root, text="Grupo")
grupo.grid(row=3, column=0)
grupo_e = Entry(root, textvariable=grupo_val)
grupo_e.grid(row=3, column=1, padx=(5, 5), sticky=W)

copas = Label(root, text="Copas")
copas.grid(row=3, column=3)
copas_e = Entry(root, textvariable=copas_val)
copas_e.grid(row=3, column=4, padx=(5, 5), sticky=W)

############################## Base de Datos ###################################################


def conexion():
    con = sqlite3.connect("databasetp_1.db")
    return con


try:
    miConexion = sqlite3.connect("databasetp_1.db")
    cursor = miConexion.cursor()
    cursor.execute(
        "CREATE TABLE equipo(id INT(7) NOT NULL PRIMARY KEY, nombre VARCHAR(128), grupo VARCHAR(1), copas INT(1), continente VARCHAR(30))"
    )
except Exception as ex:
    print(ex)


def crear():
    global el_id
    miConexion.commit()
    data = (
        str(el_id),
        str(equipo_val.get()),
        str(grupo_val.get()),
        int(copas_val.get()),
        str(conti_val.get()),
    )
    sql = "INSERT INTO equipo(id, nombre, grupo, copas, continente) VALUES(?,?,?,?,?)"
    cursor.execute(sql, data)
    miConexion.commit()
    tree.insert(
        "",
        "end",
        text=(el_id),
        values=(equipo_val.get(), conti_val.get(), grupo_val.get(), copas_val.get()),
    )
    equipos.append(equipo_val.get())
    el_id += 1
    print(equipos)
    messagebox.showinfo(message="El registro se creó con exito!", title="Crear")


crear_b = Button(
    root, text="Crear", command=crear, relief=RAISED, fg="white", bg="#573CDE", width=10
)
crear_b.grid(row=4, column=0, padx=(10, 10), pady=(10, 10))


def eliminar():
    valor = tree.focus()
    item = tree.item(valor)
    el_id = item["text"]

    data = (el_id,)
    sql = "DELETE FROM equipo WHERE id = ?;"
    cursor.execute(sql, data)
    miConexion.commit()
    tree.delete(valor)
    messagebox.showinfo(message="El registro se eliminó con exito!", title="Eliminar")


eliminar_b = Button(
    root,
    text="Eliminar",
    relief=RAISED,
    fg="white",
    bg="red",
    command=eliminar,
    width=10,
)
eliminar_b.grid(row=4, column=1, padx=(10, 10), pady=(10, 10), sticky=E)


###################### Treeview ##########################

tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=100, minwidth=50)
tree.column("col2", width=100, minwidth=50, anchor=W)
tree.column("col3", width=100, minwidth=50, anchor=W)
tree.column("col4", width=100, minwidth=50, anchor=W)
tree.heading("#0", text="ID")
tree.heading("col1", text="Equipo")
tree.heading("col2", text="Continente")
tree.heading("col3", text="Grupo")
tree.heading("col4", text="Copas")
tree.grid(row=11, column=0, columnspan=6)

##################### Titulo de Entrys para Editar ############################

l1 = Label(
    root,
    text="INGRESE LOS DATOS A EDITAR",
    font=("bold", 8),
    fg="white",
    bg="green",
)
l1.grid(row=12, column=0, columnspan=6, padx=1, pady=1, sticky=W + E)

##################### Entrys  para Editar ############################

equipo_val1 = StringVar()
conti_val1 = StringVar()
grupo_val1 = StringVar()
copas_val1 = IntVar()
global data
data = equipo_val1.get(), conti_val1.get()


team1 = Label(root, text="Equipo")
team1.grid(row=13, column=0)
equipo1 = Entry(root, textvariable=equipo_val1)
equipo1.grid(row=13, column=1)

pj1 = Label(root, text="Continente")
pj1.grid(row=13, column=2)
jogadores1 = Entry(root, textvariable=conti_val1)
jogadores1.grid(row=13, column=3)

grupo1 = Label(root, text="Grupo")
grupo1.grid(row=14, column=0)
grupo1_e = Entry(root, textvariable=grupo_val1)
grupo1_e.grid(row=14, column=1)

copas1 = Label(root, text="Copas")
copas1.grid(row=14, column=2)
copas1_e = Entry(root, textvariable=copas_val1)
copas1_e.grid(row=14, column=3)

#########################################################################
equipo_val1.set("Equipo")
conti_val1.set("Continente")
grupo_val1.set("Grupo")
copas_val1.set("0")


def editar2():
    valor = tree.focus()
    item1 = tree.item(valor)
    el_id = item1["text"]
    tree.item(
        valor,
        values=(
            equipo_val1.get(),
            conti_val1.get(),
            grupo_val1.get(),
            copas_val1.get(),
        ),
    )
    data = (
        str(equipo_val1.get()),
        str(grupo_val1.get()),
        str(copas_val1.get()),
        str(conti_val1.get()),
        el_id,
    )
    sql = "UPDATE equipo SET nombre = ?, grupo = ?, copas = ?, continente = ? WHERE id = ?"
    cursor.execute(sql, data)
    miConexion.commit()
    messagebox.showinfo(message="El registro se editó con exito!", title="Agregar")


editar_b2 = Button(
    root,
    text="Editar",
    relief=RAISED,
    fg="white",
    bg="green",
    command=editar2,
    width=10,
)
editar_b2.grid(row=4, column=2, columnspan=2, pady=(10, 10), sticky=E + N)


def mostrar():
    ventana = Toplevel()
    ventana.title("Equipos")

    tree = ttk.Treeview(ventana)
    tree["columns"] = ("col1", "col2", "col3", "col4")
    tree.column("#0", width=0, minwidth=0, anchor=W)
    tree.column("col1", width=70, minwidth=50, anchor=W)
    tree.column("col2", width=70, minwidth=50, anchor=W)
    tree.column("col3", width=70, minwidth=50, anchor=W)
    tree.column("col4", width=70, minwidth=50, anchor=W)
    tree.heading("#0", text="ID")
    tree.heading("col1", text="Equipo")
    tree.heading("col2", text="Grupo")
    tree.heading("col3", text="Copas")
    tree.heading("col4", text="Continente")
    tree.grid(row=0, column=0, columnspan=2)

    cursor = miConexion.cursor()
    sql = "SELECT nombre,grupo,copas,continente FROM equipo ORDER BY grupo"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    miConexion.commit()

    print(resultado)
    rows = resultado
    for i in rows:
        tree.insert("", "end", text=el_id, values=i)


agrupar = Button(
    root,
    text="Mostrar",
    relief=RAISED,
    fg="white",
    bg="purple",
    command=mostrar,
    width=10,
)
agrupar.grid(row=4, column=3, columnspan=2, padx=(10, 10), pady=(10, 10), sticky=E)


def cerrar():
    sql = "DROP TABLE equipo"
    cursor.execute(sql)
    miConexion.commit()
    print("ya se elimino")
    root.destroy()

closeButton = Button(
    root, text="Cerrar", relief=RAISED, fg="white", bg="black", command=cerrar, width=10
)
closeButton.grid(row=14, column=4, columnspan=2, padx=(10, 10), pady=(10, 10), sticky=E)

def handler(): 
    if messagebox.askokcancel("Quit?", "Are you sure you want to quit?"):
        sql = "DROP TABLE equipo"
        cursor.execute(sql)
        miConexion.commit()
        print("ya se elimino")
        root.quit()

root.protocol("WM_DELETE_WINDOW", handler)


root.mainloop()


### aguante boca ###
