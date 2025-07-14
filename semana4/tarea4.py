# Conjuntos vacíos para cada sala
sala1 = set()
sala2 = set()
sala3 = set()

# Función para ingresar visitantes por sala
def ingresar_visitantes(sala, numero_sala):
    print(f"\nIngrese los nombres de los visitantes de la Sala {numero_sala} (escriba 'fin' para terminar):")
    while True:
        nombre = input("Nombre: ").strip()
        if nombre.lower() == 'fin':
            break
        elif nombre:  # Evita agregar nombres vacíos
            sala.add(nombre)

# Ingreso de datos
ingresar_visitantes(sala1, 1)
ingresar_visitantes(sala2, 2)
ingresar_visitantes(sala3, 3)

# Unión de los visitantes de todas las salas
visitantes_totales = sala1.union(sala2).union(sala3)

# Mostrar la lista única
print("\nLista Única de Visitantes:")
for visitante in visitantes_totales:
    print(visitante)
