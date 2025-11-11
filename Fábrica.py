"""Como supervisor, quiero que un for muestre los productos fabricados del 1 al número que indique el usuario.
Si el número es par, mostrar “Producto verificado”.
Si es impar, mostrar “Producto pendiente”."""

numero=int(input("Numero de productos--->"))

for i in range(numero):
    if i %2 ==0:
        print(f"Numero par {i}")

    else:
        print(f"Numero inpar {i}")
    
