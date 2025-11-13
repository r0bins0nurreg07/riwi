"""Como cajero, quiero una función calcular_entradas() que pida edades de los clientes hasta que se ingrese 0.
Aplicar precio:
####
Menores de 12 → $5.000
De 12 a 59 → $8.000
Mayores de 60 → $4.000
Usar un while y condiciones."""



def calcular_entradas():
    precio=0
    edad=int(input("Ingrese tu edad--->"))
    while edad!=0:

        if edad<12:
            precio+=5000

        elif 12<=edad<=59: 
            precio+=8000

        else:
             precio+=4000
        edad=int(input("Ingrese tu edad--->"))

    print(f"Precio total $ {precio}")

    


calcular_entradas()



