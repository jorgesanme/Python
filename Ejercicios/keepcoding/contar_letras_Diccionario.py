#contar letras con un diccionario

#texto a contar
miTexto = "tres o cuatro palabras para Ti, Otras tantas para MI"

# se crea el diccionario
frecuencias = dict()

# bucle que recorre caracter a caracter en mi texto
for caracter in miTexto:
    if caracter in frecuencias:   # si el caracter se encuentra en las claves de Frecuencias
        frecuencias[caracter]+=1  # le sumamos uno al valor de la clave 
    else:                         
        frecuencias[caracter] = 1 #caso contrario se crea el valor (1) para la nueva clave

#se crea una variable que cuenta todas las letras
total =0

# se crea un bucle para mostrar todo el diccionario con sus valores

for letras in frecuencias.keys():
    print(letras, "-", frecuencias[letras])
    total += frecuencias[letras]

print ("total letras", total)
    
# Se imprime las letras y su cantidad encontrada
