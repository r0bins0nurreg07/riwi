"""Como profesor, quiero una función promedio_notas() que reciba tres notas y calcule el promedio.
Si el promedio es mayor o igual a 3.0 → mostrar “Aprobado”, de lo contrario “Reprobado”.
Debe repetirse para varios estudiantes usando un while."""





import statistics


def promedio_notas():
    notas=0
    resultado=[]
    promedio=0

    while notas!=3:
        for i in range(3):
            notas=float(input("Ingrese la nota ---->"))
            resultado.append(notas)
            notas+=1

        promedio_notas=sum(resultado)/len(resultado)


        if promedio_notas>3:
            print(f"Aprobado {promedio_notas}")

        else:
            print(f"Reprobado {promedio_notas}")

promedio_notas()



