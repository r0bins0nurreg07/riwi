"""Como proyeccionista, quiero mostrar una cuenta regresiva del 5 al 1 usando for. 
Si llega al número 1, debe imprimir “¡Que empiece la función!”."""


for i in range(5,0,-1):
  
    print(f"Cuenta regresiva en {i}")
    if i==1:
        print("¡Que empiece la función!")