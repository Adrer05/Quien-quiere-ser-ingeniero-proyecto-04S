import customtkinter as ctk
import os
os.system("cls")

DATABASE_URL = os.getenv("DATABASE_URL")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x600")
app.title("Main")

# Frame login
frame_login = ctk.CTkFrame(app, width=350, height=400)
# Frame register
frame_register = ctk.CTkFrame(app, width=350, height=400)

# ========== FRAME LOGIN ==========
titulo_bienvenida = ctk.CTkLabel(frame_login, text="Bienvenido a Quien Quiere Ser Ingeniero?", font=("Arial", 28))
titulo_bienvenida.pack(pady=30)

titulo_login = ctk.CTkLabel(frame_login, text="Iniciar Sesión", font=("Arial", 24))
titulo_login.pack(pady=30)

usuario_login = ctk.CTkEntry(frame_login, placeholder_text="Usuario", width=250)
usuario_login.pack(pady=15)

password_login = ctk.CTkEntry(frame_login, placeholder_text="Contraseña", show="*", width=250)
password_login.pack(pady=15)

# Resultado
resultado_login = ctk.CTkLabel(frame_login, text="", font=("Arial", 14))
resultado_login.pack(pady=10)

def login():
    user = usuario_login.get()
    pwd = password_login.get()
    print(f"Usuario: {user}, Password: {pwd}")
    resultado_login.configure(text=f"Bienvenido {user}!")

boton_login = ctk.CTkButton(frame_login, text="Entrar", command=login, width=250)
boton_login.pack(pady=20)

boton_ir_registro = ctk.CTkButton(frame_login, text="Registrarse", command=lambda: mostrar_frame(frame_register), width=250)
boton_ir_registro.pack(pady=1)

# ========== FRAME REGISTER ==========
titulo_register_1 = ctk.CTkLabel(frame_register, text="Este es el primer paso para convertirte en un gran Ingeniero", font=("Arial", 20))
titulo_register_1.pack(pady=30)

titulo_register_2 = ctk.CTkLabel(frame_register, text="Registrarse", font=("Arial", 24))
titulo_register_2.pack(pady=30)

usuario_register = ctk.CTkEntry(frame_register, placeholder_text="Usuario", width=250)
usuario_register.pack(pady=15)

password_register = ctk.CTkEntry(frame_register, placeholder_text="Contraseña", show="*", width=250)
password_register.pack(pady=15)

eleccion_rol = ctk.CTkComboBox(
    frame_register,
    values=["Administrador", "Profesor", "Jugador"]
)
eleccion_rol.pack(pady=20)

boton_volver_login = ctk.CTkButton(frame_register, text="Volver al login", command=lambda: mostrar_frame(frame_login), width=250)
boton_volver_login.pack(pady=1)

# ========== FUNCIÓN PARA CAMBIAR FRAMES ==========
def mostrar_frame(frame_a_mostrar):
    # Ocultar TODOS los frames
    frame_login.pack_forget()
    frame_register.pack_forget()
    
    # Mostrar el frame deseado
    frame_a_mostrar.pack(fill="both", expand=True, padx=20, pady=20)

# Mostrar frame de login al inicio
mostrar_frame(frame_login)

# Botón cerrar
def cerrar_app():
    app.quit()
    app.destroy()

boton_cerrar = ctk.CTkButton(
    app, 
    text="Cerrar", 
    command=cerrar_app,
    fg_color="red"
)
boton_cerrar.pack(pady=10)

app.mainloop()