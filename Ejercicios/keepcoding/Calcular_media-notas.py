# calcular media de unas notas

def calculaMedia(lista): # parametros pasados por orden, deben estar todos
    suma =0
    for n in lista:
        suma += n
    return round(suma/len(lista), 3)

def esMedia(*items): # un parametros variables en cantidad  se inicia con ( * )
    suma = 0
    for n in items:
        suma += n
    return round (suma/len(items), 2)

