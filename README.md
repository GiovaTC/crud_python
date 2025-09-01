# CRUD en Python conectado a SQL Server usando la librería `pyodbc`

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
