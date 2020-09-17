# se define una funcion que realice el factorial de cualquier nº

def factorial(n):
    # si el nº  es distinto de 1 y mayor que 1 ( si multiplicamos por 0 se caska)
    if n != 1 and n>1:
    # se devuelve el valor de n * n-1( llamando a la misma funcion recursivamente)
        return  n * factorial(n-1)
    else:
        return n
    
print (factorial(5))