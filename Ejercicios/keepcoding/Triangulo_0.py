#while True:
#    try:
#        b= float (input ("introduzca la base: "))
#        h= float ( input("introduzca la altura: "))
#        break
#    except ValueError:
#        print ("Oops! Solo se permiten números ENTEROS... Nada de letras.")
#        False 
#####################

## se define una funcion
def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        #print ("No se permiten letras o enteros negativos")
        return False


B = input ("base del triángulo: ")
  
if esDecimal(B):
    b= float(B)
    H = input ("altura del triángulo: ")
    if esDecimal(H):
        h= float (H)
        area= b*h/2
        print ("el area es: ",round (area))
    
                   
    else:
        print (H, "No se permiten letras o enteros negativos")
        
else:
    print (B, " No se permiten letras o enteros negativos")
    







