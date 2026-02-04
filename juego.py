import os
import time
import threading
import sys

def limpiar_pantalla():
    # Detecta si es Windows o Unix 
    os.system('cls' if os.name == 'nt' else 'clear')

def preguntar_listo():
    listo = input("¿Estás listo para comenzar? (s/n): ").lower()
    return listo == 's'

def temporizador(segundos, evento_detener):
    """Muestra el tiempo mientras el usuario no responda."""
    for i in range(segundos, 0, -1):
        if evento_detener.is_set():
            break
        # \r permite sobrescribir la misma línea en la consola
        sys.stdout.write(f"\rTiempo restante: {i} segundos ")
        sys.stdout.flush()
        time.sleep(1)
    if not evento_detener.is_set():
        print("\n¡Tiempo agotado! Presiona Enter para continuar...")

def jugar(preguntas, puntaje):
    for p in preguntas:
        limpiar_pantalla()
        print(f"{p.texto}")
        letras = ['a', 'b', 'c', 'd']
        for i, opcion in enumerate(p.opciones):
            print(f"{letras[i]}) {opcion}")

        # Usamos un evento para detener el hilo del temporizador
        detener_timer = threading.Event()
        t = threading.Thread(target=temporizador, args=(15, detener_timer))
        t.daemon = True # El hilo muere si el programa principal termina
        t.start()

        r = input("\nTu respuesta (a/b/c/d): ").lower()
        detener_timer.set() # Avisamos al timer que se detenga

        if r == p.correcta:
            print("¡Correcto! +10 puntos")
            puntaje += 10
        else:
            print(f"Incorrecto. La respuesta era '{p.correcta}'")
        
        time.sleep(2)
    return puntaje