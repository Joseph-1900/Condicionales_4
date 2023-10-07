"""Leer el número de llantas de una compra y mostrar el valor que debe pagarse. 
El almacén las vende con la siguiente política: Si se compran menos de 6 llantas, 
el precio unitario es $240000. Si se compran 6 o 7, el precio unitario es $221000, 
y si se compran más de 7 llantas, el precio unitario es $180000."""

cantidad_llantas = int(input("Ingrese la cantidad de llantas compradas: "))

precio_unitario1 = 240000  
precio_unitario2 = 221000  
precio_unitario3 = 180000  

if cantidad_llantas < 6:
    valor_total = cantidad_llantas * precio_unitario1
elif 6 <= cantidad_llantas <= 7:
    valor_total = cantidad_llantas * precio_unitario2
else:
    valor_total = cantidad_llantas * precio_unitario3
print(f"El valor total a pagar es: ${valor_total:.2f}")
