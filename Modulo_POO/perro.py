# los obejtos se construyen casi igual que en java.
# simplemente aprender la sintaxis

class Perro():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self, *l): # se le puede poner una cadena o el ( *l) que nos permite pasarle cualquier parametro incluso lista o diccionarios
        if self.peso>=8:
            print ("superGUAU, superGua", *l)
        else:
            print ("miniguau,miniguau,miniguau,", *l)
   
   # se define la funcion que nos devuelve los atributos que tiene cada objeto
   # resultado al hacer print(nombre-objeto) 
    def __str__(self):
        return "Mi nombre es {}, tengo {} años de edad y peso {} kg".format (self.nombre, self.edad, self.peso)

## se escribe una herencia para perro de asistencia
    
class PerroAsistencia(Perro):
        def ___init__(self,nombre, edad, peso, amo ):
            self.amo= amo
            #se inicia las atributos desde superclase (upper en java)
            Perro.__init__(self, nombre, edad, peso)
            #se inicia el tributo especifico de la clase hija.
            self.amo = amo
            
        