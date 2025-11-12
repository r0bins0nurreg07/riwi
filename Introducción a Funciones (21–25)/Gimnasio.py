"""Como entrenador, quiero una función calcularEnergia() que reciba un número de repeticiones y devuelva un mensaje:

Si las repeticiones son menores de 5 → “Necesitas más esfuerzo”.
Si son 5 o más → “¡Buen trabajo!”."""


def calcular_energia(numero):
    if numero>5:
        print(f"Buen trabajo {numero}")

    else:
        print(f"Necesitas más esfuerzo {numero}")

     


calcular_energia(4)