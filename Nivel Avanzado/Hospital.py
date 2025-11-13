"""Como médico, quiero una función evaluar_paciente() que reciba frecuencia cardiaca y temperatura corporal.
Si ambos valores están fuera del rango normal (FC > 100 o Temp > 38), mostrar “Paciente en observación”.
Repetir el proceso con varios pacientes en un bucle while."""



def evaluar_paciente():
    ejecutador=True
    paciente=1
    fc=int(input("Ingrese la frecuencia cardiaca o el numero cero para salir --->"))
    temp=int(input("Ingrese la temperatura corporal--->"))
    while ejecutador:

        if fc==0:
            break

        if fc>100 and temp>38:
            print(f"Paciente numero {paciente} en observaxion")

        else:
            print(f"Paciente numero {paciente}  estas bien ")

        fc=int(input("Ingrese la frecuencia cardiaca--->"))
        temp=int(input("Ingrese la temperatura corporal"))

evaluar_paciente()




