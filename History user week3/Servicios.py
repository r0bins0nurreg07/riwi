import archivos
inventario=[]

def agregar_productos():
    while True:
        try:
            nombre=input("Ingresa el nombre del producto ").strip()
            if not nombre:
                print("Debe ingresar información ")
                continue

            precio=float(input("Ingresa el precio del producto "))
            cantidad=int(input("Ingresa el cantidad del producto "))
            break
        except ValueError:
            print("\nError a ingresar la información")
    for i in inventario:
        if i ["Nombre"]==nombre:
            print("Usuario ya existente ")
            return
        

    producto={"id":len(inventario)+1,"Nombre":nombre, "Precio":precio, "Cantidad":cantidad}
    inventario.append(producto)


def mostrar_inventario():
    if not inventario:
        print("NO hay productos agregados ")

    for buscar in inventario:
        print(f"ID: {buscar["id"]} NOMBRE: {buscar["Nombre"]} PRECIO: {buscar["Precio"]} CANTIDAD: {buscar[ "Cantidad"]}")

def buscar_producto():
    while True:
        try: 
            id=int(input("Ingrese el codigo de producto"))
            if id<=0:
                print("El ID debe ser numerico")
                continue
            else:
                print("Producto encontrado")
                break
        except ValueError:
            print(F"Error al ingresar la información \n")

    localitation=False
    
    for buscar in inventario:
        if buscar["id"]==id:
            print(f"ID: {buscar["id"]} NOMBRE: {buscar["Nombre"]} PRECIO: {buscar["Precio"]} CANTIDAD: {buscar[ "Cantidad"]}")
            localitation=True
    if localitation==False:
        print("No se encontro el producto en el inventario")
            

def actulizar_producto():
    while True:
        try: 
            id=int(input("Ingrese el codigo de producto"))
            if id<=0:
                print("El ID debe ser numerico")
                continue
            else:
                print("Producto encontrado")
                break
        except ValueError:
            print(F"Error al ingresar la información \n")


    for buscar in inventario:
        localizar=False
        if buscar["id"]==id:
            precio=float(input("Ingrese el nuevo precio "))
            cantidad=int(input("Ingrese la nueva cantidad "))

            buscar["Precio"]=precio
            buscar["Cantidad"]=cantidad
            print("Actualizado correctamente")
            localizar=True

    if localizar==False:
            print("Producto no encontrado")

def eliminar_producto():
    while True:
        try: 
            id=int(input("Ingrese el codigo de producto"))
            if id<=0:
                print("El ID debe ser numerico")
                continue
            else:
                print("Producto encontrado")
                break
        except ValueError:
            print(F"Error al ingresar la información \n")


    if not inventario:
        print("No hay producto registrados ")

    for e,est in enumerate(inventario):
        if est["id"]==id:
            inventario.pop(e)
            print("Producto eliminada ")
            return
        print("No se encontro el ID indicado ")

def calcular_estadistica():
    for i in inventario:
        unidad_total= sum(i["Cantidad"]for i in inventario)
        valor_total=sum(i["Cantidad"]*i["Precio"] for i in inventario)
        producto_max= max(inventario,key=lambda p:p["Precio"])
        producto_stock=max(inventario,key=lambda p:p["Cantidad"])
        return print(f"Unidad Total: {unidad_total}\nValor Total: {valor_total}\nProducto más caro: {producto_max}\nProducto mayor stock: {producto_stock}")








