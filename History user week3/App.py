import os
from Servicios import *
from archivos import *



def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_menu():
    print("="*50)
    print("                  INVENTARIO")
    print("="*50)
    print("1.Agregar\n2.Mostrar\n3.Buscar\n4.Actualizar\n5.Eliminar\n6.Estadísticas\n7.Guardar CSV\n8.Cargar CSV\n9.Salir")
    print("="*50)

checkout=True


while checkout:
    mostrar_menu()
    try:
        opcion=int(input("Ingrese la opción que desea realizar "))
    except ValueError:
        print("Ingrese una opción validad")

    if opcion==1:
        agregar_productos()

    elif opcion==2:
        mostrar_inventario()

    elif opcion==3:
        buscar_producto()

    elif opcion==4:
        actulizar_producto()

    elif opcion==5:
        eliminar_producto()

    elif opcion==6:
        calcular_estadistica()

    elif opcion==7:
        
        guardarcsv()
        
    elif opcion==8:
        cargarcsv()

    elif opcion==9:
        break
    else:
        print("opcion no validad, intente nuevamente")
    input("\n Presione ENTER para continuar ")
    limpiar()

    


