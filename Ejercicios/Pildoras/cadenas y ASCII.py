# manipular Cadenas String
# video 1214 repasarlo todo antes de seguir

cadena= "HOLA MUNDO"
for caracter in cadena:
    if ord(caracter) in range (65,90) #or cadena in range (97,122):
        print(caracter, "-", ord(caracter+32))
    
    