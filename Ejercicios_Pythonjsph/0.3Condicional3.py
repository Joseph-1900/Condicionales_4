"""Solicitar número al usuario y determinar si es negativo, positivo o cero"""

numero = float(input("Ingresa un número: "))
if numero == 0:
    print("El número es igual a cero.")
elif numero > 0:
    print("El número es positivo.")
else:
    print("El número es negativo.")
