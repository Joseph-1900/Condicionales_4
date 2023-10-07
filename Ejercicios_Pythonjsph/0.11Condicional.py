"""11. El precio que debe pagar un cliente por una pizza depende del tamaño seleccionado, como se muestra a continuación:
    
    
    | Tamaño | Precio |
    | --- | --- |
    | 1 | $15.000 |
    | 2 | $24.000 |
    | 3 | $36.000 |
    
Si cada ingrediente adicional cuesta $4.000. Escribir un programa que solicite al empleado 
encargado de registrar las ventas, el tamaño de la pizza y el número de ingredientes adicionales y muestre al cliente 
el precio que debe pagar."""

precio_tamanos = {1: 15000, 2: 24000, 3: 36000}
precio_ingrediente_adicional = 4000


tamaño_pizza = int(input("Ingresa el tamaño de la pizza (1, 2 o 3): "))
ingredientes_adicionales = int(input("Ingresa el número de ingredientes adicionales: "))


if tamaño_pizza not in precio_tamanos:
    print("Tamaño de pizza no válido. Debes elegir 1, 2 o 3.")
else:
    
    precio_base = precio_tamanos[tamaño_pizza]
    
    
    costo_ingredientes = ingredientes_adicionales * precio_ingrediente_adicional
    
    
    precio_total = precio_base + costo_ingredientes
    print(f"El precio de la pizza es ${precio_total}.")
