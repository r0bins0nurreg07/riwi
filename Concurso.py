"""Como participante, quiero que el programa me pida un número entre 1 y 5 usando un while.
Si acierto, mostrar “¡Correcto!”.
Si no, mostrar “Intenta otra vez” y seguir hasta acertar.
"""

booleano=True
numero_correcto=5
while booleano:
    numero=int(input("Ingresa el numero del 1 al 5--->"))
    if numero_correcto==numero:
        print(f"Correcto! {numero}")
        break

    else: 
        print("Intenta otra vez")