"""Como jefe de equipo, quiero una función evaluar_empleado(nombre, horas) que:

Use un bucle for para simular las horas trabajadas (de 1 hasta horas).
Si la hora es mayor de 8, contar como hora extra.
Al final, calcular el total de horas normales y extras.
Mostrar un resumen del empleado."""


nombre=input("Ingresa el nombre--->")
hora=int(input("Ingresa el total de horas trabajadas-->"))

def evaluar_empleado(nombre, horas):
    if nombre!="" and horas!=0:
        for evaluar in range(horas):
            if horas>8:
                calcular= horas-8
                total_horas=print(f"Haz trabajado 8 horas y {calcular}  extras")
                break

            else:
                total_horas=print(f"Haz trabajado {horas}")
                break
    else:
        print("Error al ingresar la información ")


evaluar_empleado(nombre,hora)



    