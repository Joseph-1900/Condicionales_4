"""Preguntar al usuario el nombre y la edad, si es mayor o igual a 18 años mostrar el mensaje 
"Usted es mayor de edad", de lo contrario "Usted es menor de edad". Si el número ingresado es negativo 
o la edad ingresada es mayor a 100 años, mostrar al usuario un mensaje de ingresar una edad válida."""



nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))


if edad < 0 or edad > 100:
    print("Por favor, ingresa una edad válida.")
else:
   
    if edad >= 18:
        print(f"{nombre}, eres mayor de edad.")
    else:
        print(f"{nombre}, eres menor de edad.")

    