"""Como cajero, quiero pedir montos de venta hasta que el usuario escriba 0.
Si la venta supera $100,000, mostrar “Venta destacada”.
Al final, mostrar el total vendido."""

total_vendido=0
montos=int(input("Ingresa el monto de venta--->"))

while montos!=0:
    if montos>=100:
        print ("Venta destacada")
        total_vendido+=montos

    else:
         total_vendido+=montos


    montos=int(input("Ingresa el monto de venta--->"))


print(f"Total vendido {total_vendido}")


    

    

