"""Como mesero, quiero una función calcular_propina(total_cuenta) que reciba el valor total
 de la cuenta y calcule la propina del 10%.
Si el total es mayor de $100.000, aplicar el 15%.
El programa debe mostrar el total final a pagar."""



def calcular_propina(total_cuenta):

    if total_cuenta<100000:
        total_pagar=(total_cuenta)-((total_cuenta)*(10/100))

    else:
        total_pagar=(total_cuenta)-((total_cuenta)*(15/100))

      

    return total_pagar


valor=int(input("Ingrese el valor a pagar--->"))


print(f"Total a pagar ${calcular_propina(valor)}")




