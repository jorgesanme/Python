from functools import reduce

lista = [10,3, 8,-8 -1, 15,9]

# operadore map hace mapeo de cada uno del contenido de la lista.
print("lista: ",lista)

listaDoble = map(lambda x: x*2, lista)
# list nos permite ver el contenido de un obejto ( listaDoble es un objeto)
print ("el doble de la lista:", list(listaDoble))

# filter nos selecciona solo los valores que coincidad con lo espesificado.

listaPares = filter(lambda x: x%2== 0, lista)
print ("valores pares: ",list(listaPares))

# recude nos resume el contenido de la lista a un solo valor, suma o multiplo o division o resta.

sumatorio= reduce( lambda x , y : x+y, lista)

print ("suma de todos: ",(sumatorio))

suma100 = reduce ( lambda x,y: x+y, range(0,101))

print ("suma100: ", suma100)