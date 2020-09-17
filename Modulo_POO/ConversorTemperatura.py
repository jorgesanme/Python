# se define la classe 
class Termometro():
# se definen los atributos del objeto
    def __init_(self):
        self.__unidadM = 'C'
        self.__temperatura = 0
# definir la funcion que hace la conversión de unidades        
    def conversor ( self, temperatura, unidad):
        if unidad == 'C':
            return "{}º F".format(temperatura * 9/5 +32)
        elif unidad == 'F':
            return "{}º C".format((temperatura - 32) * 5/9)
        else:
            return "unidad incorrecta"

# se mostrara la información del objeto
    def __str__(self):
        return "{}º {}".format(self.__temperatura, self.__unidadM)
    
    ## se define los setter y getter
    
    def unidadMedida (self, unidM=None):
    #Si no tiene valor para la variable, se hace getter.
        if unidM == None:
            return self.__unidadM
    #si el valor pasado es igual a una unidad valida, se hace setter.       
        else:
            if unidM == 'F' or unidM== 'C':
                self.__unidadM = unidM
    
    def temp(self, temperatura=None):
    #Si no tiene valor para la variable, se hace getter.        
        if temperatura == None:
            return self.__temperatura
    #si el valor pasado es igual a una unidad valida, se hace setter.        
        else:
            self.__temperatura = temperatura
# devolvera la media que tenga la unidad     
    def mide (self, unidM=None):
        if unidM== None or unidM == self.unidadM:
            return self.__str__()
        else:
            if unidM== 'F' or unidM== 'C':
                
                return self.__conversor(self.__temperatura,self.__unidadM)
            else:
                return self.__str__()