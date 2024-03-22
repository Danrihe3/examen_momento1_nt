'''
INTEGRANTES

DANIEL RIOS HERRERA
JULIAN ÁLVAREZ
EDWIN SUÁREZ

'''

frutas=[]

opcionUsusario=6
contadorTotal=0

print("Calcula tu salpicón")
print("*******************")
print()

while opcionUsusario!=5:
    print("Menú de opciones")
    print()
    print("1. Registrar fruta.")
    print("2. Mostrar costo total del salpicón.")
    print("3. Mostrar frutas ordenadas.")
    print("4. Mostrar fruta más barata.")
    print("5. Salir")
    opcionUsusario=input("Digita la opción que deseas realizar: ")
    print()
    while opcionUsusario.isdigit()==False:
        print(f'La opción {opcionUsusario} no es una opción válida')
        print("Digita una opcion válida")
        opcionUsusario=input("Digita la opción que deseas realizar: ")
        opcionUsusario=int(opcionUsusario)
        print()
    opcionUsusario=int(opcionUsusario)
    if opcionUsusario == 1:
        fruta={}
        fruta["nombre"]=input("Digita el nombre de la fruta: ")
        while fruta["nombre"].isdigit()==True:
            print("El nombre de la fruta no puede contener números")
            print("Inténtalo nuevamente")
            fruta["nombre"]=input("Digita el nombre de la fruta: ")
        fruta["id"]=input("Digita el id de la fruta (Solo números): ")
        while fruta["id"].isdigit()==False:
            print(f'El id {fruta["id"]} no es válido.')
            print("Inténtalo de nuevo solo con números.")
            fruta["id"]=input("Digita el id de la fruta (Solo números): ")
        fruta["precioUnitario"]=input("Precio unitario: ")
        while fruta["precioUnitario"].isdigit()==False:
            print(f'El precio {fruta["precioUnitario"]} no es válido.')
            print("Inténtalo nuevamente.")
            fruta["precioUnitario"]=input("Precio unitario: ")
        fruta["precioUnitario"]=int(fruta["precioUnitario"])
        fruta["cantidad"]=input("Cantidad: ")
        while fruta["cantidad"].isdigit()==False:
            print(f'La cantidad {fruta["cantidad"]} no es válida.')
            print("Inténtalo de nuevo.")
            fruta["cantidad"]=input("Cantidad: ")
        fruta["cantidad"]=int(fruta["cantidad"])
        contadorTotal+=fruta["precioUnitario"]*fruta["cantidad"]
        frutas.append(fruta)
        print()

    elif opcionUsusario==2:
        print("El costo total de salpicón es: ")
        print()
        print(f'{contadorTotal} pesos.')
        print()
    
    elif opcionUsusario==3:
        print("Frutas ordenadas de mayor a menor precio: ")
        print()
        frutasOrdenadas=sorted(frutas,key=lambda orden: orden["precioUnitario"], reverse=True)
        for ordenFinal in frutasOrdenadas:
            print(ordenFinal["nombre"])
            print(ordenFinal["precioUnitario"])
            print()
    elif opcionUsusario==4:
        print("La fruta más barata es: ")
        frutasOrdenadas=sorted(frutas,key=lambda orden: orden["precioUnitario"])
        print(frutasOrdenadas[0]["nombre"])
        print(frutasOrdenadas[0]["precioUnitario"])
        print()

    elif opcionUsusario==5:
        print()    
        print("Gracias por usar nuestro sistema")
        print()