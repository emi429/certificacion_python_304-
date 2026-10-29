#creando un diccionario
persona={
    "nombre":"emily",
    "edad":17,
    "profesion":"programador",
    "estudiante":True
}
print(persona)
#accediendo a un valor especifico
print(persona["edad"])
#se puede usar el metodo get(), es util porque no marca el error si el valor no existe
print(persona.get("profesion"))
#modificar un valor existente
persona["edad"]=16
print(persona["edad"])
#agregar un pra(clave:valor)
persona["ciudad"]="san pepe ranch"
print(persona)