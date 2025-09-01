import tkinter as tk
from tkinter import ttk, messagebox
import crud_sql  # importa el otro archivo

def cargar_usuarios():
    for row in tree.get_children():
        tree.delete(row)
    for usuario in crud_sql.obtener_usuarios():
        tree.insert("", tk.END, values=usuario)

def agregar_usuario():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    email = entry_email.get()

    if not nombre or not edad or not email:
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return

    crud_sql.insertar_usuario(nombre, int(edad), email)
    cargar_usuarios()
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def actualizar_usuario():
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showwarning("Error", "Selecciona un usuario")
        return

    item = tree.item(seleccionado)
    id_usuario = item["values"][0]

    nombre = entry_nombre.get()
    edad = entry_edad.get()
    email = entry_email.get()

    crud_sql.actualizar_usuario(id_usuario, nombre, int(edad), email)
    cargar_usuarios()

def eliminar_usuario():
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showwarning("Error", "Selecciona un usuario")
        return

    item = tree.item(seleccionado)
    id_usuario = item["values"][0]

    crud_sql.eliminar_usuario(id_usuario)
    cargar_usuarios()

# Ventana principal
root = tk.Tk()
root.title("CRUD con SQL Server y Tkinter")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame)
entry_nombre.grid(row=0, column=1)

tk.Label(frame, text="Edad:").grid(row=1, column=0, padx=5, pady=5)
entry_edad = tk.Entry(frame)
entry_edad.grid(row=1, column=1)

tk.Label(frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame)
entry_email.grid(row=2, column=1)

btn_agregar = tk.Button(frame, text="Agregar", command=agregar_usuario, bg="lightgreen")
btn_agregar.grid(row=3, column=0, padx=5, pady=5)

btn_actualizar = tk.Button(frame, text="Actualizar", command=actualizar_usuario, bg="lightblue")
btn_actualizar.grid(row=3, column=1, padx=5, pady=5)

btn_eliminar = tk.Button(frame, text="Eliminar", command=eliminar_usuario, bg="salmon")
btn_eliminar.grid(row=3, column=2, padx=5, pady=5)

tree = ttk.Treeview(root, columns=("ID", "Nombre", "Edad", "Email"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Edad", text="Edad")
tree.heading("Email", text="Email")
tree.pack(pady=10)

cargar_usuarios()

root.mainloop()
