# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Ingresa un número entero positivo: "))
# Verificar si el número ingresado es positivo
if numero <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
# Inicializar la variable para almacenar la suma
    suma = 0
# Utilizar un bucle para sumar los números naturales desde 1 hasta el número ingresado
for i in range(1, numero + 1):
    suma += i
# Imprimir el resultado de la suma
print(f"La suma de los números naturales hasta {numero} es: {suma}")