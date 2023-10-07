"""Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir el resultado."""


numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))


if numero1 > numero2:
    mayor = numero1
    menor = numero2
elif numero2 > numero1:
    mayor = numero2
    menor = numero1
else:
    print("Ambos números son iguales.")
   
if 'mayor' in locals() and 'menor' in locals():
    print(f"El número mayor es {mayor}.")
    print(f"El número menor es {menor}.")
