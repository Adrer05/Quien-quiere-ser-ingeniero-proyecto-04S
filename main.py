from preguntas import categorias
from juego import limpiar_pantalla, preguntar_listo, jugar
import os
os.system("cls")



def main():

    print("1. Matemáticas\n2. Física\n3. Unefa\n4. Venezuela\n5. Generales")
    ## buscar el tema en la base de datos
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

if __name__ == "__main__":
    main()