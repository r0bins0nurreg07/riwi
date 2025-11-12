"""Como gerente, quiero una función verificarTurno(hora) que determine:

Si la hora es menor que 12 → “Turno de mañana”.
Si está entre 12 y 18 → “Turno de tarde”.
Si es mayor → “Turno de noche”.
El programa principal debe pedir la hora e imprimir el resultado."""

def varificarTurno(hora):
    if hora<12:
        print("Turno Mañana")
    else:
        print("urno de noche")


hora=int(input("Ingresa la hora--->"))

varificarTurno(hora)