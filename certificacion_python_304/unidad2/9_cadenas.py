#cadenas y concatenacion con(+)
cadena1='hola'
cadena2='mundo'
multilinea="""esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
#cadenas y repeticion
eco="ja"*3
print(eco)
#cambiar una cadena de minuscula a mayuscula
tu_nombre='Emily'
print(tu_nombre.upper())
#cambiar una cadena e mayuscula a minuscula
print(tu_nombre.lower())
#remplazar texto en una cadena
frase="me gusta programacion"
print(frase.replace("programacion","lengua y comunicacion"))
#formato de cadenas(f-string)
edad=16
nombre='emily'
mensaje=f"hola, me llamo {nombre} y tengo {edad} años"
print(mensaje)
#contar los caracteres de una cadena
texto = "¡felicidades por continuar en el CECYRANCH!!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#COMPROBAR SI UN TEXTO CONTIENE UNA PALABRA
oracion="aprender python es divertido"
if "pato" in oracion:
    print("encontrado")
else:
    print("no esta")
#calidad contenido de una cadena 
nlista="emy"
print(nlista.isalpha())
print(nlista.isdigit())