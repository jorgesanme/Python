def evalua(nota):
    valoracion="aprobado"
    if nota<0:
        print("nota no validad")
    elif 0<nota<5:
        return "suspenso"
    elif 0<nota>=5 and nota<6:
        return "aprobado"
    elif 0<nota>=6 and nota<8:
        return "bien"
    elif nota>=8 and nota<9:
        return "notable"
    else:
        return "sobresaliente"


nota= int (input("introduzca nota: "))

print(evalua(nota))

if nota in range(0, 5):
    print(" hay que estudiar más")
    