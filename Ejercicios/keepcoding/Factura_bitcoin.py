# culcular el total de factura

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
factuni= []
factpre= []

# se crea el bucle while 
while unidades > 0 and precio > 0:
    
    #se muestra cada una de las compras
    total= round(unidades * precio)
    print("unidades", unidades, "\t\t Precio", precio, "\t\t Total: ", total)  
    
    #se almacena en las listas cada una de las compras
    factuni.append(unidades)
    factpre.append(precio)
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
print("\nbucle For\n")
print("------------------------------------------")
for cont in range (0,len(factuni)):
                      print("unidades: ", factuni[cont], "\t\tPrecio:", factpre[cont], "\t\tTotal: ", (factuni[cont]*factpre[cont]))
                   
print("------------------------------------------")
print("Unidades: ", totalUnidades, " pvp medio: ",round(totalPrecio/totalUnidades), "Total: ",totalPrecio,  )

# se muesta las compras con bucle While
indice =0
print("\nbucle While\n")
print("------------------------------------------")
while indice < len(factuni):
    print("unidades: ", factuni[indice], "\t\tPrecio:", factpre[indice], "\t\tTotal: ", (factuni[indice]*factpre[indice]))
    indice +=1               
print("------------------------------------------")
print("Unidades: ", totalUnidades, " pvp medio: ",round(totalPrecio/totalUnidades), "Total: ",totalPrecio,  )

#se muestra las compras almacenadas en las listas
print("\nbucle For MEJORADO\n")
print("------------------------------------------")
for unidades, precio in  zip(factuni, factpre):
                      print("unidades: ", unidades, "\t\tPrecio:",precio, "\t\tTotal: ", (unidades*precio))
                   
print("------------------------------------------")
print("Unidades: ", totalUnidades, " pvp medio: ",round(totalPrecio/totalUnidades), "Total: ",totalPrecio,  )

