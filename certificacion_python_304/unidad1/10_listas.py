#Declarando una lista
try:
    materias=["programacion","filosofia","matematicas","ingles"]
    print(materias[2])
    materias.append("lengua y comunicacion")
    print(materias)
    materias[1]="biologia"
    print(materias)
    materias.remove("matematicas")
    print(materias)
except IndexError:
     print("ESE INDICE NO EXISTE")