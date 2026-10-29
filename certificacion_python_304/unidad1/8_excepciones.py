
# Ejemplo 1 con manejo de excepciones

try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    resultado = numero1 / numero2
    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir un número entre cero")

except ValueError:
    print("Error: No puedes ingresar letras")

