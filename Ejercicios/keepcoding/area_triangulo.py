# area de un triangulo


# se define la funcion que hace la operación
def area (b, h): 
    return b*h/2

# si el programa es llamado como modulo (import)
# no se ejecutará el codigo siguiente
if __name__ == "__name__":
    # se pide al usuario introducir datos
    base = float (input ("Base: "))
    altura = float (input ("Altura: "))

    print (area( base, altura))