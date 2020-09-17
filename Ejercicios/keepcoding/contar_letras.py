# contar letras
miTexto = "tres o cuatro palabras para Ti"

letras =[]
frecuencias = []

def existe(letra, lista):
    posicion = 0
    while posicion <len(lista):
        if lista[posicion] == letra:
            return posicion
        posicion+= 1
    
    return None

for caracter in miTexto:
    posicion= existe(caracter,letras)
    if posicion != None:
        
        frecuencias[posicion] += 1
    else:
        letras.append(caracter)
        frecuencias.append(1)
# Se imprime las letras y su cantidad encontrada
indice = 0
total =0
while indice< len (letras):
    print (letras[indice], "-" , frecuencias[indice])
    
    total += frecuencias[indice]
    indice += 1
print ("total letras", total)
