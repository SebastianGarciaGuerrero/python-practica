import json
import os

# Archivos
AUTORES_FILE = "autores.json"
LIBROS_FILE = "libros.json"

# Función para cargar datos
def cargar_datos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w") as f:
            json.dump([], f)
    with open(nombre_archivo, "r") as f:
        return json.load(f)

# Función para guardar datos
def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w") as f:
        json.dump(datos, f, indent=4)

# Agregar autor
def agregar_autor():
    nombre = input("Nombre del autor: ")
    nacionalidad = input("Nacionalidad del autor: ")
    autores = cargar_datos(AUTORES_FILE)
    autores.append({"nombre": nombre, "nacionalidad": nacionalidad})
    guardar_datos(AUTORES_FILE, autores)
    print("Autor agregado exitosamente.\n")

# Agregar libro
def agregar_libro():
    titulo = input("Título del libro: ")
    genero = input("Género del libro: ")
    anio = input("Año de publicación: ")
    autor = input("Nombre del autor: ")
    libros = cargar_datos(LIBROS_FILE)
    libros.append({"titulo": titulo, "genero": genero, "anio": anio, "autor": autor})
    guardar_datos(LIBROS_FILE, libros)
    print("Libro agregado exitosamente.\n")

# Mostrar datos
def mostrar_datos():
    print("Autores:")
    autores = cargar_datos(AUTORES_FILE)
    print(json.dumps(autores, indent=4, ensure_ascii=False))
    print("\nLibros:")
    libros = cargar_datos(LIBROS_FILE)
    print(json.dumps(libros, indent=4, ensure_ascii=False))
    print()

# Menú principal
def main():
    while True:
        print("1. Agregar autor")
        print("2. Agregar libro")
        print("3. Mostrar información")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_autor()
        elif opcion == "2":
            agregar_libro()
        elif opcion == "3":
            mostrar_datos()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.\n")

if __name__ == "__main__":
    main()
