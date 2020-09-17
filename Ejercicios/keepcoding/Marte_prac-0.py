# practica de comunicacion con Marte

digitos16= ("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f")
angulo = 360/16
cadena = input ("introduzca el mensaje a enviar: ")

for caracter in cadena:
    vhex= hex(ord(caracter))
    digito1=vhex[2]
    digito2=vhex[3]
    #print (digito1, digito2)


print ("--------------------")
# version 2 del mismo programa
mensaje = []
for caracter in cadena:
    vhex= hex(ord(caracter))
    digito1=vhex[2]
    angulo1= digitos16.index(digito1)*angulo
    
    digito2=vhex[3]
    angulo2= digitos16.index(digito2)*angulo
    par=(angulo1,angulo2)
    mensaje.append(par)
    #print (digito1,"-", angulo1)
    #print (digito2,"-", angulo2)file:///home/jorge/Primux_file:///home/jorge/Primux_migración/Ringtones/Batman_Begins_Score_-_01_-_Vespertilio.mp3migración/Ringtones/Batman_Begins_Score_-_01_-_Vespertilio.mp3
print (mensaje[:])
salida=""
for par in mensaje:
    
    caracter =""
    # se localiza el digito correspondiente al angulo en el 1º conjunto de pares
    base16_1= int(round(par[0]/angulo))
    base16_2= int(round(par[1]/angulo))
    
# se convierte ese digito a hexadecimal    

    vhex_1= hex(base16_1)
    vhex_2= hex(base16_2)
# se extrae las dos primera posiciones del hexadecimal de cada digito y se convierten en String   
    caracter += str((vhex_1[2:]))
    caracter += str((vhex_2[2:]))
# confirmamos por pantalla los valores encontrados    
    print (caracter)
# se  tranforma el valor hexadecimal en enteros para posteriormente obtener la letra (chr) de cada entero    
    letra = chr(int(caracter,16))
# se suma esa letra a la salida por pantalla y se imprime
    salida += letra
print ((salida))
    
   
 
    