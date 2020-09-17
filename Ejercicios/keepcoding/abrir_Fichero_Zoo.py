def procesa(reg):
    precio = 0
    print (reg)
    total= 0
    for i in reg:        
        if i[2:] == '0':
            precio= 0
            unidades = int (i[0:1])
            total += unidades*precio                       
            print ("{} entradas de bebes..:\t  {:.2f}€ \t\t Total {:.2f}".format(unidades, precio, unidades*precio) )
            
        elif i[2:] == '14':
            precio = 14
            unidades = int (i[0:1])
            total += unidades*precio                      
            print ("{} entradas de niño...:\t  {:.2f}€ \t\t Total {:.2f}".format(unidades, precio, unidades*precio) )
            
        elif i[2:] == '18':
            precio = 18
            unidades = int (i[0:1])
            total += unidades*precio                        
            print ("{} entradas de abuelo.:\t  {:.2f}€ \t\t Total {:.2f}".format(unidades, precio, unidades*precio) )
            
        elif i[2:] == '23':
            precio = 23
            unidades = int (i[0:1])
            total += unidades*precio                        
            print ("{} entradas normal....:\t  {:.2f}€ \t\t Total {:.2f}".format(unidades, precio, unidades*precio) )
        
            
    print ("\n\t\t Total del Tiket: ", total, "\n")    
    return total
    
    
fEntrada = open ("FicheroEntradas.txt", 'r')

linea = fEntrada.readline()

while linea != '':
    entradas= linea.split(',')
    procesa(entradas)
    linea= fEntrada.readline()

#for linea in todas:
 #   print (linea)

fEntrada.close()