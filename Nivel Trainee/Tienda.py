"""Como vendedor, quiero una función aplicar_descuentos() que pida varios precios hasta que el usuario escriba 0.
Si el precio supera 50.000, aplicar 10% de descuento.
Al final, mostrar la suma total de las compras con descuento."""


def aplicar_descuentos():
    total=0
    precio= int(input("Ingresa el precio del priducto--->"))

    while precio!=0:

        if precio>50000:
            Precio_descuento= (precio)-((precio)*(10/100))
            total+=Precio_descuento

        else:
            total+=precio
        precio= int(input("Ingresa el precio del priducto--->"))

    
    return total

print (f"Suma total de las compras $ {aplicar_descuentos()}")





