import turtle
import random
class Circuito():
    
    corredores =[]
    __posStartY = (-30,-10,10,30)
    __colorTurtle = ('red','blue','green','orange')
    
    def __init__(self, width, height):               
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightblue')
        #'lightgray'
        self.__starline = -width/2 + 10
        self.__finline = width/2 -30
        
        self.__createRunners()
        
    def __createRunners(self):        
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__starline, self.__posStartY[i])
            self.corredores.append(new_turtle)      
       
    def competir(self):
        
        hayGanador= False        
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.forward(avance +1)
            
                if tortuga.position()[0] >= self.__finline:
                    hayGanador= True
                    print ("La tortuga de color {} ha ganado".format(tortuga.color()[0]))
                    break
        
        self.corredores[i]
        
if __name__ == '__main__':
    circuito = Circuito(640, 480)
    circuito.competir()