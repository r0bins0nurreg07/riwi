"""Como comprador, quiero una función carrito() que permita ingresar precios de productos y valide:

Si el precio es negativo, mostrar error y pedir otro valor.
Si el precio es mayor a 100.000, aplicar un 20% de descuento.
Usar while y if dentro de la función hasta ingresar 0 para finalizar.
"""


def función_carrito():
    precio=int(input("Ingrese el valor del product--->"))
    valor =0

    while precio!=0:
        if precio<0:
            print("Error al ingresar el valor ")

        if precio>100000:
            precio=(precio)-((precio)*(20/100))
            valor+=precio
        
        else:
            valor+=precio

        precio=int(input("Ingrese el valor del product--->"))

    print(f"Valor total $ {valor}")

función_carrito()
    

        

