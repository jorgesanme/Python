# diccionarios en python  clave :  valor

# crear un diccionario
diccionario={"alemania":"Berlin", "Francia":"Paris", "Reino Unido":"londres", "España":"Madrid"}

#imprimir o acceso a un registro 
print (diccionario["Francia"])
print("\n")
print (diccionario["España"])

# añadir un registro al diccionario
diccionario["Italia"]="lisboa"
print(diccionario)
print("\n")

# Modificar un registro en el diccionario
diccionario["Italia"]="Roma"

print(diccionario)

# Borrar / eliminar un registro del diccionario
del diccionario["Reino Unido"]
print("\n")
print(diccionario)

# el diccionario puede almacenar cualquier tipo de datos
otrodiccionario={"alemania":"Berlin", 23:"Mike Jordan", "Mosqueteros":3 , 43:"Rohin", 7:"Samurais"}
print("\n")
print(otrodiccionario)
print (otrodiccionario[23])

# usando una TUPLA para almacenar en un diccionario

mitupla=["españa", "Francia", "reino unido", "alemania"]

dicc= {mitupla[0]:"madrid", mitupla[1]:"paris", mitupla[2]:"londres", mitupla[3]:"berlin"}
print("\n")
print (dicc)

print(dicc[mitupla[1]])
print(dicc["Francia"])

# metodos de un diccionario
# .keys devuelve las claves diccionario
# .values  devuelve los valores asignados a las claves
# len() longitud de pares de claves-valores
print (dicc.keys())
print (dicc.values())