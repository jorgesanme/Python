# creando un diccionario


# se pide los primeros datos 
while True:
    try:
        unidades= float (input ("cantidad comprada: "))
        precio= float  (input ("precio de unitario(€): "))
        break
    except ValueError:
        print ("Oops! Solo se permiten números... Nada de letras.")
        False

#se inicia las variables

totalUnidades=0
totalPrecio=0
# se crean dos lista para almacenar las compras ( con una matriz será más facil)
listaFactura=[]

# se crea el bucle while 
while unidades > 0 and precio > 0:
    
    #se muestra cada una de las compras
    total= round(unidades * precio)
    print("unidades", unidades, "\t\t Precio", precio, "\t\t Total: ", total)  
    
    #se almacena en el diccionario dict() los registros
    #se crea el indise [' '] para cada registro ( es como un atributo de java)
    item= dict()
    item['unidades']=unidades
    item['precio']=precio
    # se guarda un registro en la lista de facturas
    listaFactura.append(item)
    #se cargan en los totales los valores nuevos
    totalUnidades+= unidades
    totalPrecio += precio
    #se vuelve a pedir los valores de compra
    while True:
        try:
            unidades= float (input ("cantidad comprada: "))
            precio= float  (input ("precio de unitario(€): "))
            break
        except ValueError:
            print ("Oops! Solo se permiten números... Nada de letras.")
            False
            


#se muestra las compras almacenadas en las listas
print("\nbucle For MEJORADO\n")
print("------------------------------------------")
for item in  listaFactura:
                      print("unidades: ", item['unidades'], "\t\tPrecio:",item['precio'], "\t\tTotal: ", (item['unidades']*item['precio']))
                   
print("------------------------------------------")
print("Unidades: ", totalUnidades, " pvp medio: ",round(totalPrecio/totalUnidades), "Total: ",totalPrecio,  )



