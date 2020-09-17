# uso de un generador

#esta es una funcion normal
def generaPares(limite):    
    num=1    
    milista=[]    
    while num <=limite:
        milista.append(num*2)        
        num += 1
    return milista

print (generaPares(10))


# este es el GEnerador
def generaPar(limite):
    num=1
    while num<= limite:
        yield num*2
        num += 1
devuelvePar=generaPar(10)

#imprimir cada una de los valores de cada paso de un Generador

print (next(devuelvePar))
print ("aqui va mi código...")
print (next(devuelvePar))
print ("aqui va mi código...")
print (next(devuelvePar))