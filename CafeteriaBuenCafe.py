"""1. Cafetería “Buen Café”  Control de tazas servidas
Como barista, quiero usar un bucle for para mostrar cuántas
 tazas he servido del 1 al 10, pero si el número es 5, mostrar el mensaje “¡Mitad del turno completada!”."""


barrista=4

for i in range(0,10):
   print(f"Tazas servidas {i+1}")
   if i==barrista:
      print(f"Mitad del turno completada! ")
    
