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
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Usuarios (nombre, edad, email) VALUES (?, ?, ?)",
                    (nombre, edad, email))
    conexion.commit()
    conexion.close()
    print(f"Usuario {nombre} insertado con exito.")

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
        cursor.execute("UPDATE Usuarios SET edad=? WHERE  id=?", (edad, id_usuario))
    if email:
        cursor.execute("UPDATE Usuarios SET email=? WHERE id=?", (email, id_usuario))

    conexion.commit()
    conexion.close()
    print(f"usuario con id {id_usuario} actualizado .")

# DELETE