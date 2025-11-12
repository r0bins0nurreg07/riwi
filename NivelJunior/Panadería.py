"""Como panadero, quiero usar un for del 1 al 12.
Si el número es 6, mostrar “Mitad de la producción completada”.
Si es 12, mostrar “¡Día finalizado!”."""


for i in range(1,12+1):
    if i==6:
        print(f"“Mitad de la producción completada {i}”")

    if i ==12:
        print(f"¡Día finalizado! {i}")

    else:
        print(f"Numero {i}")

    