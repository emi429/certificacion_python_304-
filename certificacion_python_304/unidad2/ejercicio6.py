tabla = [
    ["nombre", "edad", "calificacion"],
    ["emily", 16, 9.6],
    ["carlitos", 16, 9.6],
    ["leonel", 16, 6.7],
    ["america", 15, 9.6],
    ["luis michel", 16, 6.0],
    ["sdana", 16, 9.0],
    ["carlos casillas", 16, 8.9],
    ["brian", 16, 8.9],
    ["kimberly", 15, 9.6]
]

numero = input("Ingresa un nombre: ")

filas = len(tabla)
columnas = len(tabla[0])

for i in range(filas):
    for j in range(columnas):
        if tabla[i][j] == numero:
            print("Posición:", f"[{i}][{j}]")
   