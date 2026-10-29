#creando una tupla
coordenadas=(10.5,20.3,30.5,10.5)#tupla numerica
nombres=("luis","ana","angel")#tupla de cadena de texto 
coordenadas[0]=10.9
for indice,coordenada in enumerate(coordenadas):
    print(f"indice[{indice}]-----coordenada[{coordenada}]")