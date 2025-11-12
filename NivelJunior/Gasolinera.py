"""Como operador, quiero usar un while que sume litros hasta superar 100.
Cada vez que se venda una cantidad, verificar:

Si el total aún es menor que 100 → mostrar “Sigue vendiendo”.
Si llega o supera 100 → mostrar “Meta diaria alcanzada”."""


litros=0



while litros<100:
    venta= int(input("Cantidad vendida--->"))
    if venta <=100:
        litros+=venta
        print(f"Sigue vendiendo” {litros}")
        
    else:
        litros+=venta

print(f"Meta diaria alcanzada” {litros}")

        
    
        





