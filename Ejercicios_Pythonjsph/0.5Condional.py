"""Solicitar notas de 0.0 a 5.0 a un estudiante y calcular promedio. 
Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar 
"No aprobó" si su nota es menor a 3.0. """


nota1 = float(input("Ingresa la primera nota (0.0 - 5.0): "))
nota2 = float(input("Ingresa la segunda nota (0.0 - 5.0): "))
nota3 = float(input("Ingresa la tercera nota (0.0 - 5.0): "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 3.0:
    print(f"El promedio es {promedio:.2f}, ¡Aprobado!")
else:
    print(f"El promedio es {promedio:.2f}, No aprobado.")


