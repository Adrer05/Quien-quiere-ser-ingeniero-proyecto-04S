from preguntas import categorias
from juego import limpiar_pantalla, preguntar_listo, jugar
import os
os.system("cls")

def main():
    nombre = input("Bienvenido al Juego de Preguntas ¡Quién quiere ser Ing!\nIngresa tu nombre: ")
    puntaje = 0

    limpiar_pantalla()
    print(f"Hola, {nombre}. Selecciona el tema:")
    print("1. Matemáticas\n2. Física\n3. Unefa\n4. Venezuela\n5. Generales")
    
    try:
        tema = int(input("Opción: "))
        if not preguntar_listo():
            print("¡Hasta la próxima!")
            return

        if 1 <= tema <= 5:
            puntaje = jugar(categorias[tema - 1], puntaje)
        else:
            print("Opción inválida.")
            return
    except ValueError:
        print("Debes ingresar un número.")
        return

    limpiar_pantalla()
    print(f"Juego finalizado, {nombre}. Tu récord: {puntaje} puntos.")

    # Guardado en archivo
    with open("record_jugadores.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} - {puntaje} pts\n")

if __name__ == "__main__":
    main()