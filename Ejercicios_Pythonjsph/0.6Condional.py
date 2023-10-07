"""Crear un programa con un menú de opciones, que permita calcular las 
áreas de figuras geométricas (cuadrado, rectángulo, triángulo, círculo, rombo y trapecio)."""

import math

def area_cuadrado(lado):
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi * (radio ** 2)

def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) * altura) / 2

def main():
    while True:
        print("\nMenú de Opciones:")
        print("1. Calcular área del cuadrado")
        print("2. Calcular área del rectángulo")
        print("3. Calcular área del triángulo")
        print("4. Calcular área del círculo")
        print("5. Calcular área del rombo")
        print("6. Calcular área del trapecio")
        print("7. Salir")

        opcion = input("Ingresa el número de la opción deseada: ")

        if opcion == "1":
            lado = float(input("Ingresa la longitud del lado del cuadrado: "))
            print(f"El área del cuadrado es: {area_cuadrado(lado)}")
        elif opcion == "2":
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            print(f"El área del rectángulo es: {area_rectangulo(base, altura)}")
        elif opcion == "3":
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            print(f"El área del triángulo es: {area_triangulo(base, altura)}")
        elif opcion == "4":
            radio = float(input("Ingresa el radio del círculo: "))
            print(f"El área del círculo es: {area_circulo(radio)}")
        elif opcion == "5":
            diagonal_mayor = float(input("Ingresa la longitud de la diagonal mayor del rombo: "))
            diagonal_menor = float(input("Ingresa la longitud de la diagonal menor del rombo: "))
            print(f"El área del rombo es: {area_rombo(diagonal_mayor, diagonal_menor)}")
        elif opcion == "6":
            base_mayor = float(input("Ingresa la longitud de la base mayor del trapecio: "))
            base_menor = float(input("Ingresa la longitud de la base menor del trapecio: "))
            altura = float(input("Ingresa la altura del trapecio: "))
            print(f"El área del trapecio es: {area_trapecio(base_mayor, base_menor, altura)}")
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()


