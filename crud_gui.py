import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

# ------------------------
# Conexión a SQL Server
# ------------------------
def conectar():
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=GTAPIERO-POLI;" # Cambia por tu servidor, ej: "localhost\\SQLEXPRESS"
        "DATABASE=PruebaPython;"
        "UID=sa;"
        "PWD=tapiero;"
    )
    return conexion

# ----------------------------
# Funciones CRUD
# ----------------------------
def listar_usuarios():
    for row in tabla.get_children():
        tabla.delete(row)

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT  * FROM Usuarios")
    for u in cursor.fetchall():
        tabla.insert("", "end", values=u)
    conexion.close()

def insertar_usuario():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    email = entry_email.get()

    if not nombre or not edad or not email:
        messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos .")
        return
    
    conexion =  conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO Usuarios (nombre, edad, email) VALUES (?, ?, ?)",
                       (nombre, int(edad), email))
        conexion.commit()
        messagebox.showinfo("Éxito", f"Usuario {nombre} agregado correctamente . ")
        listar_usuarios()
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conexion.close

def eliminar_usuario():
    seleccionado = tabla.focus()
    if not seleccionado:
        messagebox.showwarning("Selección", "Seleccione un usuario para eliminar . ")
        return
    
    datos = tabla.item(seleccionado)["values"]
    id_usuario = datos[0]

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE id=?", (id_usuario,))
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Éxito", f"Usuario con ID {id_usuario} eliminado .")
    listar_usuarios()
