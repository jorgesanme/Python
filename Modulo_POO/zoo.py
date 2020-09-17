# practica de entradas al ZOO
import operator # se importa una clase que permite realizar operaciones en lista y diccionarios
#se importa la clase que nos permite guardar en archivo

# se define una funcion para estipular el precio por edades. 
def precio (e):
    if e>0 and e <= 2:
         precioE= 0
    elif e >2 and e <=12:
        precioE= 14
    elif e >=65:
        precioE= 18
    else:
        precioE=23    
    return precioE

#se comprueva que las claves existen en el diccionario:
def dic(key):
    if key in entrada:    #si existe, se suma uno al valor actual
        entrada[key] += 1
    else:
        entrada[key]= 1   # si no existe se crea una clave nueva con valor 1      
    return entrada

# se solicita el numero de personas que van a entrar    
while True:
    try:    
        pax= int (input("Bienvenidos al Zoo, ¿cuantas personas van a entrar? "))
        if pax < 0:             
                print ("¿Eres el listillo de turno?, no pueden entrar {} personas". format(pax))
                False
        else:
            break
    except ValueError:
        print ("Oops! Solo se permiten números ENTEROS... Nada de letras.")
        False

# se crea la variable que suma el total y una estructura de almacenamiento, el diccionario 
totalT=0
entrada = {}

#se inicia el indice del while
indice=1

#mientras el indice sea menor o igual al número de personas a entrar, se pide las edades 
while indice <= pax:
    while True:
        try:
            edad= int (input("Edad de la {}º persona: ".format (indice)))
            if edad <0:
                print ("¡¡Otra vez el listillo de turno!!, no se puede tener {} años edad". format(edad))
                False
            else:               
#se llama a  la funcion dic, se busca  si la clave existe
                dic (precio(edad))
                print ("La {}º persona de {} años paga el precio de {:.2f} €".format(indice,edad, precio(edad)))        
                indice += 1
                break

        except ValueError:
            print ("Oops! Solo se permiten números ENTEROS... Nada de letras.")
            False
    

# se imprime un retorno de carro para dar vistocidad a la factura, y otras chorradas
print ("\n")
print ("Factura simplificada, Zoo del Burro Feliz")
# se intenta ordenar el diccionario convirtiendola en una lista .sorted(miDic.items(), key=operator.itemgetter(0))
entrada= sorted(entrada.items(), key=operator.itemgetter(0))

for key in entrada:
    ## Si  usamos el diccionario sin ordenar 
    #totalT += entrada.get(key)* key
    #print ("{} entrada a precio {:.2f}€: \t\t\t {:.2f}".format (entrada.get(key), key,(entrada.get(key)* key)))
    totalT += int(round(key[0]* key[1]))
    print ("{} entrada a precio {:.2f}€: \t\t\t {:.2f}".format (key[1], key[0],(key[0]* key[1])))
print ("\t\t\t\t------")
print ("\t\t\t Total  {:.2f}€". format(totalT))

# se guarda los datos en un archivo FILE

fEntrada = open ('FicheroEntradas.txt', 'a+')
for key in entrada:
    registro = "{}-{},".format (key[1],key[0])
    print ("{},{},".format (key[1],key[0]))
    fEntrada.write (registro)
    
fEntrada.write("\n")
fEntrada.close()


