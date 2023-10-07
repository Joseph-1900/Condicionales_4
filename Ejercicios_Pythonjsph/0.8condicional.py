"""Solicitar tres números al usuario e imprimirlos en orden ascendente y descendente. """

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

numeros = [numero1, numero2, numero3]

ascendente = sorted(numeros)

descendente = sorted(numeros, reverse=True)
print("Números en orden ascendente:", ascendente)
print("Números en orden descendente:", descendente)

