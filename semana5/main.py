# archivo: main.py
from datetime import datetime
from empleado import Empleado

# Entrada de datos por el usuario
nombre = input("Ingrese el nombre del empleado: ")
salario = float(input("Ingrese el salario del empleado: "))
anio = int(input("Ingrese el año de ingreso (YYYY): "))
mes = int(input("Ingrese el mes de ingreso (1-12): "))
dia = int(input("Ingrese el día de ingreso (1-31): "))

# Crear objeto del empleado
fecha_ingreso = datetime(anio, mes, dia)
empleado = Empleado(nombre, salario, fecha_ingreso)

# Mostrar resultados
print("\n--- Datos del Empleado ---")
print(f"Empleado: {empleado.nombre}")
print(f"Salario: ${empleado.salario}")
print(f"Antigüedad: {empleado.calcular_antiguedad()} años")

beneficios = empleado.obtener_beneficios()
if beneficios:
    print("Beneficios Asignados:", ", ".join(beneficios))
else:
    print("Beneficios Asignados: Ninguno")
