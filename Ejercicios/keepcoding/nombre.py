mes1= 31
mes2= 28
mes3= 30

diaMes=[31,28,31,30,31,30,31,31,30,31,30,31]
n = input ("¿como te llamas? ")
print("hola, ",n)

strEdad= input("¿que edad tienes? ")
strYear= input("¿en que años estamos?")
strMes= input("¿en que mes estamos?")
strDia= input("¿en que día estamos")

edad=int(strEdad)
year=int(strYear)
mes= int (strMes)
dia= int (strDia)

indice= 0
transcurrido=0


while indice < mes-1:
    transcurrido = transcurrido + diaMes[indice]
    indice= indice + 1 
    

transcurrido += dia
    
prob = (transcurrido / 365) * 100

nacimiento = year - edad

print (n, "nacistes en " , nacimiento, " con una probabilidad de:", prob)

print (" o en ", nacimiento -1, " con una probabilidad del ", 100-prob) 
   
    
             