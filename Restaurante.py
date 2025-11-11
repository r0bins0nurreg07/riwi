"""Como jefe de cocina, quiero usar un for para repetir 3 veces el mensaje “Limpia tu estación”.
Si es la última vez, mostrar “¡Revisión completada!”."""


for i in range(3):
    if i==2:
        print("¡Revisión completada!")
    else:
        print(f"Limpia tu estación {i+1}")