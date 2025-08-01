# Juego realizado para la primer practica del curso
# Introducción a la Programación con Python

import random

numeroSecreto = random.randint(1, 100)
cantIntentos = 0
cantIntentosMax = 10
fueAdivinado = False

print("¡Bienvenido al juego de adivinar el número!")
print("He pensado en un número entre 1 y 100.")
print("Intenta adivinarlo.")
print(f"Tienes {cantIntentosMax} intentos para adivinar el número.") # Para traer el numero de intentos máximos f antes del texto {nombrevar} se debe poner una f, de lo contrario no se interpreta la variable

while not fueAdivinado:
    if cantIntentos >= cantIntentosMax:
        print("GAME OVER!, has agotado todos tus intentos.")
        print(f"El número era: {numeroSecreto}")
        break
    print("""-------------------------------------------------- """)
    print(f"Intento número {cantIntentos + 1} de {cantIntentosMax}.")
    print("--------------------------------------------------")

    entrada = input("Ingresa un número: ")
    numeroIngresado = int(entrada)

    if numeroIngresado == numeroSecreto:
        fueAdivinado = True
        print("¡Felicidades! Has adivinado el número.")
    elif numeroIngresado < numeroSecreto:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")

    cantIntentos += 1   