import pyodbc

def conectar():
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=GTAPIERO-POLI;" # Cambia por tu servidor, ej: "localhost\\SQLEXPRESS"
        "DATABASE=PruebaPython;"
        "UID=sa;"
        "PWD=tapiero;"
    )
    return conexion

#------------------------
# CRUD
#------------------------

# CREATE
def insertar_usuario(nombre, edad, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Usuarios (nombre, edad, email) VALUES (?, ?, ?)", (nombre, edad, email))
    conn.commit()
    conn.close()

def obtener_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, edad, email FROM Usuarios")
    rows = cursor.fetchall()
    conn.close()
    return rows

def actualizar_usuario(id_usuario, nombre, edad, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Usuarios SET nombre=?, edad=?, email=? WHERE id=?", (nombre, edad, email, id_usuario))
    conn.commit()
    conn.close()

def eliminar_usuario(id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE id=?", (id_usuario,))
    conn.commit()
    conn.close()