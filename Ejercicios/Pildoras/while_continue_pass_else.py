#continue , pass y else

for letra in "Python mola  mucho coño":
    if letra== "h":
        continue # omite el print y comienza el siguiente siclo de iterador FOR
      
    print (letra, end="")

#Al terminar el bucle, se le dice que haga esto otro, pertenece al bucle for
else:
    print ("\nse ha impreso todo el texto")