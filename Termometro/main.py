import pygame
import sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("image/ter.jpg")
    
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados -32) *5/9
        else:
            resultado = grados
        
        return "{:10.2f}".format(resultado)
        
        
class Selector():
    __tipounidad = None
    
    def __init__(self, unidad="C"):
        self.__customes=[]
        self.__customes.append (pygame.image.load("image/fara.png"))
        self.__customes.append (pygame.image.load("image/centi.png"))
        
        self.__tipounidad = unidad
        
    def getcustome(self):
        if self.__tipounidad== 'F':
            return self.__customes[0]
        elif self.__tipounidad== 'C':
            return self.__customes[1]
        else:
            print("unidad no validad")
            pass
    
    def change(self, event):                
        if self.__tipounidad == 'F':
            self.__tipounidad = 'C'
        else:
            self.__tipounidad = 'F'
    
    def unidad(self):
        return self.__tipounidad
            
            
            
class NumberInput():
    __value = 0
    __strValue = ""
    __position = [0,0]
    __size = [0,0]
    __pointsCount = 0
    
    def __init__(self,value=0):
        
        self.__font= pygame.font.SysFont("Arial",24)
        self.value(value)

        
    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74,74,74))
        rect = textBlock.get_rect()
        rect.left= self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        return (rect, textBlock)
     
   # se define el evento pulsar una tecla numerica
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) <10 or (event.unicode=='.' and self.__pointsCount== 0):                
                self.__strValue += event.unicode
                self.value(self.__strValue)
                
                if event.unicode == '.':
                    self.__pointsCount += 1
                
            elif event.key == K_BACKSPACE:
                if self.__strValue[-1] == '.':
                    self.__pointsCount -= 1
                self.__strValue = self.__strValue[0:-1]
                self.value(self.__strValue)
                
            
    # se define setter getter
    def value(self, val=None):
        
        if val==None:
            return self.__value
        else:
            val= str(val)
            try:
                self.__value = float(val)
                self.__strValue= val
                if '.' in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount = 0
            except:
                pass
    def width(self, val=None):
        
        if val==None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
            
    def height(self, val=None):
        
        if val==None:
            return self.__size [1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
            
    def size(self, val=None):
        
        if val==None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])] 
            except:
                pass
            
    def posX(self, val=None):
                
         if val==None:
             return self.__position[0]
         else:            
             try:
                self.__position[0] = int(val)
             except:
                 pass
            
    def posY(self, val=None):
        
        if val==None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
            
    def pos(self, val=None):
        
        if val==None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])] 
            except:
                pass
        

class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode( (290,425) )
        pygame.display.set_caption("Termómetro")
        self.__screen.fill( (244, 236, 203) )
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.pos((106,58))
        self.entrada.size((133,28))
        
        self.selector= Selector()
                                      
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
                self.entrada.on_event(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:                    
                    self.selector.change(event)
                    grados = self.entrada.value()
                    nuevaUnidad= self.selector.unidad()
                    temperatura= self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.value((temperatura))
                    
                    
            # se pinta el termómetro en su posición
            self.__screen.blit(self.termometro.custome, (2, 10))
                        
            #se pinta el cuadro de texto
            text = self.entrada.render() #se obtiene rectáncuglo blanco y foto de texto, se asigna a variable text
            pygame.draw.rect(self.__screen, (255,255,255), text[0]) # creamos el rectangulo blanco con sus datos (pos y tamaño) text[0]
            self.__screen.blit(text[1], self.entrada.pos())
            pygame.display.flip()
            
            # se pinta el selector 
            self.__screen.blit(self.selector.getcustome(), (100,153) )
            
if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()