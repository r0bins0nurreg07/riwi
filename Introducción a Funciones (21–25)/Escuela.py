"""Como profesor, quiero crear una función promedioNotas() que reciba tres notas y calcule el promedio.
Si el promedio es mayor o igual a 3.0, mostrar “Aprobado”; si no, “Reprobado”."""


def promedioNOta(nota1,nota2,nota3):
    promedio=((nota1+nota2+nota3)/3)
    return promedio

total= promedioNOta(50,60,10)

if total>=30:
    print(f"Aprobado {total}")


else:
     print(f"Reprobado {total}")


