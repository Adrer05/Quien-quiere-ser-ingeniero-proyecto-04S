import os
os.system("cls")
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
DATABASE_URL = os.getenv("DATABASE_URL")
# Connect to the database
try:
    connection = psycopg2.connect(DATABASE_URL)
    print("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)
except Exception as e:
    print(f"Failed to connect: {e}")

try:
    cursor.execute("SELECT * FROM usuario")

    # 4. Obtener y mostrar los resultados
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except:
    print("hola")