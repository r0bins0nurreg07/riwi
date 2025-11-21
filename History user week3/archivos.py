import os
import csv


def guardarcsv(guardar="guardar.csv"):
    from Servicios import inventario

    os.makedirs("DataBase", exist_ok=True)
    rutacsv=os.path.join("DataBase",guardar)

    with open(rutacsv,"w",newline="",encoding="utf-8") as archivo:
        write=csv.DictWriter(archivo,fieldnames=inventario[0].keys())
        write.writeheader()
        write.writerows(inventario)
        return
    
def cargarcsv(guardar="guardar.csv"):
    from Servicios import inventario

    os.makedirs("DataBase", exist_ok=True)
    rutacsv=os.path.join("DataBase",guardar)

    with open(rutacsv, "r", newline="", encoding="utf-8") as archivo:
        read= csv.DictReader(archivo)
        inventario.clear()
        for fila in read:
            producto = {
                "id": int(fila.get("id")),
                "Nombre": fila.get("Nombre"),
                "Precio": float(fila.get("Precio", 0)),
                "Cantidad": int(fila.get("Cantidad", 0))
            }
            inventario.append(producto)
            print(producto)
        


    

