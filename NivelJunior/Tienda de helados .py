"""Como empleado, quiero usar un while que cuente clientes hasta que el número supere 15.
Si el número es múltiplo de 5, mostrar “Pausa para limpieza”.
Al final, mostrar “Turno finalizado”."""


clientes=0

while clientes<=15:
    if clientes %5==0:
        print(f"Pausa para limpieza {clientes}")
        clientes+=1

    else:
        print(f"Numero --->{clientes}")
        clientes+=1

print(f"Turno finalizado {clientes}")
