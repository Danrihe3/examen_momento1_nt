import uuid
import random

idDisponibles=list(range(1,201))

zonaA=[]
zonaB=[]
zonaC=[]
zonaD=[]


opcionUsuario=8

print("Tienda Giks")
print("***********")
print("Inventario")
print("***********")

while opcionUsuario!=6:
    
    print("Menu de opciones")
    print()
    print("1.Registrar productos")
    print("2.Mostrar todos los productos")
    print("3.Buscar un producto")
    print("4.Modificar productos")
    print("5.Eliminar productos")
    print("6.Salir")
    opcionUsuario=input("Digita la opción que deseas realizar: ")
    print()
    while opcionUsuario.isdigit()==False:
        print("Debes ingresar una opción válida")
        opcionUsuario=input("Digita la opción que deseas realizar: ")
        print()
    opcionUsuario= int(opcionUsuario)

    if opcionUsuario == 1:
        for idProducto in idDisponibles:
            idProducto=random.choice(idDisponibles)
              
        producto={}
        producto["id"]=idProducto
        producto["nombre"]=input("Nombre del producto: ").upper()
        producto["precio"]=input("Precio unitario: ")
        while producto["precio"].isdigit()==False:
            print("El precio debe estar en números")
            producto["precio"]=input("Precio unitario: ")
        producto["precio"]=int(producto["precio"])
        producto["zona"]=input("Zona a la que desea ingresar el producto(A,B,C ó D): ").upper()
        while producto["zona"]!="A" and producto["zona"]!= "B" and producto["zona"]!="C" and producto["zona"]!="D":
            print(f'La zona {producto["zona"]} no existe')
            print("Ingresa una opcion válida")
            producto["zona"]=input("Zona a la que desea ingresar el producto(A,B,C ó D): ").upper()
        producto["descripcion"]=input("Descripción del producto: ")
        producto["marca"]=input("Marca o casa del producto: ").upper()
        producto["referencia"]=input("Referencia del producto: ").upper()
        producto["pais"]=input("País de origen del producto: ").upper()
        while producto["pais"].isdigit()==True:
            print("El pais no puede ser o contener números")
            print("Ingresa un país válido")
            producto["pais"]=input("País de origen del producto: ").upper()
        producto["numeroUnidades"]=input("Numero de unidades compradas: ")
        while producto["numeroUnidades"].isdigit()==False:
            print("El número de productos solo puede ser un número")
            producto["numeroUnidades"]=input("Numero de unidades compradas: ")
        producto["numeroUnidades"]=int(producto["numeroUnidades"])
        while producto["numeroUnidades"]>50:
            print("La cantidad de unidades no puede ser mayor a 50")
            producto["numeroUnidades"]=input("Numero de unidades compradas: ")           
        producto["garantia"]=input("Tiene garantía extendida(S/N): ").upper()
        while producto["garantia"].isdigit()==True:
            print(f'La opción {producto["garantia"]} no es válida')
            print("Digita S o N")
        if producto["garantia"]=="S":
            producto["garantia"]=True
        else:
            producto["garantia"]=False

        if producto["zona"]=="A":
            for agregar in range(producto["numeroUnidades"]):
                zonaA.append(producto)
        elif producto["zona"]=="B":
            for agregar in range(producto["numeroUnidades"]):
                zonaB.append(producto)
        elif producto["zona"]=="C":
            for agregar in range(producto["numeroUnidades"]):
                zonaC.append(producto)
        else:
            zonaD.append(producto)
        idDisponibles.remove(idProducto)
        print()

    if opcionUsuario == 2:
        for mostrarZonaA in zonaA:
            print("Zona A")
            print("******")
            print(f'Id: {mostrarZonaA["id"]}')
            print(f'Nombre: {mostrarZonaA["nombre"]}')
            print(f'Precio: {mostrarZonaA["precio"]}')
            print(f'Descripción: {mostrarZonaA["descripcion"]}')
            print(f'Marca: {mostrarZonaA["marca"]}')
            print(f'Referencia: {mostrarZonaA["referencia"]}')
            print(f'Pais: {mostrarZonaA["pais"]}')
            print(f'Numero de Unidades: {mostrarZonaA["numeroUnidades"]}')
            if mostrarZonaA["garantia"]==True:
                print("Garantía extendida: Sí")
            else:
                print("Garantía extendida: No")
            print()
        for mostrarZonaA in zonaB:
            print("Zona B")
            print("******")
            print(f'Id: {mostrarZonaA["id"]}')
            print(f'Nombre: {mostrarZonaA["nombre"]}')
            print(f'Precio: {mostrarZonaA["precio"]}')
            print(f'Descripción: {mostrarZonaA["descripcion"]}')
            print(f'Marca: {mostrarZonaA["marca"]}')
            print(f'Referencia: {mostrarZonaA["referencia"]}')
            print(f'Pais: {mostrarZonaA["pais"]}')
            print(f'Numero de Unidades: {mostrarZonaA["numeroUnidades"]}')
            if mostrarZonaA["garantia"]==True:
                print("Garantía extendida: Sí")
            else:
                print("Garantía extendida: No")
            print()
        for mostrarZonaA in zonaC:
            print("Zona C")
            print("******")
            print(f'Id: {mostrarZonaA["id"]}')
            print(f'Nombre: {mostrarZonaA["nombre"]}')
            print(f'Precio: {mostrarZonaA["precio"]}')
            print(f'Descripción: {mostrarZonaA["descripcion"]}')
            print(f'Marca: {mostrarZonaA["marca"]}')
            print(f'Referencia: {mostrarZonaA["referencia"]}')
            print(f'Pais: {mostrarZonaA["pais"]}')
            print(f'Numero de Unidades: {mostrarZonaA["numeroUnidades"]}')
            if mostrarZonaA["garantia"]==True:
                print("Garantía extendida: Sí")
            else:
                print("Garantía extendida: No")
            print()
        for mostrarZonaA in zonaD:
            print("Zona D")
            print("******")
            print(f'Id: {mostrarZonaA["id"]}')
            print(f'Nombre: {mostrarZonaA["nombre"]}')
            print(f'Precio: {mostrarZonaA["precio"]}')
            print(f'Descripción: {mostrarZonaA["descripcion"]}')
            print(f'Marca: {mostrarZonaA["marca"]}')
            print(f'Referencia: {mostrarZonaA["referencia"]}')
            print(f'Pais: {mostrarZonaA["pais"]}')
            print(f'Numero de Unidades: {mostrarZonaA["numeroUnidades"]}')
            if mostrarZonaA["garantia"]==True:
                print("Garantía extendida: Sí")
            else:
                print("Garantía extendida: No")
            print()
    
    if opcionUsuario == 3:
        nombreBuscar=input("Ingresa el nombre del producto que deseas buscar: ").upper()
        for buscador in zonaA:
            print()
            if buscador["nombre"]==nombreBuscar:
                print(f'Zona: {buscador["zona"]}')
                print(f'Id: {buscador["id"]}')
                print(f'Nombre: {buscador["nombre"]}')
                print(f'Precio: {buscador["precio"]}')
                print(f'Descripción: {buscador["descripcion"]}')
                print()
            else:
                print("No se ha encontrado el producto en la zona A")
        print()
        for buscador in zonaB:
            print()
            if buscador["nombre"]==nombreBuscar:
                print(f'Zona: {buscador["zona"]}')
                print(f'Id: {buscador["id"]}')
                print(f'Nombre: {buscador["nombre"]}')
                print(f'Precio: {buscador["precio"]}')
                print(f'Descripción: {buscador["descripcion"]}')
                print()
            else:
                print("No se ha encontrado el producto en la zona B")
        print()
        for buscador in zonaC:
            print()
            if buscador["nombre"]==nombreBuscar:
                print(f'Zona: {buscador["zona"]}')
                print(f'Id: {buscador["id"]}')
                print(f'Nombre: {buscador["nombre"]}')
                print(f'Precio: {buscador["precio"]}')
                print(f'Descripción: {buscador["descripcion"]}')
                print()
            else:
                print("No se ha encontrado el producto en la zona C")
        print()

        for buscador in zonaD:
            print()
            if buscador["nombre"]==nombreBuscar:
                print(f'Zona: {buscador["zona"]}')
                print(f'Id: {buscador["id"]}')
                print(f'Nombre: {buscador["nombre"]}')
                print(f'Precio: {buscador["precio"]}')
                print(f'Descripción: {buscador["descripcion"]}')
                print()
            else:
                print("No se ha encontrado el producto en la zona D")
        print()

    if opcionUsuario==4:
        nombreModificar=input("Ingresa el nombre del producto que deseas modificar: ").upper()
        for modificador in zonaA:
            if modificador["nombre"]==nombreModificar: 
                nuevoCantidad=input("Ingresa la nueva cantidad: ")
                while nuevoCantidad.isdigit()==True:
                    print(f'La cantidad {nuevoCantidad} no es válida.')
                    print("Prueba nuevamente usando solo números")
                    nuevoCantidad=input("Ingresa la nueva cantidad: ")
                while nuevoCantidad >= modificador["numeroUnidades"]:
                    print("No puedes ingresar una cantidad mayor a la actual")
                    nuevoCantidad=input("Ingresa la nueva cantidad: ")
                    while nuevoCantidad.isdigit()==True:
                        print(f'La cantidad {nuevoCantidad} no es válida.')
                        print("Prueba nuevamente usando solo números")
                        nuevoCantidad=input("Ingresa la nueva cantidad: ")
                modificador["numeroUnidades"]=nuevoCantidad
                print("Cantidad modificada con éxito")
                print()   
            else:
                print("No se ha encontrado el producto")
                print()
        for modificador in zonaB:
            if modificador["nombre"]==nombreModificar: 
                nuevoCantidad=input("Ingresa la nueva cantidad: ")
                while nuevoCantidad.isdigit()==True:
                    print(f'La cantidad {nuevoCantidad} no es válida.')
                    print("Prueba nuevamente usando solo números")
                    nuevoCantidad=input("Ingresa la nueva cantidad: ")
                while nuevoCantidad >= modificador["numeroUnidades"]:
                    print("No puedes ingresar una cantidad mayor a la actual")
                    nuevoCantidad=input("Ingresa la nueva cantidad: ")
                    while nuevoCantidad.isdigit()==True:
                        print(f'La cantidad {nuevoCantidad} no es válida.')
                        print("Prueba nuevamente usando solo números")
                        nuevoCantidad=input("Ingresa la nueva cantidad: ")
                modificador["numeroUnidades"]=nuevoCantidad
                print("Cantidad modificada con éxito")
                print()   
            else:
                print("No se ha encontrado el producto")
                print()

        for modificador in zonaC:
            if modificador["nombre"]==nombreModificar: 
                nuevoCantidad=input("Ingresa la nueva cantidad: ")
                while nuevoCantidad.isdigit()==True:
                    print(f'La cantidad {nuevoCantidad} no es válida.')
                    print("Prueba nuevamente usando solo números")
                    nuevoCantidad=input("Ingresa la nueva cantidad: ")
                while nuevoCantidad >= modificador["numeroUnidades"]:
                    print("No puedes ingresar una cantidad mayor a la actual")
                    nuevoCantidad=input("Ingresa la nueva cantidad: ")
                    while nuevoCantidad.isdigit()==True:
                        print(f'La cantidad {nuevoCantidad} no es válida.')
                        print("Prueba nuevamente usando solo números")
                        nuevoCantidad=input("Ingresa la nueva cantidad: ")
                modificador["numeroUnidades"]=nuevoCantidad
                print("Cantidad modificada con éxito")
                print()   
            else:
                print("No se ha encontrado el producto")
                print()

        for modificador in zonaD:
            if modificador["nombre"]==nombreModificar: 
                nuevoCantidad=input("Ingresa la nueva cantidad: ")
                while nuevoCantidad.isdigit()==True:
                    print(f'La cantidad {nuevoCantidad} no es válida.')
                    print("Prueba nuevamente usando solo números")
                    nuevoCantidad=input("Ingresa la nueva cantidad: ")
                while nuevoCantidad >= modificador["numeroUnidades"]:
                    print("No puedes ingresar una cantidad mayor a la actual")
                    nuevoCantidad=input("Ingresa la nueva cantidad: ")
                    while nuevoCantidad.isdigit()==True:
                        print(f'La cantidad {nuevoCantidad} no es válida.')
                        print("Prueba nuevamente usando solo números")
                        nuevoCantidad=input("Ingresa la nueva cantidad: ")
                modificador["numeroUnidades"]=nuevoCantidad
                print("Cantidad modificada con éxito")
                print()   
            else:
                print("No se ha encontrado el producto")
                print()

    if opcionUsuario == 5:
        opcionEliminar=input("Ingresa el nombre del producto que deseas eliminar: ").upper()
        for eliminador in zonaA:
            print(zonaA)

            if opcionEliminar==eliminador["nombre"]:
                print("Producto encontrado")
                print("___________________")
                print()
                print(f'Id: {eliminador["id"]}')
                print(f'Nombre: {eliminador["nombre"]}')
                print(f'Precio: {eliminador["precio"]}')
                print(f'Zona: {eliminador["zona"]}')
                print(f'Descripción: {eliminador["descripcion"]}')
                print(f'Marca: {eliminador["marca"]}')
                print(f'Referencia: {eliminador["referencia"]}')
                print(f'Pais: {eliminador["pais"]}')
                print(f'Numero de Unidades: {eliminador["numeroUnidades"]}')
                print("___________________")
                print()
                print("¿Está seguro que desea eliminar este producto?")
                confirmarEliminar=input("Digite S para confirmar. N para cancelar.").upper()
                if confirmarEliminar == "S":
                    if eliminador["zona"]=="A":
                        zonaA.remove(eliminador)
                    elif eliminador["zona"]=="B":
                        zonaB.remove(eliminador)
                    elif eliminador["zona"]=="B":
                        zonaC.remove(eliminador)
                    else:
                        zonaD.remove(eliminador)
                print()
                print("Producto eliminado con éxito")
                print()

            else:
                print(f'No se ha encontrado ningun producto con el nombre {opcionEliminar}')
                print()
    if opcionUsuario==6:
        print("Gracias por usar nuestro sistema")
        print(idDisponibles)

