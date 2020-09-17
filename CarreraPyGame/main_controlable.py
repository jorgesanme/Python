import pygame
from pygame.locals import*
import sys
import random

class Runners():    
    __customes = ('emiko','weo','yo','fefa')
    
    
    def __init__(self, x=0, y=0, custome=None):
        
        ixCustome = random.randint(0,3)
                
        self.custome = pygame.image.load("Image/{}.png".format(self.__customes[ixCustome]))
        self.position = [x,y]
        self.name = self.__customes[ixCustome]
        
class Game():
    def __init__ (self):
        # definir la pantalla
        self.__screen =  pygame.display.set_mode((640,480)) # tamaño de la pantalla
        pygame.display.set_caption("Carrera de Bichitos") # titulo de la pantalla
        self.background = pygame.image.load("Image/background.png")
        # fin pantalla
        
        self.runner = Runners(320,240)
        
    def start(self):
        
        gameOver = False
        
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        # se programa mover hacia arriba el runner
                        self.runner.position[1] -= 5                    
                        
                    elif event.key == K_DOWN:
                        # MUEVE ABAJO
                        self.runner.position[1] += 5
                        
                    elif event.key == K_LEFT:
                        # MUEVE IZQUIERDA
                        self.runner.position[0] -= 5
                        
                    elif event.key == K_RIGHT:
                        # VUEME DERECHA.
                        self.runner.position[0] += 5
                    else:
                        pass
                
                self.__screen.blit(self.background, (0, 0))
                self.__screen.blit(self.runner.custome, self.runner.position)
                
                pygame.display.flip()
            

if __name__ == '__main__':
    
    game = Game()
    pygame.font.init()
    game.start()
