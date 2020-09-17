# mostra nota media de una lista  de notas
# se solicita la cantidad de asignaturas
while True:
    try:
        asig= int (input ("Cuantas notas desea introducir: ") )
        break
    except ValueError:
        print ("Oops! Solo se permiten números ENTEROS... Nada de letras.")
        False
        
# se crea una lista vacía
notas=[]
contador=0
# se rellena la lista con las notas de cada asignatura
for contador in range (0, asig):
    notas.insert(contador, int (input(f"cual es la {contador+1}º nota? ")))
    contador += 1

# bucle for para calcular la media de notas
contador=0
sumaNotas=0

for contador in range(0,len(notas)):
    sumaNotas= sumaNotas+ notas[contador]

# Bucle While para calcular la media de notas    
contador2=0
sumaNotas2=0
while contador2 < len(notas):
    sumaNotas2 += notas[contador2]
    contador2 +=1

# presentar datos del alumno
    
media=  sumaNotas / len(notas)
print("-----------con bucle for-------------------")
print(f"El alumno tiene: {len(notas)} asignaturas ")
print("La nota Media es: %.2f" % media)
print("-----------------------------------------")


# realizado con while
media2= sumaNotas2 / len(notas)

print("------------con bucle While----------------")
print(f"El alumno tiene: {len(notas)} asignaturas ")
print("La nota Media es: %.2f" % media2)
print("-----------------------------------------")