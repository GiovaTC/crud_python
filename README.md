	
# CRUD en Python conectado a SQL Server usando la librería `pyodbc`

<img width="2554" height="1079" alt="image" src="https://github.com/user-attachments/assets/6b2df811-60ca-47a6-88bd-d914eaecf9a7" />
	
<img width="2559" height="1042" alt="image" src="https://github.com/user-attachments/assets/51c95902-7966-44cd-ae19-c9c261baa8a5" />

-- Inserts de prueba para la tabla Usuarios
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Carlos Pérez', 28, 'carlos.perez@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('María Gómez', 34, 'maria.gomez@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Juan Rodríguez', 22, 'juan.rodriguez@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Ana Torres', 29, 'ana.torres@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Luis Ramírez', 41, 'luis.ramirez@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Sofía Morales', 25, 'sofia.morales@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Pedro Hernández', 36, 'pedro.hernandez@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Laura Castillo', 27, 'laura.castillo@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Andrés Fernández', 33, 'andres.fernandez@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Camila Vargas', 30, 'camila.vargas@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Diego Rojas', 24, 'diego.rojas@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Paola Medina', 32, 'paola.medina@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Fernando Cruz', 38, 'fernando.cruz@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Valentina López', 26, 'valentina.lopez@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Ricardo Sánchez', 35, 'ricardo.sanchez@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Daniela Herrera', 29, 'daniela.herrera@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('José Martínez', 40, 'jose.martinez@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Carolina Jiménez', 31, 'carolina.jimenez@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Martín Ortega', 23, 'martin.ortega@example.com');
INSERT INTO Usuarios (nombre, edad, email) VALUES ('Isabella Pardo', 27, 'isabella.pardo@example.com');

---

## 📌 Pasos previos

1. Instalar el conector de SQL Server:

```bash

pip install pyodbc
Asegúrate de tener SQL Server instalado y en ejecución.

Crear una base de datos de prueba:

sql

CREATE DATABASE PruebaPython;
GO
Dentro de esa base de datos, crear la tabla Usuarios:

sql

USE PruebaPython;

CREATE TABLE Usuarios (
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre NVARCHAR(100) NOT NULL,
    edad INT,
    email NVARCHAR(100) UNIQUE NOT NULL
);

📌 Código Python (CRUD con SQL Server)
python

import pyodbc

# -------------------------
# Conexión a SQL Server
# -------------------------
def conectar():
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"     # Cambia por tu servidor, ej: "localhost\\SQLEXPRESS"
        "DATABASE=PruebaPython;"
        "UID=sa;"               # Usuario de SQL Server
        "PWD=tu_password;"      # Contraseña
    )
    return conexion


# -------------------------
# CRUD
# -------------------------

# CREATE
def insertar_usuario(nombre, edad, email):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Usuarios (nombre, edad, email) VALUES (?, ?, ?)", 
                   (nombre, edad, email))
    conexion.commit()
    conexion.close()
    print(f"Usuario {nombre} insertado con éxito.")


# READ
def listar_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    usuarios = cursor.fetchall()
    conexion.close()
    return usuarios


# UPDATE
def actualizar_usuario(id_usuario, nombre=None, edad=None, email=None):
    conexion = conectar()
    cursor = conexion.cursor()
    
    if nombre:
        cursor.execute("UPDATE Usuarios SET nombre=? WHERE id=?", (nombre, id_usuario))
    if edad:
        cursor.execute("UPDATE Usuarios SET edad=? WHERE id=?", (edad, id_usuario))
    if email:
        cursor.execute("UPDATE Usuarios SET email=? WHERE id=?", (email, id_usuario))
    
    conexion.commit()
    conexion.close()
    print(f"Usuario con ID {id_usuario} actualizado.")


# DELETE
def eliminar_usuario(id_usuario):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE id=?", (id_usuario,))
    conexion.commit()
    conexion.close()
    print(f"Usuario con ID {id_usuario} eliminado.")


# -------------------------
# Ejemplo de uso
# -------------------------
if __name__ == "__main__":
    # Insertar usuarios
    insertar_usuario("Juan Pérez", 30, "juan@example.com")
    insertar_usuario("Ana Gómez", 25, "ana@example.com")

    # Listar usuarios
    print("Usuarios registrados:")
    for u in listar_usuarios():
        print(u)

    # Actualizar usuario
    actualizar_usuario(1, nombre="Juanito Pérez", edad=31)

    # Eliminar usuario
    eliminar_usuario(2)

    # Listar usuarios finales
    print("\nUsuarios después de cambios:")
    for u in listar_usuarios():
        print(u)
		
📌 Notas importantes
En la función conectar(), cambia:

SERVER=localhost; → si usas SQLEXPRESS, sería:

SERVER=localhost\SQLEXPRESS;
UID=sa; y PWD=tu_password; → por tu usuario y contraseña de SQL Server.

El driver ODBC Driver 17 for SQL Server debe estar instalado en tu máquina.
Si usas una versión más nueva, cambia por:

ODBC Driver 18 for SQL Server

# 🚀 Ejecutar aplicación CRUD en Python con SQL Server

---

## 🔹 1. Prepara SQL Server

Abre **SQL Server Management Studio (SSMS)** o **Azure Data Studio**.

Crea la base de datos de prueba (solo una vez):

```sql
CREATE DATABASE PruebaPython;
GO

USE PruebaPython;

CREATE TABLE Usuarios (
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre NVARCHAR(100) NOT NULL,
    edad INT,
    email NVARCHAR(100) UNIQUE NOT NULL
);
```
---

## 🔹 2. Instala dependencias en Python

Abre tu terminal o consola y ejecuta:

```bash
pip install pyodbc
```

⚠️ Además necesitas el driver **ODBC Driver 17 (o 18) for SQL Server**:

👉 En Windows puedes descargarlo desde: [Microsoft ODBC Driver for SQL Server](https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server).

---

## 🔹 3. Ajusta el archivo Python

Guarda el código del CRUD en un archivo, por ejemplo: **`crud_sqlserver.py`**

En la parte de la conexión:

```python
conexion = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\SQLEXPRESS;"  # <-- ajusta tu instancia aquí
    "DATABASE=PruebaPython;"
    "UID=sa;"
    "PWD=TuPasswordAqui;"
)
```

---

## 🔹 4. Ejecuta la aplicación

En la consola, ve a la carpeta donde guardaste `crud_sqlserver.py` y ejecuta:

```bash
python crud_sqlserver.py
```

---

## 🔹 5. Resultado esperado

Deberías ver en la consola algo como:

```
Usuario Juan sonora insertado con éxito.
Usuario Ana Loceba insertado con éxito.
Usuarios registrados:
(1, 'Juan sonora', 40, 'sonora@clr.com.co')
(2, 'Ana Loceba', 64, 'loceba@clr.com.co')
Usuario con ID 2 actualizado.
Usuario con ID 1 eliminado.

Usuarios después de cambios:
(2, 'Ana Loceba', 94, 'loceba@clr.com.co')
```

# 🙌 Ventana gráfica (GUI) con Tkinter

Tkinter (viene con Python por defecto).

Te preparo una primera versión con una interfaz visual básica pero agradable, que te permite:

- Insertar usuarios.  
- Listar usuarios en una tabla.  
- Actualizar datos de un usuario.  
- Eliminar usuarios.  

---

## 📌 CRUD con GUI (Tkinter)

Guarda este archivo como **`crud_gui.py`**:

```python
import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

# -------------------------
# Conexión a SQL Server
# -------------------------
def conectar():
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"  # Ajusta tu instancia aquí
        "DATABASE=PruebaPython;"
        "UID=sa;"
        "PWD=TuPasswordAqui;"
    )
    return conexion

# -------------------------
# Funciones CRUD
# -------------------------
def listar_usuarios():
    for row in tabla.get_children():
        tabla.delete(row)

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    for u in cursor.fetchall():
        tabla.insert("", "end", values=u)
    conexion.close()

def insertar_usuario():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    email = entry_email.get()

    if not nombre or not edad or not email:
        messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")
        return

    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO Usuarios (nombre, edad, email) VALUES (?, ?, ?)", 
                       (nombre, int(edad), email))
        conexion.commit()
        messagebox.showinfo("Éxito", f"Usuario {nombre} agregado correctamente.")
        listar_usuarios()
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conexion.close()

def eliminar_usuario():
    seleccionado = tabla.focus()
    if not seleccionado:
        messagebox.showwarning("Selección", "Seleccione un usuario para eliminar.")
        return

    datos = tabla.item(seleccionado)["values"]
    id_usuario = datos[0]

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE id=?", (id_usuario,))
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Éxito", f"Usuario con ID {id_usuario} eliminado.")
    listar_usuarios()

def actualizar_usuario():
    seleccionado = tabla.focus()
    if not seleccionado:
        messagebox.showwarning("Selección", "Seleccione un usuario para actualizar.")
        return

    datos = tabla.item(seleccionado)["values"]
    id_usuario = datos[0]

    nombre = entry_nombre.get() or datos[1]
    edad = entry_edad.get() or datos[2]
    email = entry_email.get() or datos[3]

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE Usuarios SET nombre=?, edad=?, email=? WHERE id=?",
                   (nombre, int(edad), email, id_usuario))
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Éxito", f"Usuario con ID {id_usuario} actualizado.")
    listar_usuarios()

# -------------------------
# Interfaz gráfica (Tkinter)
# -------------------------
ventana = tk.Tk()
ventana.title("CRUD Usuarios - Python + SQL Server")
ventana.geometry("650x400")
ventana.config(bg="#f4f6f9")

# Frame de formulario
frame_form = tk.Frame(ventana, bg="#ffffff", padx=10, pady=10, relief="ridge", borderwidth=2)
frame_form.pack(side="top", fill="x", pady=10, padx=10)

tk.Label(frame_form, text="Nombre:", bg="#ffffff").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nombre = tk.Entry(frame_form, width=30)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Edad:", bg="#ffffff").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_edad = tk.Entry(frame_form, width=30)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Email:", bg="#ffffff").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_email = tk.Entry(frame_form, width=30)
entry_email.grid(row=2, column=1, padx=5, pady=5)

# Botones
btn_agregar = tk.Button(frame_form, text="Agregar", bg="#28a745", fg="white", command=insertar_usuario)
btn_agregar.grid(row=0, column=2, padx=10)

btn_actualizar = tk.Button(frame_form, text="Actualizar", bg="#ffc107", fg="black", command=actualizar_usuario)
btn_actualizar.grid(row=1, column=2, padx=10)

btn_eliminar = tk.Button(frame_form, text="Eliminar", bg="#dc3545", fg="white", command=eliminar_usuario)
btn_eliminar.grid(row=2, column=2, padx=10)

# Tabla de usuarios
frame_tabla = tk.Frame(ventana)
frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

columnas = ("ID", "Nombre", "Edad", "Email")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=150)

tabla.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Cargar datos al inicio
listar_usuarios()

ventana.mainloop()
📌 Características
Interfaz en ventana con Tkinter.

Botones para Agregar, Actualizar y Eliminar usuarios.
Los usuarios se muestran en una tabla con scroll.
Campos de texto para introducir datos.
Colores suaves para hacerlo más agradable a la vista.

📌 Ejecución
Guarda el archivo como crud_gui.py.

Ejecuta en la terminal:
python crud_gui.py
