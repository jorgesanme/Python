from tkinter import *
from tkinter import ttk

# el frame principal o ventana de la aplicación root = Tk()
# root = Tk()  la podemos llamar tambien mainWindow
# tamaño y nombre de la ventana

class mainApp(Tk): # la pantalla principal hereda de Tk()
    
    size = "220x250"
    entrada = None
    tipoUnidad = None
    
    __temperaturaAnte = ""
    
    def __init__(self):
        Tk.__init__(self)  # se inicia el contructor de Tk con el valor de
                            # de nuestro propio __init__
             
        self.geometry(self.size)
        self.title("Termómetro con Tkinter")
        self.configure(bg = "#0accb3")
        self.resizable(0,0)
        
        # se usa una variable de control llamada StringVar()
        self.temperatura = StringVar(value="")
        self.temperatura.trace("w", self.validateTemperature)
        self.tipoUnidad= StringVar(value="C")
        
        self.createLayout()
        
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable= self.temperatura).place(x=5, y=10)
        self.lblUnidad = ttk.Label(self, text="Grados:").place(x=10, y=45)
        self.rb1 = ttk.Radiobutton(self, text="Fahrenheit", variable= self.tipoUnidad, value="F", command=self.selected).place(x=30, y=75)
        self.rb2 = ttk.Radiobutton(self, text="Celcius", variable= self.tipoUnidad, value="C", command=self.selected).place(x=30, y=105)
   
    def start(self):
       self.mainloop()
       
    def validateTemperature(self, *args):
        
        nuevoValor = self.temperatura.get()
        print("NuevoValor: ",nuevoValor, "vs valorAnteior",self.__temperaturaAnte)
        try:
            
            float(nuevoValor)
            self.__temperaturaAnte = nuevoValor
            print ("Fija-valorAnterior: ",self.__temperaturaAnte)
        except:
            self.temperatura.set(self.__temperaturaAnte)
            print ("RecuperavalorAnterior: ",self.__temperaturaAnte)
    
    def selected(self):
        resultado = 0
        toUnidad = self.tipoUnidad.get()
        grados = float(self.temperatura.get())
        
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
        
        self.temperatura.set (resultado)
        
        

#inicia la ventana 
if __name__ == '__main__':
    app= mainApp()
    app.start()
