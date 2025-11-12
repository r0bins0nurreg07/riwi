"""Como usuario, quiero usar un while con máximo 3 intentos de contraseña.
Si acierto, mostrar “Acceso permitido”.
Si agoto los intentos, mostrar “Acceso denegado”."""

contador=1
password="1234"

while contador<=3:
    password1=input("Ingrese contraseña--->")

    if password==password1:
        print("Inicio correcto")
        break   
    else:
        contador+=1

print("Se acabaron los intentos ")
        
        