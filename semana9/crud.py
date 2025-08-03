from db_connection import get_connection

def agregar_pacientes(ID, Nombre, Edad, Genero, HistorialMedico, Contacto):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO Pacientes ((ID, Nombre, Edad, Genero, HistorialMedico, Contacto) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id, Nombre, Edad, Genero, HistorialMedico, Contacto))
        conn.commit()
        conn.close()

def obtener_pacientes():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pacientes")
        return cursor.fetchall()

def eliminar_pacientes(id):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Pacientes WHERE ID = %s", (id,))
        conn.commit()
        conn.close()

def actualizar_pacientes(id, Nombre, Edad, Genero, HistorialMedico, Contacto):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE Pacientes SET Nombre=%s, Edad=%s, Genero=%s, HistorialMedico=%s, Contacto=%s WHERE ID=%s"
        cursor.execute(query, (Nombre, Edad, Genero, HistorialMedico, Contacto, id))
        conn.commit()
        conn.close()

def obtener_pacientes():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pacientes")
        return cursor.fetchall()
    else:
        return []

