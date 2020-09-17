def normal (x): #se devuelve el valor que tenga el rango
    return x

def cuadrado (y): # devuelve el cuadrado del valor del rango
    return y*y

def sumaTodos (limitTo, f):
    resultado= 0
    # nos suma el valor dentro del rango que se
    # pasa por parametros (100 o cualquier otro)
    for i in range (limitTo+1):
        resultado += f(i)
    return resultado
# imprime la suma de todos los valores entre 0 y 100.
# 'Normal' y 'Cuadrado' son  funciones pasadas por parámetro

if __name__ == '__main___':
    
    print (sumaTodos(100, normal))
    print (sumaTodos(3, cuadrado))

    