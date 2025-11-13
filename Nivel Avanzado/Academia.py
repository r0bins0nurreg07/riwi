"""Como estudiante de programación, quiero una función calcular_factorial(numero) que use un bucle for para calcular el factorial del número.
Si el número ingresado es negativo, mostrar “Número inválido”.
De lo contrario, mostrar el resultado."""


numero=int(input("Ingrese el numero---->"))

def calcular_factorial(numero):

    if numero < 0:
        print("Número inválido")
        return
    
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    
    print(f"El factorial de {numero} es: {factorial}")


calcular_factorial(numero)



