# se define una lista con nombre

miLista=["David","Nayra","Mariela","Javier","Jorge"]

print("segundo nombre de la lista es:", miLista[1])
print("")
print("1º nombre de la lista es:",miLista[0])
print("")
#empieza a contar desde el final de la lista [-1]
print("último nombre de la lista es:",miLista[-1])
print("")

print("penultimo nombre de la lista es:",miLista[-2])
print("")

#acceso a una porcion de la lista [0:3]
print("el nombre justo en medio de la lista es:",miLista[2:3])
print("")
#añadir valor a la lista .append
miLista.append("Sandra")
print("último nombre de la lista  AHORA es:",miLista[-1])
print("")

#insertar valor en oto lugar de la lista .insert(indice,valor)
miLista.insert(1,"pedro")
print("segundo nombre de la lista AHORA es:", miLista[1])
print("")

# INSERTAR VARIOS VALORES A LA LISTA o AÑADIR OTRA LISTA extend ([VALORES, VALORES])
miLista.extend(["Bilbao","Emiko","Eileen"])
print("el nombre justo en medio de la lista es:",miLista[-3:]) # muestra desde la posicion -3 hasta el final de la lista
print("")

# imprimir todo la lista a traves de una funcion que se puede usar muchas veces
def imprimir(lista):
    for contador in range(0,len(lista)):
        print("indice: [",contador,"]","  nombre: ",lista[contador])

imprimir(miLista)    
# mostrar el indice de un elemento .index()

print ("ese valor esta en la posicion nº: ", miLista.index("Emiko"))

# comprobar si un valor esta en la lista  " in "
print("")
print ("esta pepe en la lista")
print ("pepe" in miLista)
print("")
print ("esta Eileen en la lista")
print ("Eileen" in miLista)

# borrar un valor un elemento de la lista .remove()
print ("se procede a borrar a Bilbao de la lista")
miLista.remove ("Bilbao")
print (miLista[:])
print("")
# borrar el ultimo valor de la lista .pop()
print("se borra el ultimo valor de la lista que es--> ", miLista[-1])
miLista.pop()
print (miLista[:])
print("")
# Sumar lista aunque sean diferentes suma " + "
lista2=["carlos","ana","lidia"] # una lista nueva
print ("se va a sumar esta nueva lista:  ", lista2[:])
print("")

miLista3=lista2+miLista # se suman las dos lista a la tercera

imprimir(miLista3) # se llama a la funcion imprimir para mostrar toda la lista
    
