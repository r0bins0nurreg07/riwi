"""Como conductor, quiero una función simular_viaje(pasajeros) que recorra con un for cada pasajero y muestre “Pasajero X a bordo”.
Si llega a 10 pasajeros, mostrar “Bus lleno” y detener el bucle."""

def simular_viaje(pasajeros):
    for contar in range(1,pasajeros):
        if contar==10:
            print(F"Bus lleno con el pasajero {contar}")
            break

        else:
            print(f"Pasajero numero {contar}")



simular_viaje(12)
