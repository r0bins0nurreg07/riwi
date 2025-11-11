"""Como profesor, quiero usar un while que sume tareas hasta 10. Si el contador llega a 10, mostrar “¡Todas las tareas recibidas!”.
 Si aún no llega, mostrar cuántas faltan."""
contador=1
tareas1=10
tareas=[]
while contador<tareas1:
    print(f"Faltan  {tareas1-contador} tareas ")

    notas= contador
    tareas.append(notas)

    contador+=1

print(F"Tareas recibidad {tareas}")