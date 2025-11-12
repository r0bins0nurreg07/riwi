"""Como cliente, quiero usar un for que sume mi ahorro mensual durante 6 meses.
Si en algún mes el total supera $1,000,000, mostrar “¡Meta alcanzada!”.
Al final, mostrar el total acumulado."""



total=0
meses=6

supera=100


for i  in range(meses):
    subtotal=int (input("Ingrese la cuota --->"))

    if subtotal<=supera :
        
        total+=subtotal
        print(f"Has pagado la cuota {i}\n Total acumulado: $ {total}")

        

    else:
    
        total+=subtotal
        print(f"dffda {total}")
        break

      

   
