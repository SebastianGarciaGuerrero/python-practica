def calculadora (num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: división por cero no permitida"

numero1 = float(input("ingrese un numero: "))
numero2 = float(input("ingrese el segundo numero: "))
operacion = input("Ingrese el operador (+, -, *, /): ")

resultado = calculadora(numero1, numero2, operacion)
print(f"El resultado de la operación es: {resultado}")
