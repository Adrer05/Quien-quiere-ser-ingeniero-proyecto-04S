"""
Modelos SQLAlchemy para el juego 'Quien quiere ser ingeniero'
Basado en el esquema de la base de datos de Supabase
"""
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Usuario(Base):
    """Modelo base para usuarios del sistema"""
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    usuario = Column(String(50), nullable=False, unique=True)
    
    # Relaciones
    jugador = relationship("Jugador", back_populates="usuario", uselist=False)
    administrador = relationship("Administrador", back_populates="usuario", uselist=False)
    profesor = relationship("Profesor", back_populates="usuario", uselist=False)
    
    def __repr__(self):
        return f"<Usuario(id={self.id}, usuario='{self.usuario}', nombre='{self.nombre} {self.apellido}')>"


class Carrera(Base):
    """Modelo para las carreras universitarias"""
    __tablename__ = 'carrera'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    
    # Relaciones
    jugadores = relationship("Jugador", back_populates="carrera")
    semestres = relationship("Semestre", back_populates="carrera")
    
    def __repr__(self):
        return f"<Carrera(id={self.id}, nombre='{self.nombre}')>"


class Semestre(Base):
    """Modelo para los semestres de cada carrera"""
    __tablename__ = 'semestre'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, nullable=False)
    carrera_id = Column(Integer, ForeignKey('carrera.id'), nullable=True)
    
    # Relaciones
    carrera = relationship("Carrera", back_populates="semestres")
    asignaturas = relationship("Asignatura", back_populates="semestre")
    jugadores = relationship("Jugador", back_populates="semestre")
    
    def __repr__(self):
        return f"<Semestre(id={self.id}, numero={self.numero}, carrera_id={self.carrera_id})>"


class Asignatura(Base):
    """Modelo para las asignaturas"""
    __tablename__ = 'asignatura'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    semestre_id = Column(Integer, ForeignKey('semestre.id'), nullable=True)
    
    # Relaciones
    semestre = relationship("Semestre", back_populates="asignaturas")
    temas = relationship("Tema", back_populates="asignatura")
    profesores = relationship("ProfesorAsignatura", back_populates="asignatura")
    
    def __repr__(self):
        return f"<Asignatura(id={self.id}, nombre='{self.nombre}')>"


class Tema(Base):
    """Modelo para los temas de cada asignatura"""
    __tablename__ = 'tema'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    asignatura_id = Column(Integer, ForeignKey('asignatura.id'), nullable=True)
    
    # Relaciones
    asignatura = relationship("Asignatura", back_populates="temas")
    preguntas = relationship("Pregunta", back_populates="tema")
    
    def __repr__(self):
        return f"<Tema(id={self.id}, nombre='{self.nombre}')>"


class Jugador(Base):
    """Modelo para los jugadores del juego"""
    __tablename__ = 'jugador'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=True)
    carrera_id = Column(Integer, ForeignKey('carrera.id'), nullable=True)
    es_estudiante_unefa = Column(Boolean, nullable=True, default=False)
    semestre_id = Column(Integer, ForeignKey('semestre.id'), nullable=True)
    ocupacion = Column(String(100), nullable=True)
    puntuacion_total = Column(Integer, nullable=True, default=0)
    
    # Relaciones
    usuario = relationship("Usuario", back_populates="jugador")
    carrera = relationship("Carrera", back_populates="jugadores")
    semestre = relationship("Semestre", back_populates="jugadores")
    partidas = relationship("Partida", back_populates="jugador")
    ranking = relationship("Ranking", back_populates="jugador", uselist=False)
    
    def __repr__(self):
        return f"<Jugador(id={self.id}, usuario_id={self.usuario_id}, puntuacion_total={self.puntuacion_total})>"


class Administrador(Base):
    """Modelo para los administradores del sistema"""
    __tablename__ = 'administrador'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=True)
    contraseña_hash = Column(String(255), nullable=False)
    
    # Relaciones
    usuario = relationship("Usuario", back_populates="administrador")
    preguntas_creadas = relationship("Pregunta", 
                                    foreign_keys="Pregunta.creado_por_admin",
                                    back_populates="creador_admin")
    
    def __repr__(self):
        return f"<Administrador(id={self.id}, usuario_id={self.usuario_id})>"


class Profesor(Base):
    """Modelo para los profesores"""
    __tablename__ = 'profesor'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=True)
    contraseña_hash = Column(String(255), nullable=False)
    
    # Relaciones
    usuario = relationship("Usuario", back_populates="profesor")
    asignaturas = relationship("ProfesorAsignatura", back_populates="profesor")
    preguntas_creadas = relationship("Pregunta", 
                                    foreign_keys="Pregunta.creado_por_profesor",
                                    back_populates="creador_profesor")
    
    def __repr__(self):
        return f"<Profesor(id={self.id}, usuario_id={self.usuario_id})>"


class ProfesorAsignatura(Base):
    """Modelo de relación entre profesores y asignaturas"""
    __tablename__ = 'profesor_asignatura'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    profesor_id = Column(Integer, ForeignKey('profesor.id'), nullable=True)
    asignatura_id = Column(Integer, ForeignKey('asignatura.id'), nullable=True)
    
    # Relaciones
    profesor = relationship("Profesor", back_populates="asignaturas")
    asignatura = relationship("Asignatura", back_populates="profesores")
    
    def __repr__(self):
        return f"<ProfesorAsignatura(id={self.id}, profesor_id={self.profesor_id}, asignatura_id={self.asignatura_id})>"


class Pregunta(Base):
    """Modelo para las preguntas del juego"""
    __tablename__ = 'pregunta'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    texto = Column(Text, nullable=False)
    tema_id = Column(Integer, ForeignKey('tema.id'), nullable=True)
    creado_por_admin = Column(Integer, ForeignKey('administrador.id'), nullable=True)
    creado_por_profesor = Column(Integer, ForeignKey('profesor.id'), nullable=True)
    modificado_por = Column(Integer, nullable=True)
    activa = Column(Boolean, nullable=True, default=True)
    
    # Relaciones
    tema = relationship("Tema", back_populates="preguntas")
    creador_admin = relationship("Administrador", 
                                foreign_keys=[creado_por_admin],
                                back_populates="preguntas_creadas")
    creador_profesor = relationship("Profesor", 
    foreign_keys=[creado_por_profesor],
    back_populates="preguntas_creadas")
    respuestas = relationship("Respuesta", back_populates="pregunta")
    detalles_partida = relationship("DetallePartida", back_populates="pregunta")
    
    def __repr__(self):
        return f"<Pregunta(id={self.id}, tema_id={self.tema_id}, texto='{self.texto[:50]}...')>"


class Respuesta(Base):
    """Modelo para las respuestas de cada pregunta"""
    __tablename__ = 'respuesta'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    pregunta_id = Column(Integer, ForeignKey('pregunta.id'), nullable=True)
    texto = Column(Text, nullable=False)
    es_correcta = Column(Boolean, nullable=False)
    
    # Relaciones
    pregunta = relationship("Pregunta", back_populates="respuestas")
    detalles_partida = relationship("DetallePartida", back_populates="respuesta")
    
    def __repr__(self):
        return f"<Respuesta(id={self.id}, pregunta_id={self.pregunta_id}, es_correcta={self.es_correcta})>"


class Partida(Base):
    """Modelo para las partidas jugadas"""
    __tablename__ = 'partida'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    jugador_id = Column(Integer, ForeignKey('jugador.id'), nullable=True)
    puntuacion_obtenida = Column(Integer, nullable=True, default=0)
    
    # Relaciones
    jugador = relationship("Jugador", back_populates="partidas")
    detalles = relationship("DetallePartida", back_populates="partida")
    
    def __repr__(self):
        return f"<Partida(id={self.id}, jugador_id={self.jugador_id}, puntuacion={self.puntuacion_obtenida})>"


class DetallePartida(Base):
    """Modelo para los detalles de cada pregunta en una partida"""
    __tablename__ = 'detalle_partida'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    partida_id = Column(Integer, ForeignKey('partida.id'), nullable=True)
    pregunta_id = Column(Integer, ForeignKey('pregunta.id'), nullable=True)
    respuesta_id = Column(Integer, ForeignKey('respuesta.id'), nullable=True)
    acertada = Column(Boolean, nullable=False)
    puntos_obtenidos = Column(Integer, nullable=True, default=0)
    
    # Relaciones
    partida = relationship("Partida", back_populates="detalles")
    pregunta = relationship("Pregunta", back_populates="detalles_partida")
    respuesta = relationship("Respuesta", back_populates="detalles_partida")
    
    def __repr__(self):
        return f"<DetallePartida(id={self.id}, partida_id={self.partida_id}, acertada={self.acertada})>"


class Ranking(Base):
    """Modelo para el ranking de jugadores"""
    __tablename__ = 'ranking'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    jugador_id = Column(Integer, ForeignKey('jugador.id'), nullable=True)
    puntuacion_maxima = Column(Integer, nullable=True, default=0)
    
    # Relaciones
    jugador = relationship("Jugador", back_populates="ranking")
    
    def __repr__(self):
        return f"<Ranking(id={self.id}, jugador_id={self.jugador_id}, puntuacion_maxima={self.puntuacion_maxima})>"
