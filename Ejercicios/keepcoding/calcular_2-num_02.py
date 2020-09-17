
## entrada de datos con control de excepciones
strnum1= input("Introduzca el 1º Número: ")
strnum2= input("Introduzca el 2º Número: ")

comp= False
while not comp:
    
    if strnum1.isdigit() and strnum2.isdigit():
        num1= int (strnum1)
        num2= int (strnum2)
        comp= True
        
    elif strnum1[0] !='' and strnum1[0] == '-' and strnum1[1:0].isdigit():
        strnum1= int (strnum1)
        
    elif  strnum2[0] !='' and strnum2[0] == '-' and strnum2[1:0].isdigit():
        strnum2= int (strnum2)
        
    else:
        print(" numeros enteros en positivo")
        
    

## transformamos los caracteres STR en numeros Float
## tambien se realiza la dividicion entre 10
        
num1= float (strnum1) /10
num2= float (strnum2) /10

## procesamiento de datos
## Se definen 4 funciones con las operaciones aritmeticas solicitadas

def sumar( num1, num2):
    suma= round (num1+num2, 2)
    print ("Suma: \t \t", num1, " + ", num2 , " = %.2f" % suma)
    print ("-----")
   
def restar ( num1, num2):
    resta= round (num1-num2, 2)
    print ("Resta: \t",num1, " - ", num2 , " = %.2f" % resta )
    print ("-----")

def multiplicar ( num1, num2):
    multip= round (num1*num2 , 2)
    print ("multiplicar: \t",num1, " X ", num2 , " = %.2f" % multip )
    print ("-----")

def dividir  ( num1, num2):
    dividir= round (num1/num2, 2)
    print ("Dividir: \t",num1, " / ", num2 , " = %.2f" % dividir )
    print ("-----")

   
## se muestra por consola el resultado de las operaciones ( ya formateado con  2 decimales)
    
print("")
sumar(num1, num2)
restar(num1, num2)
multiplicar(num1, num2)
dividir(num1, num2)

# Despedida
print ("Gracias por usar este servicio")

