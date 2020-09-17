# anagrama de palabras

def compara(p1,p2):
       
    listaComparacionLetras= []
    
    for caracter1 in p1:
        bombilla= False
        for caracter2 in p2:
            if caracter1 == caracter2:
                bombilla = True
                listaComparacionLetras.append(True)
            
        if not bombilla:
            listaComparacionLetras.append(False)
    
    
    if False in listaComparacionLetras:
        print ("no es Anagrama")
    else:
        print ("Es un anagrama")
 
   
    
raton= 'amor'
perro = 'ramo'
compara(raton, perro)

