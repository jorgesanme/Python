import pygame
import sys
import random

class Runners():    
    __customes = ('emiko','weo','yo','fefa')
    
    
    def __init__(self, x=0, y=0, custome=None):
        
        ixCustome = random.randint(0,3)
                
        self.custome = pygame.image.load("Image/{}.png".format(self.__customes[ixCustome]))
        self.position = [x,y]
        self.name = self.__customes[ixCustome]
        
    def avanzar(self):
        self.position[0] += random.randint(0,5)-1


class Game():
    runners = []
    __posY= (90,160,230,310)
    __names= ('emiko','weo','yo','fefa')
    __starline= -5
    __finline= 600    
        
    def __init__ (self):
        # definir la pantalla
        self.__screen =  pygame.display.set_mode((640,480)) # tamaño de la pantalla
        pygame.display.set_caption("Carrera de Bichitos") # titulo de la pantalla
        self.background = pygame.image.load("Image/background.png")
        # fin pantalla
        
        # se crean los corredores en la lista 
        for i in  range(4):
            
            elRunner = Runners(self.__starline, self.__posY[i])
            elRunner.name = self.__names[i]
            self.runners.append(elRunner)
                    
    def close(self):
        pygame.quit()
        sys.exit()
    def competir(self):       
   #se crea los metodos que inician el grupo de actividades del juego     
        hayGanador = False
        
        while not hayGanador:
            #comprobacion de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    hayGanador= True
            
            # bucle para avanzar cada uno de los corredores
            for runners in self.runners:                
                runners.avanzar()
            
            # bucle para determinar el ganador y final del juego
          
                if runners.position[0] >=self.__finline:
                    print("{} ha ganado".format(runners.name))
                    hayGanador = True
            
            
            # Refrescar/ renderizar la pantalla
            
            self.__screen.blit(self.background, (0,0) ) # se pinta la pantalla con el fondo  
            
            # se pinta en la pantalla con los runners
            for runners in self.runners:
                self.__screen.blit(runners.custome, runners.position)              
                           
            pygame.display.flip()
        
        while True:
            # se lanza escucha de eventos a la espera de cerrar ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                   
        

if __name__ == '__main__':
    #iniciar el juego
    pygame.init()
    game = Game()
    game.competir()