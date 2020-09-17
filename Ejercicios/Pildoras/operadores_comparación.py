# evaluar salarios de una empresa, condiciones y
# concadenación de operadores comparación

salario_presi= int (input("cuanto cobra este Presi: "))

print("El Presi cobra: "+ str(salario_presi))

salario_direc= int (input("cuanto cobra el director: "))


print("El Director cobra: "+ str(salario_direc))

salario_adminis= int (input("cuanto cobra el Administrativo: "))

print("El Administrativo cobra: "+ str(salario_adminis))

# aqui se ve la concadenación de comparadores
if salario_adminis < salario_direc < salario_presi:
    print("Todos cobran lo suyo")
else:
    print("alguien esta estafando a la empresa")
    
