class Pregunta:
    def __init__(self, texto, opciones, correcta):
        self.texto = texto
        self.opciones = opciones
        self.correcta = correcta

# Definición de categorías usando objetos de la clase Pregunta
categorias = [
    # 1. Matemáticas
    [
        Pregunta("¿Cuánto es 5x3?", ["8", "15", "10", "20"], 'b'),
        Pregunta("¿Raíz cuadrada de 16?", ["3", "2", "4", "5"], 'c'),
        Pregunta("3 + 6 * 2?", ["18", "15", "20", "12"], 'b'),
        Pregunta("¿Área de un círculo?", ["pi*r^2", "2*pi*r", "r*pi", "pi*r"], 'a'),
        Pregunta("¿Cuánto es 12/4?", ["2", "3", "4", "5"], 'b'),
        Pregunta("2^3=?", ["6", "9", "8", "4"], 'c'),
        Pregunta("¿Valor de pi aprox.?", ["3.14", "2.17", "3.50", "1.61"], 'a'),
        Pregunta("15-7=?", ["8", "9", "10", "7"], 'a')
    ],
    # 2. Física
    [
        Pregunta("Unidad de fuerza:", ["Newton", "Joule", "Watt", "Volt"], 'a'),
        Pregunta("Aceleración de la gravedad (m/s^2):", ["9.8", "10.2", "12", "8.5"], 'a'),
        Pregunta("E = ?", ["mc^2", "mgh", "mv^2", "ma"], 'a'),
        Pregunta("Velocidad = ?", ["distancia/tiempo", "fuerza/masa", "trabajo/potencia", "masa/aceleracion"], 'a'),
        Pregunta("¿Carga eléctrica se mide en?", ["Newton", "Amper", "Coulomb", "Volt"], 'c'),
        Pregunta("¿Ley de inercia es de?", ["Newton", "Einstein", "Tesla", "Bohr"], 'a'),
        Pregunta("¿Un cuerpo en reposo?", ["Se mueve", "Permanece", "Explota", "Flota"], 'b'),
        Pregunta("Presión = ?", ["fuerza/area", "peso/masa", "distancia/tiempo", "masa/volumen"], 'a')
    ],
    # 3. UNEFA
    [
        Pregunta("Color de la UNEFA:", ["Azul", "Verde", "Rojo", "Amarillo"], 'a'),
        Pregunta("Rector de la UNEFA:", ["Ricardo Nicodemo Ramos", "Angelino Fernandez", "Rector C", "Rector D"], 'a'),
        Pregunta("Fundador de UNEFA:", ["Chavez", "Capriles", "Maduro", "Bello"], 'a'),
        Pregunta("Sede principal:", ["Caracas", "Maracay", "Valencia", "Barquisimeto"], 'a'),
        Pregunta("Modalidad UNEFA:", ["Presencial", "Virtual", "Ambas", "Ninguna"], 'c'),
        Pregunta("UNEFA es:", ["Privada", "Publica", "Mixta", "Internacional"], 'b'),
        Pregunta("Año fundación:", ["1999", "2000", "2003", "1998"], 'd'),
        Pregunta("UNEFA significa:", ["Univ. Nac. Exp.", "Univ. Nac. Exp. Politécnica de la FA", "Univ. Nac. Exp. de la FA", "Univ. Esp. de Form. Art."], 'b')
    ],
    # 4. Venezuela
    [
        Pregunta("Capital de Venezuela:", ["Caracas", "Maracaibo", "Valencia", "Barinas"], 'a'),
        Pregunta("Moneda actual:", ["Peso", "Dólar", "Euro", "Bolívar"], 'd'),
        Pregunta("Héroe nacional:", ["Bolívar", "Napoleón", "Madison", "Washington"], 'a'),
        Pregunta("Día de independencia:", ["5 julio", "19 abril", "24 junio", "1 enero"], 'a'),
        Pregunta("Río más largo:", ["Orinoco", "Apure", "Caroní", "Arauca"], 'a'),
        Pregunta("Estados en Venezuela:", ["20", "24", "21", "23"], 'b'),
        Pregunta("Sistema político:", ["Dictadura", "Monarquía", "República", "Feudal"], 'c'),
        Pregunta("Región petrolera:", ["Oriente", "Zulia", "Los Andes", "Llanos"], 'b')
    ],
    # 5. Generales
    [
        Pregunta("Planeta rojo:", ["Venus", "Marte", "Júpiter", "Saturno"], 'b'),
        Pregunta("Animal más rápido:", ["Tigre", "Halcón", "Chita", "Elefante"], 'c'),
        Pregunta("Año bisiesto:", ["2022", "2021", "2020", "2023"], 'c'),
        Pregunta("Inventor de la bombilla:", ["Tesla", "Edison", "Einstein", "Newton"], 'b'),
        Pregunta("Continentes:", ["6", "7", "5", "8"], 'b'),
        Pregunta("Idioma más hablado:", ["Inglés", "Chino", "Español", "Árabe"], 'b'),
        Pregunta("Red social más usada (2024):", ["Facebook", "TikTok", "Instagram", "X"], 'a'),
        Pregunta("Primer país con tren bala:", ["China", "EEUU", "Japón", "Francia"], 'c')
    ]
]