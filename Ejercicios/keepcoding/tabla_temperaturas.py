# se diseña un programa que convierta Fahrenheit a Centigrados.
#
def fahrenheitToCentrigados(g):
    return (g-32)* 5/9

def centigradosToFahrenheit(g):
    return (g*9/5)+32

def centigrados(ini, fin):
    print ("ºF --> ºC")
    for grados in range(ini, fin+10, 10):
        print("{}ºF\t \t {}ºC".format(grados,  round (fahrenheitToCentrigados(grados),2)))

def fahrenheit(ini, fin):
    print ("ºC --> ºF")
    for fahrenheit in range (ini, fin+10,10):
        print ("{}ºC\t \t {}ºF" .format(fahrenheit, round (centigradosToFahrenheit(fahrenheit),2))) # round (valor/variable, decimales) --> round (grados, 2 )

strtipo = input (" Salida ( F / C ) ")

if strtipo.islower():
    tipo= strtipo.upper()
else:
    tipo= strtipo


if tipo == 'C':
    centigrados(0,230)
elif tipo == 'F':
    fahrenheit(0,100)
else:
    print("tipo incorrecto")