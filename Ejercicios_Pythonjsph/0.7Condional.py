"""Conversión de temperaturas. Crear un menú de opciones. """


def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def main():
    while True:
        print("\nMenú de Opciones:")
        print("1. Convertir de Celsius a Fahrenheit")
        print("2. Convertir de Fahrenheit a Celsius")
        print("3. Salir")

        opcion = input("Ingresa el número de la opción deseada: ")

        if opcion == "1":
            celsius = float(input("Ingresa la temperatura en grados Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")
        elif opcion == "2":
            fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit} grados Fahrenheit equivalen a {celsius} grados Celsius.")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()
