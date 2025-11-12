"""Como analista financiero, quiero una función calcularInteres() que reciba un monto y una tasa (porcentaje) 
y retorne el valor final después de aplicar el interés una vez.
El programa principal debe pedir los datos y mostrar el resultado."""



def calcularInteres(monto, interes):
    total_pagar=monto+(monto)*(interes/100)

    return total_pagar

print(calcularInteres(4000,5))