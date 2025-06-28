# Ejemplo 1: Calcular precio con impuesto
def calcular_precio(producto, precio_base, impuesto):
    precio_total = precio_base * (1 + impuesto)
    print(f"El precio a pagar por {producto} es: ${precio_total:.2f}")

# Datos del producto y precio base
nombre_producto = "Computadora"
precio_producto = 800  # Precio base en dólares
impuesto_producto = 0.15  # Impuesto del 15%

# Llamada a la función
calcular_precio(nombre_producto, precio_producto, impuesto_producto)

# Ejemplo 2: Promedio de calificaciones y área de triángulo
import math

# Función para calcular el promedio de tres calificaciones de ‘n’ estudiantes
def calcular_promedio_calificaciones(n):
    for i in range(n):
        print(f"\nEstudiante {i + 1}:")
        calif1 = float(input("Ingrese la primera calificación: "))
        calif2 = float(input("Ingrese la segunda calificación: "))
        calif3 = float(input("Ingrese la tercera calificación: "))
        promedio = (calif1 + calif2 + calif3) / 3
        print(f"El promedio del estudiante {i + 1} es: {promedio:.2f}")

# Función para calcular el área de un triángulo dados su base y altura
def calcular_area_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area:.2f}")

# Menú de operaciones
while True:
    print("\nMenú:")
    print("1. Calcular promedio de calificaciones de estudiantes")
    print("2. Calcular área de un triángulo")
    print("3. Salir")

    opcion = input("Seleccione una opción (1, 2 o 3): ")

    if opcion == '1':
        cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
        calcular_promedio_calificaciones(cantidad_estudiantes)
    elif opcion == '2':
        calcular_area_triangulo()
    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
