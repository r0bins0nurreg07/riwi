"""Como vigilante, quiero usar un while que cuente vehículos hasta llegar a 20.
Si entra un número par, mostrar “Vehículo par registrado”.
Si el total llega a 20, mostrar “Capacidad completa”."""

vehiculos=0
activar=True

while vehiculos<20:
    vehiculos+=1
    if vehiculos %2==0:
        print(f"Vehículo par registrado ->{vehiculos}")
        
    
    else:
       print(f"Numero --->{vehiculos}")
       print("Capacidad completa")
    
     




   

    


