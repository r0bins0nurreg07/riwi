
inventario=[]
def agregar_producto():
    nombre=input("Ingrese el nombre --->")
    precio=float(input("Ingrese el precio--->"))
    cantidad=int(input("Ingrese la cantidiad--->"))
    

    sub_producto={"Nombre": nombre, "Precio":precio,"Cantidad":cantidad}
    inventario.append(sub_producto)

    return inventario

def mostrar_inventario():
    for mostrar in inventario:
        lista= (f"Nombre: {mostrar["Nombre"]} Precio: {mostrar["Precio"]} Cantidad: {mostrar["Cantidad"]} ")
        print(lista)
    
def calcular_estadistica(inventario):
    total=0

    for calcular in inventario:
        total+= calcular["Precio"]* calcular["Cantidad"]
    return total


try:
   
    check=True
    while check:
            print("<------Bienvenidos a inventario--->")
            print("Agregar producto(1)\n Mostrar inventario(2)\n Calcular estadísticas(3)\n Salir (4)")
            opcion=int(input("Ingrese la opcion que desea realizar--->"))

            if opcion==1:
                agregar_producto()
                
            elif opcion==2:
                mostrar_inventario()

            elif opcion==3:
                print(calcular_estadistica(inventario))

            elif opcion==4:
                break

            else:
                print("Error al ingresar ")
                       

except:
     print("SOlo se permite las opcinones parametrizadas ")

    



 



   
