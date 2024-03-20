import uuid

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
    opcionUsuario=input("Digita la opción que deseas realizar")
    while opcionUsuario.isdigit()==False:
        print("Debes ingresar una opción válida")
        opcionUsuario=input("Digita la opción que deseas realizar")

    opcionUsuario= int(opcionUsuario)

    if opcionUsuario == 1:
        idProducto=uuid.uuid1
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
        producto["numeroUnidades"]=input("Numero de unidades compradas")
        while producto["numeroUnidades"].isdigit()==False:
            print("El número de productos solo puede ser un número")
            producto["numeroUnidades"]=input("Numero de unidades compradas")
        producto["numeroUnidades"]=int(producto["numeroUnidades"])
        while producto["numeroUnidades"]>50:
            print("La cantidad de unidades no puede ser mayor a 50")
            producto["numeroUnidades"]=input("Numero de unidades compradas")           
        producto["garantia"]=input("Tiene garantía extendida(S/N): ").upper()
        while producto["garantia"].isdigit()==True:
            print(f'La opción {producto["garantia"]} no es válida')
            print("Digita S o N")
        if producto["garantia"]=="S":
            producto["garantia"]=True
        else:
            producto["garantia"]=False

        if producto["zona"]=="A":
            zonaA.append(producto)
        elif producto["zona"]=="B":
            zonaB.append(producto)
        elif producto["zona"]=="C":
            zonaC.append(producto)
        else:
            zonaD.append(producto)

    if opcionUsuario == 2:
        print(zonaA)
        print(zonaB)
        print(zonaC)
        print(zonaD)
    
    if opcionUsuario == 3:
        nombreBuscar=input("Ingresa el nombre del producto que deseas buscar: ").upper()
        for buscador in zonaA:
            if buscador["nombre"]==nombreBuscar:
                print(f'Id: {buscador["id"]}')
                print(f'Nombre: {buscador["nombre"]}')
                print(f'Precio: {buscador["precio"]}')
                print(f'Descripción: {buscador["descripcion"]}')
            else:
                print("No se ha encontrado el producto en la zona A")
        for buscador in zonaB:
            if buscador["nombre"]==nombreBuscar:
                print(f'Id: {buscador["id"]}')
                print(f'Nombre: {buscador["nombre"]}')
                print(f'Precio: {buscador["precio"]}')
                print(f'Descripción: {buscador["descripcion"]}')
            else:
                print("No se ha encontrado el producto en la zona B")
        for buscador in zonaC:
            if buscador["nombre"]==nombreBuscar:
                print(f'Id: {buscador["id"]}')
                print(f'Nombre: {buscador["nombre"]}')
                print(f'Precio: {buscador["precio"]}')
                print(f'Descripción: {buscador["descripcion"]}')
            else:
                print("No se ha encontrado el producto en la zona C")

        for buscador in zonaD:
            if buscador["nombre"]==nombreBuscar:
                print(f'Id: {buscador["id"]}')
                print(f'Nombre: {buscador["nombre"]}')
                print(f'Precio: {buscador["precio"]}')
                print(f'Descripción: {buscador["descripcion"]}')
            else:
                print("No se ha encontrado el producto en la zona D")

    if opcionUsuario==4:
        nombreModificar=input("Ingresa el nombre del producto que deseas modificar: ").upper()
        for modificador in zonaA:
            if modificador["nombre"]==nombreModificar: 
                nuevoCantidad=int(input("Ingresa la nueva cantidad: "))
                if nuevoCantidad <= modificador["numeroUnidades"]:
                    modificador["numeroUnidades"]=nuevoCantidad
                else:
                    print("No puedes ingresar una cantidad mayor a la actual")
                    nuevoCantidad=int(input("Ingresa la nueva cantidad: "))
                    modificador["numeroUnidades"]=nuevoCantidad
            else:
                print("No se ha encontrado el producto")
        for modificador in zonaB:
            if modificador["nombre"]==nombreModificar: 
                nuevoCantidad=int(input("Ingresa la nueva cantidad: "))
                if nuevoCantidad <= modificador["numeroUnidades"]:
                    modificador["numeroUnidades"]=nuevoCantidad
                else:
                    print("No puedes ingresar una cantidad mayor a la actual")
                    nuevoCantidad=int(input("Ingresa la nueva cantidad: "))
                    modificador["numeroUnidades"]=nuevoCantidad

        for modificador in zonaC:
            if modificador["nombre"]==nombreModificar: 
                nuevoCantidad=int(input("Ingresa la nueva cantidad: "))
                if nuevoCantidad <= modificador["numeroUnidades"]:
                    modificador["numeroUnidades"]=nuevoCantidad
                else:
                    print("No puedes ingresar una cantidad mayor a la actual")
                    nuevoCantidad=int(input("Ingresa la nueva cantidad: "))
                    modificador["numeroUnidades"]=nuevoCantidad

        for modificador in zonaD:
            if modificador["nombre"]==nombreModificar: 
                nuevoCantidad=int(input("Ingresa la nueva cantidad: "))
                if nuevoCantidad <= modificador["numeroUnidades"]:
                    modificador["numeroUnidades"]=nuevoCantidad
                else:
                    print("No puedes ingresar una cantidad mayor a la actual")
                    nuevoCantidad=int(input("Ingresa la nueva cantidad: "))
                    modificador["numeroUnidades"]=nuevoCantidad

    if opcionUsuario==6:
        print("Gracias por usar nuestro sistema")

