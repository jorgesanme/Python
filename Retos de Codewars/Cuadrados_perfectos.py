# calcular numero cuadrado perfectos
import math

def is_square(n): 
    a= n*n
    if n> -1 and math.sqrt(n) %1 ==0:
        print ("es cuadrado")
    else:
        print ("no es un nombre cuadrado")
    return False # fix me
    

num= int (input("introduzca el nº de bloques: "))

is_square(num)
