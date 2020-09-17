# programa de becas
print ("programa de becas de este Año\n")

dista_escuela=int (input("distancia de tu casa a la escuela: "))
print(dista_escuela,"\n")

Num_her=int (input("Numero de hermanos en la escuela: "))
print(Num_her,"\n")

Salario_familia=int (input("Ingresos familiares:"))

print(Salario_familia,"\n")

# concadenamos comparadores 
if dista_escuela>40 and Num_her>2 and Salario_familia<=20000:
    print ("Tienes derecho a un beca")

else:
    print("No tiene derecho a beca")
    
    





