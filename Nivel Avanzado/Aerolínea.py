"""Como viajero frecuente, quiero una función calcular_millas(viajes) que reciba el número de viajes realizados y sume millas según la distancia:

Viaje corto (< 1000 km): 500 millas
Medio (1000–3000 km): 1000 millas
Largo (> 3000 km): 2000 millas
Debe repetirse hasta que el usuario escriba “fin” y mostrar el total acumulado."""

viajes=input("Kilimetros recorridos--->")

def calcular_millas(viajes):
    ejecutar= True
    acumalada=0
    num_vijaes=1

    while ejecutar:

        if viajes=="fin":
            print(f"Numero de viejes {num_vijaes}\n Total aculado de millas {acumalada}")
            break
                    
        if int(viajes)<1000:
            acumalada+=500
            print(f"Numero de viaje {num_vijaes}\n Viaje corto: 500 millas")
            
            

        elif int(viajes)>=1000 and int(viajes)<=3000:
            acumalada+=1000
            print(f"Numero de viaje {num_vijaes}\n Viaje Medio: 1000 millas")
            
            

        elif int(viajes)>3000:
            acumalada+=2000
            print(f"Numero de viaje {num_vijaes}\n Viaje largo: 2000 millas")
            

        num_vijaes+=1
        viajes=input("Kilimetros recorridos--->")

    return acumalada

        
            
calcular_millas(viajes)

       


        



