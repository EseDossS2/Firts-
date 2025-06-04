import random
import string
import os

def generar_contrasena_segura(longitud, mayusculas, minusculas, numeros, simbolos):
    """
    Genera una contraseña segura basada en los parámetros especificados.

    Args:
        longitud (int): La longitud deseada de la contraseña.
        incluir_mayusculas (bool): True si se deben incluir letras mayúsculas.
        incluir_minusculas (bool): True si se deben incluir letras minúsculas.
        incluir_numeros (bool): True si se deben incluir números.
        incluir_simbolos (bool): True si se deben incluir símbolos.

    Returns:
        str: La contraseña generada, o un mensaje de error si no se selecciona ningún tipo de caracter.
    """

    caracteres = ""
    # Se construye el conjunto de caracteres disponibles para la contraseña
    if mayusculas:
        caracteres += string.ascii_uppercase  #  letras mayúsculas (A-Z)
    if minusculas:
        caracteres += string.ascii_lowercase  #  letras minúsculas (a-z)
    if numeros:
        caracteres += string.digits           #  dígitos (0-9)
    if simbolos:
        # variedad de símbolos comunes. Puedes personalizar esto.
        caracteres += string.punctuation

    # Verifica si se ha seleccionado al menos un tipo de caracter
    if not caracteres:
        return "Error: Debes seleccionar al menos un tipo de caracter para generar la contraseña."

    # Se asegura de que la longitud sea positiva
    if longitud <= 0:
        return "Error: La longitud de la contraseña debe ser un número positivo."

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def limpiar_consola():
    """Limpia la consola para una mejor experiencia de usuario."""
    # os.system('cls') para Windows, os.system('clear') para sistemas Unix/Linux/macOS  <---
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Función principal del programa para la interacción con el usuario."""
    limpiar_consola()
    print("=========================================")
    print("  Generador de Contraseñas Seguras")
    print("=========================================")

    while True:
        try:
            longitud = int(input("\nIngrese la longitud deseada de la contraseña (ej. 12): "))
            if longitud <= 0:
                print("Por favor, ingrese un número entero positivo para la longitud.")
                continue
            break # Sale del bucle si la entrada es válida
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
    while True:
        mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower()
        if mayusculas in ('s', 'n'):
            mayusculas = True if mayusculas == 's' else False
            break
        else:
            print("Entrada inválida. Por favor, ingrese 's' para sí o 'n' para no.")

    while True:
        minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower()
        if minusculas in ('s', 'n'):
            minusculas = True if minusculas == 's' else False
            break
        else:
            print("Entrada inválida. Por favor, ingrese 's' para sí o 'n' para no.")

    while True:
        numeros = input("¿Incluir números? (s/n): ").lower()
        if numeros in ('s', 'n'):
            numeros = True if numeros == 's' else False
            break
        else:
            print("Entrada inválida. Por favor, ingrese 's' para sí o 'n' para no.")

    while True:
        simbolos = input("¿Incluir símbolos? (s/n): ").lower()
        if simbolos in ('s', 'n'):
            simbolos = True if simbolos == 's' else False
            break
        else:
            print("Entrada inválida. Por favor, ingrese 's' para sí o 'n' para no.")

    contrasena_generada = generar_contrasena_segura(
        longitud,
        mayusculas,
        minusculas,
        numeros,
        simbolos
    )

    print("\n--- Contraseña Generada ---")
    print(f"Tu contraseña segura es: {contrasena_generada}")
    print("---------------------------")

    input("\nPresiona Enter para salir...") # Mantiene la consola abierta hasta que el usuario presione Enter

if __name__ == "__main__":
    main()