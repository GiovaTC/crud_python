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

def actualizar_usuario():
    seleccionado = tabla.focus()
    if not seleccionado:
        messagebox.showwarning("Selección", "Seleccione un usuario para actualizar .")
        return
    
    datos = tabla.item(seleccionado)["values"]
    id_usuario = datos[0]

    nombre = entry_nombre.get() or datos[1]
    edad = entry_edad.get() or datos[2]
    email = entry_email.get() or datos[3]

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE Usuarios SET nombre=?, edad=?, email=? WHERE = id=?",
                   (nombre, int(edad, email, id_usuario)))
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Éxito", f"Usuario con ID {id_usuario} actualizado .")

    # -------------------------
    # Interfaz gráfica (Tkinter)
    # -------------------------

    ventana = tk.Tk()
    ventana.title("CRUD Usuarios - Python + SQL Server")
    ventana.geometry("650*400")
    ventana.config(bg="#f4f6f9")

    # Frame de formulario
    frame_form = tk.Frame(ventana, bg="#ffffff", padx=10, pady=10, relief="ridge", borderwidth=2)
    frame_form.pack(side="top", fill="x", pady=10, padx=10)

    tk.Label(frame_form, text="Nombre:", bg="#ffffff").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_nombre = tk.Entry(frame_form, width=30)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        