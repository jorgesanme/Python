
# SE DESEA OBTENER EL Nº MAYOR DE UNA LISTA DE PARAMETROS
#  ( *l) cojer todos los parametros separados por coma y tratarlos como array
def maxi(*l):
    # si la lista de parametros esta vacia, se devuelve '0'
    if len(l) == 0:
        return 0
    m= l[0] # Se obtiene el 1º valor de la lista
    
    # se recorre la lista comprobando el valor mayor.
    for ix in range (1, len(l)):
        if l[ix] > m: # si el valor es mayor se 
            m= l[ix]  # se asigna a la variable 'm'          
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    
    m = l[0]
    
    for ix in range (1, len(l)):
        if l[ix] <m :
            m = l[ix]
    return m

# se calcula la media de los parametros
def media (*l):
    suma = 0
    if len(l) ==0: 
       return 0    
    # se recorre la lista parámetros sumando cada valor
    for valor in (l):
        suma += valor
    
    return suma/len(l) # se devuelve suma partida por cantidad de valores


#se crea un diccionario con nombre funciones
funciones = {
    'max': maxi,
    'min': mini,
    'med': media
    }

def returnF(nombre):
    nombre=  nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    
    return None
