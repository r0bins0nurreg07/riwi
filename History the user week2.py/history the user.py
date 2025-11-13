
inventario=[]
def agregar_producto():
    nombre=input("Ingrese el nombre --->")
    precio=int(input("Ingrese el precio--->"))
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


print("<------Bienvenidos a inventario--->")
print("Agregar producto(1)\n Mostrar inventario(2)\n Calcular estadísticas(3)\n Salir (4)")

try:
    opcion=int(input("Ingrese la opcion que desea realizar--->"))

    while opcion!=4:




            if opcion==1:
                agregar_producto()
            elif opcion==2:
                mostrar_inventario()

            elif opcion==3:
                print(calcular_estadistica(inventario))

            else:
                print("Error al ingresar ")
                

            print("Opción no existente ")
            
    opcion=int(input("Ingrese la opcion que desea realizar--->"))

except:
     print("SOlo se permite las opcinones parametrizadas ")

    



 



   
