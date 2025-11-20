inventario=[]

def agregar_productos():
    nombre=input("Ingresa el nombre del producto ")
    precio=float(input("Ingresa el nombre del producto "))
    cantidad=int(input("Ingresa el nombre del producto "))

    producto={"id":len(inventario)+1,"Nombre":nombre, "Precio":precio, "Cantidad":cantidad}
    inventario.append(producto)


def mostrar_inventario():
    if not inventario:
        print("NO hay productos agregados ")

    for buscar in inventario:
        print(f"ID: {buscar["id"]} NOMBRE: {buscar["Nombre"]} PRECIO: {buscar["Precio"]} CANTIDAD: {buscar[ "Cantidad"]}")

def buscar_producto(id):
    for buscar in inventario:
        if buscar["id"]==id:
            print(f"ID: {buscar["id"]} NOMBRE: {buscar["Nombre"]} PRECIO: {buscar["Precio"]} CANTIDAD: {buscar[ "Cantidad"]}")

        else:
            print("No se encontro el producto en el inventario")

def actulizar_producto(id):
    for buscar in inventario:
        if buscar["id"]==id:
            precio=float(input("Ingrese el nuevo precio "))
            cantidad=int(input("Ingrese la nueva cantidad "))

            buscar["Precio"]=precio
            buscar["Cantidad"]=cantidad

        else:
            print("Producto no encontrado")

def eliminar_producto(id):
    if

agregar_productos()
buscar_producto(1)
actulizar_producto(1)
mostrar_inventario()