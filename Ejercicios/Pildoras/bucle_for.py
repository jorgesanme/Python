#sumar los 100 primeros numeros:
total=0
for i in range(0,101):    
    total = total+i  
print (f"total sumado {total}") # f nos permite formatear la cadena y añadir la variable en { }

# imprime las estaciones

for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
    print (f"Ahora es -> {i}")
    
# imprimer cada letra de un texto

for letra in ("ya esta aqui la primavera"):
    print (letra, end="") # nos permite terminar la linea añadiendo y caracter la siguiente al lado derecho.

print ()
for letra in ("ya esta aqui la primavera"):
    print (letra, end="-") # nos permite terminar la linea añadiendo un caracter y la siguiente al lado derecho.
    
#confirmar un email
    
contador=0
print("\n")
for i in input("introzca un email: "):
    if (i=="@"or i=="."):
        contador += 1

if contador == 2:
    print ("Email correcto")
else:
    print ("El email no es correcto")
    