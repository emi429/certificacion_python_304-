#el mapa del tesoro
mapa=[
    [".",".",".","."],
    [".",".","X","."],
    [".",".",".","."],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa)
#recorriendo las matriz con ciclos anidados
#ciclo externo para manejar filas(i)
for i in range(filas):
    for j in range(columnas):
        if mapa[i][j]=="X":
            print(f"Mapa encontrado en la posicion [{i}][{j}]") 
