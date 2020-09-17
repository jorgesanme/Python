
## entrada de datos con control de excepciones

while True:
    try:
        strnum1= int (input("Introduzca el 1º Número: "))
        strnum2= int (input("Introduzca el 2º Número: "))
    
    except ValueError:
        print ("Oops! Solo se permiten números ENTEROS... Nada de letras.")
        False
        continue            
    if strnum1 < 0 or strnum2 < 0:
        print(" No se pueden usar números negativos")
        False
    else:
        break  
   
## transformamos los caracteres STR en numeros Float
## tambien se realiza la dividicion entre 10
    
        ## Tambien se pudo 
        ## num1 = round (strnum1 / 10, 2)    
        ## num2 = round (strnum2 / 10, 2 )
    
num1= float (strnum1) /10
num2= float (strnum2) /10

## procesamiento de datos
## Se definen 4 funciones con las operaciones aritmeticas solicitadas
## Se usa el metodo round() para redondear los resultado.
## se usa el el tabulador \t y el Formateo de datos  %.2f   % ( este último es ya innecario despues de usar el Metodo round()

def sumar( num1, num2):
    suma= round (num1+num2, 2)
    print ("Suma: \t \t", num1, " + ", num2 , " = %.2f" % suma)
    print ("-----")
   
def restar ( num1, num2):
    resta= round (num1-num2, 2)
    print ("Resta: \t \t",num1, " - ", num2 , " = %.2f" % resta )
    print ("-----")

def multiplicar ( num1, num2):
    multip= round (num1*num2 , 2)
    print ("multiplicar: \t",num1, " x ", num2 , " = %.2f" % multip )
    print ("-----")

def dividir  ( num1, num2):
    dividir= round (num1/num2, 2)
    print ("Dividir: \t \t",num1, " / ", num2 , " = %.2f" % dividir )
    print ("-----")

   
## se muestra por consola el resultado de las operaciones ( ya formateado con  2 decimales)
    
print("")
sumar(num1, num2)
restar(num1, num2)
multiplicar(num1, num2)
dividir(num1, num2)

# Despedida
print("")
print ("++++++++++++++++++++++++++++++++++")
print ("+ Gracias por usar este servicio +")
print ("++++++++++++++++++++++++++++++++++")
