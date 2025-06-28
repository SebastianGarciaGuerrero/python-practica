# Programa para verificar tipos de datos en Python


# Solicitar valores al usuario

varEntero = int(input("Escriba un valor entero corto: "))

varLargo = int(input("Escriba un valor entero largo: "))

varReal = float(input("Escriba un valor con decimales: "))

varComplejo = complex(input("Escriba un valor complejo (a+bj): "))

varCadena = input("Escriba una cadena: ")

varBooleano = input("Escriba un valor booleano (True/False): ")



# Convertir a tipo booleano si es posible

if varBooleano.lower() == 'true':

    varBooleano = True

else:

    varBooleano = False



# Mostrar los valores ingresados junto con su tipo de dato en Python

print("\n\nA continuación se muestran los valores leídos y su tipo en Python:")

print(varEntero, type(varEntero))

print(varLargo, type(varLargo))

print(varReal, type(varReal))

print(varComplejo, type(varComplejo))

print(varCadena, type(varCadena))

print(varBooleano, type(varBooleano))