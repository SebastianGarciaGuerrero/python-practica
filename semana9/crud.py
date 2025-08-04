from db_connection import get_connection

def agregar_pacientes(ID, Nombre, Edad, Genero, HistorialMedico, Contacto):
    try:
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO Pacientes (ID, Nombre, Edad, Genero, HistorialMedico, Contacto)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (ID, Nombre, Edad, Genero, HistorialMedico, Contacto))
            conn.commit()
            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Error al agregar paciente: {e}")

def obtener_pacientes():
    try:
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Pacientes")
            pacientes = cursor.fetchall()
            cursor.close()
            conn.close()
            return pacientes
    except Exception as e:
        print(f"Error al obtener pacientes: {e}")
        return []

def eliminar_paciente(ID):
    try:
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Pacientes WHERE ID = %s", (ID,))
            conn.commit()
            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Error al eliminar paciente: {e}")

def actualizar_paciente(ID, Nombre, Edad, Genero, HistorialMedico, Contacto):
    try:
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            query = """
                UPDATE Pacientes
                SET Nombre = %s, Edad = %s, Genero = %s, HistorialMedico = %s, Contacto = %s
                WHERE ID = %s
            """
            cursor.execute(query, (Nombre, Edad, Genero, HistorialMedico, Contacto, ID))
            conn.commit()
            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Error al actualizar paciente: {e}")
