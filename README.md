	
# CRUD en Python conectado a SQL Server usando la librería `pyodbc`


<img width="2559" height="1042" alt="image" src="https://github.com/user-attachments/assets/51c95902-7966-44cd-ae19-c9c261baa8a5" />


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

