#Controla las entradas por teclado (Errores)
try:
    #Ingresa el nomnre 
    nombre= input("Ingrese el nombre--->")
    #Ingresa  el precio del producto por teclado 
    precio=float(input("Ingrese el precio del producto--->"))
    #Ingresa la cantidad del producto por teclado 
    cantidad=int(input("Ingresa la cantidad del producto--->"))

    #Calcula el costo total multiplicando (precio por cantidad )
    costo_total=(precio*cantidad)


    #Muesrea por pantalla Nombre del producto|Precio unitario| Cantida|Costo total
    print(f"Nombre del producto: {nombre} \nPrecio unitario {precio} \nCantidad {cantidad} \nCosto total {costo_total}")

except:
    print("Erros al ingresar la información ")


#Al usuario ingresar por teclado: nombre del producto, precio y cantidad. El sistema inmediatamente calcula 
#el costo total de los productos ingresados y de igual manera los muestra por pantalla 

