"""
Script de prueba para verificar la conexión y los modelos
"""
from config_bd import Session, test_connection
from models import (
    Usuario, Carrera, Semestre, Asignatura, Tema,
    Jugador, Administrador, Profesor, ProfesorAsignatura,
    Pregunta, Respuesta, Partida, DetallePartida, Ranking
)


def test_models():
    """Prueba los modelos consultando la base de datos"""
    
    print("\n" + "="*50)
    print("PRUEBA DE MODELOS Y CONEXIÓN")
    print("="*50 + "\n")
    
    # Probar conexión
    if not test_connection():
        print("No se pudo conectar a la base de datos")
        return
    
    db = Session()
    
    try:
        # Probar consultas básicas
        print("\n1. Probando modelo Usuario:")
        usuarios = db.query(Usuario).limit(5).all()
        print(f"   Total de usuarios (primeros 5): {len(usuarios)}")
        for usuario in usuarios:
            print(f"   - {usuario}")
        
        print("\n2. Probando modelo Carrera:")
        carreras = db.query(Carrera).all()
        print(f"   Total de carreras: {len(carreras)}")
        for carrera in carreras:
            print(f"   - {carrera}")
        
        print("\n3. Probando modelo Asignatura:")
        asignaturas = db.query(Asignatura).limit(5).all()
        print(f"   Total de asignaturas (primeras 5): {len(asignaturas)}")
        for asignatura in asignaturas:
            print(f"   - {asignatura}")
        
        print("\n4. Probando modelo Pregunta:")
        preguntas = db.query(Pregunta).filter(Pregunta.activa == True).limit(5).all()
        print(f"   Total de preguntas activas (primeras 5): {len(preguntas)}")
        for pregunta in preguntas:
            print(f"   - {pregunta}")
        
        print("\n5. Probando modelo Jugador:")
        jugadores = db.query(Jugador).limit(5).all()
        print(f"   Total de jugadores (primeros 5): {len(jugadores)}")
        for jugador in jugadores:
            print(f"   - {jugador}")
        
        print("\n6. Probando modelo Partida:")
        partidas = db.query(Partida).limit(5).all()
        print(f"   Total de partidas (primeras 5): {len(partidas)}")
        for partida in partidas:
            print(f"   - {partida}")
        
        print("\n7. Probando relaciones:")
        # Probar relación Pregunta -> Respuestas
        pregunta = db.query(Pregunta).first()
        if pregunta:
            print(f"   Pregunta: {pregunta.texto[:50]}...")
            print(f"   Respuestas: {len(pregunta.respuestas)}")
            for respuesta in pregunta.respuestas:
                correcta = "✓" if respuesta.es_correcta else "✗"
                print(f"     {correcta} {respuesta.texto[:50]}...")
        
        print("\n✓ Todas las pruebas completadas exitosamente")
        
    except Exception as e:
        print(f"\n✗ Error durante las pruebas: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        db.close()


def consulta_personalizada():
    """Ejemplo de consulta personalizada"""
    db = Session()
    
    try:
        # Ejemplo: Obtener todas las preguntas de un tema específico
        print("\n" + "="*50)
        print("CONSULTA PERSONALIZADA")
        print("="*50 + "\n")
        
        # Contar preguntas por tema
        from sqlalchemy import func
        
        resultado = db.query(
            Tema.nombre,
            func.count(Pregunta.id).label('total_preguntas')
        ).join(
            Pregunta, Tema.id == Pregunta.tema_id
        ).group_by(
            Tema.nombre
        ).all()
        
        print("Preguntas por tema:")
        for tema, total in resultado:
            print(f"   - {tema}: {total} preguntas")
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        db.close()


if __name__ == "__main__":
    test_models()
    consulta_personalizada()
