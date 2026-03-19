import random
words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
    ]
word = random.choice(words)
guessed = []
attempts = 6
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    if "_" not in progress: # Verificar si el jugador ya adivinó la palabra completa
        puntaje += 6
        print(f"¡Ganaste! Hiciste un puntaje de: {puntaje}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ").lower()
    while len(letter) != 1 or not letter.isalpha():
        print("Entrada no valida")
        letter = input("Ingresá una letra: ").lower()

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
        puntaje -= 1
        
    print()
else:
    puntaje = 0
    print(f"¡Perdiste! La palabra era: {word} tu puntaje fue: {puntaje}")