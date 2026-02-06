"""
Configuración de la base de datos con SQLAlchemy y Supabase
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
from models import Base

# Cargar variables de entorno
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el engine de SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    echo=False,  # Cambiar a True para ver las consultas SQL en consola
    pool_pre_ping=True,  # Verifica la conexión antes de usarla
    pool_size=10,  # Número de conexiones en el pool
    max_overflow=20  # Conexiones adicionales si el pool está lleno
)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(SessionLocal)


def get_db():
    """
    Función para obtener una sesión de base de datos.
    Útil para usar con context managers.
    
    Uso:
        with get_db() as db:
            jugadores = db.query(Jugador).all()
    """
    db = Session()
    try:
        yield db
    finally:
        db.close()




def test_connection():
    """
    Prueba la conexión a la base de datos
    """
    try:
        from sqlalchemy import text
        db = Session()
        # Intentar ejecutar una consulta simple
        result = db.execute(text("SELECT * FROM usuario"))
        db.close()
        print("✓ Conexión exitosa a Supabase")
        return True
    except Exception as e:
        print(f"✗ Error de conexión: {e}")
        return False

if __name__ == "__main__":
    # Prueba la conexión cuando se ejecuta directamente
    test_connection()
