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

# --------------------------------------- #
# --------------------------------------- #
# --------------------------------------- #

# DELETE    
def  eliminar_usuario(id_usuario):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE id=?", (id_usuario))
    conexion.commit()
    conexion.close()
    print(f"usuario con id {id_usuario} eliminado.")

if __name__ == "__main__":
    # Insertar datos
    insertar_usuario("Juan sonora", 40, "sonora@clr.com.co")
    insertar_usuario("Ana Loceba", 64, "loceba@clr.com.co")

# Listar usuarios 
    print("Usuarios Registrados: ")
    for u in listar_usuarios():
        print(u)

# Actualizar usuarios
    actualizar_usuario(2, nombre="Ana Loceba", edad=94)

# Eliminar usuarios
    eliminar_usuario(1)

# Listar usuario final
    print("\nUsuarios después de cambios: ")
    for u in listar_usuarios():
        print(u)