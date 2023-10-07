"""14. El número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico se calcula con la fórmula:
    
    Género femenino (1): número de pulsaciones = (220 - edad en años)/10
    
    Género masculino (2): número de pulsaciones = (210 - edad en años)/10
    
    Lea la edad y el género y muestre el número de pulsaciones."""
    

peso = float(input("Ingresa tu peso en Kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))
imc = peso / (estatura ** 2)

if imc < 18.5:
    estado = "Desnutrido"
elif 18.5 <= imc < 25:
    estado = "Normal"
elif 25 <= imc < 30:
    estado = "Sobrepeso"
elif 30 <= imc < 35:
    estado = "Obesidad Grado 1"
elif 35 <= imc < 40:
    estado = "Obesidad Grado 2"
else:
    estado = "Obesidad Grado 3"


print(f"Tu IMC es: {imc:.2f}")
print(f"Tu estado de salud es: {estado}")
