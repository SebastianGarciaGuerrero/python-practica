from db_connection import get_connection

def agregar_pacientes(ID, Nombre, Edad, Genero, HistorialMedico, Contacto):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO clinica ((ID, Nombre, Edad, Genero, HistorialMedico, Contacto) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id, Nombre, Edad, Genero, HistorialMedico, Contacto))
        conn.commit()
        conn.close()

def obtener_pacientes():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clinica")
        return cursor.fetchall()

