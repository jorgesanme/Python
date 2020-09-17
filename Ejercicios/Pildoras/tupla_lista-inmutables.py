## se crea una tupla con los dias de las semanas

tupla=("lunes", "martes","miercoles","jueves","Viernes", "sabado","domingo","domingo")

#acceso ana posición de la lista
print ("hoy es  ", tupla[1])
print ("hoy es  ", tupla[3])
print ("hoy es  ", tupla[6])

#convertimos una tupla en lista

lista=list(tupla)
print ("se muestra la lista")
print (lista[:])
print("")
print ("se muestra la tupla, diferencia en los [] / ()")
print (tupla[:])

# buscar un valor en la tupla   " in "
print("")
print("Esta el domingo en la tupla?")
print ("domingo" in tupla)

# contar cuantas veces hay un valor en la tupla .count()
print("")
print("cuantos domingos hay en al tupla?")
print (tupla.count("domingo"))

# metodo len() nos devuelve la longitud de la tupla / lista

print()
print("la tupla tienen",len(tupla), "elementos")



# DESEMPAQUETADO DE TUPLAS: se asigna a una variable  c/u del contenido de la tupla

uno, dos, tres, cuatro, cinco, seis, siete, ocho = tupla

print (uno)
print (ocho)
print (seis)
print (dos)
print (cuatro)

print("\n")

print (tupla.index('lunes'))