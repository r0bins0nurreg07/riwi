"""Como deportista, quiero ingresar un número de repeticiones y usar un for para imprimir “Repetición X completada”.
Si X es divisible por 3, mostrar además “¡Excelente ritmo!”."""

repeticiones=int(input("Numero de repeticiones-->"))
for i in range(repeticiones):
    if i %3==0:
        print(f"¡Excelente ritmo! {i}")
    else:
        print(f"Repetición {i} completada")