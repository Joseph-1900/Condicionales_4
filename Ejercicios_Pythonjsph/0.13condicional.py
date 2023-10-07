"""Un reporte de salud muestra una tabla diferente del índice de masa corporal 
IMC de una persona que se calcula con la fórmula IMC=P/(E*E) en donde P es el peso en Kg. 
y E es la estatura en metros. Lea un valor de P y de E, calcule el IMC y muestre su estado 
según la siguiente tabla:"""

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
