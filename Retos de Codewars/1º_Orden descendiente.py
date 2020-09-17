# Orden descendiente de un conjunto de nº Integer

def Descending_Order(num):
    #se busca en la lista el numero mayor
    salida=[]
    for i in num:
        salida.append(i)
        salida.sort(reverse=True)        
    lista=""
    for j in salida:    
        lista += str(j)    
                    
    return lista

numeros= int (input("Introduzca una \"retajila\" de números: "))

print ("Sus nº en orden Desdendiente", Descending_Order(str(numeros)))


# la opcion de CODEWARS
"""
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
"""