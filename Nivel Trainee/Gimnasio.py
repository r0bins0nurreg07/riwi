"""Como entrenador, quiero una función repeticiones(n) que use un bucle for para mostrar las 
repeticiones del 1 al número indicado.
Si el número actual es par, mostrar “Excelente forma”, si no, “Mantén el ritmo”."""


def repeticiones(n):
    for repeticiones in range(1,n+1):
        if repeticiones %2==0:
            print(F"Excelente forma {repeticiones}")

        else:
            print(F"Mantén el ritmo {repeticiones}")

        
    

repeticiones(8)


