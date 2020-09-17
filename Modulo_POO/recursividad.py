# recursividad es una forma de usar una funcion que,
# se llama a si misma todo el tiempo que sea necesaria.

def cuentaTras (e):
    print ("{},".format(e), end="")
    # es importante definir el cierre del bucle e >=0 ó != 0
    if e != 0 : 
        cuentaTras( e-1)

cuentaTras(10)

# sumatorio recursivo

def sumatorio(n):
    if  n != 0 and n>0:
        return n + sumatorio(n-1)
    else:
        return n

print (sumatorio(100))
    
