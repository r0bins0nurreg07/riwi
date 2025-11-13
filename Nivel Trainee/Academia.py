"""Como estudiante, quiero una función tabla_multiplicar(numero) que use un for para mostrar la tabla del número dado hasta el 10.
Si el resultado es mayor de 50, mostrar también “Resultado alto”."""



def tabla_multiplicar(numero):
    for calcular in range(numero+1):
        tabla= numero*calcular
        if tabla>50:
            print(f"Resultado alto {tabla}")

        else:
            print(f"Numero {tabla}")


print(tabla_multiplicar (10))