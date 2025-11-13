"""Como panadero, quiero una función hornear_pan(lotes) que use un for para indicar qué lote se está horneando.
Si el lote es divisible por 3, mostrar “Verificación de calidad”.
Al final, mostrar “Producción terminada”."""


def hornear_pan(verificacion):
    for lote in range(1,verificacion+1):
        print(f"Horneando pan {lote}")
        if lote %3==0:
            print(f"Verificación de calidad ")

        else:
            print(f"Producto terminado ")


       
            


hornear_pan(13)


        
        