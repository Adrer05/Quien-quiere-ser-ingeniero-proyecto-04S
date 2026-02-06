import customtkinter as ctk
import os

os.system("cls")

import customtkinter as ctk

app = ctk.CTk()
app.geometry("500x400")

# Crear TODOS los frames al inicio
frame_inicio = ctk.CTkFrame(app)
frame_config = ctk.CTkFrame(app)

# Contenido del frame de inicio
label_inicio = ctk.CTkLabel(frame_inicio, text="Pantalla de Inicio", font=("Arial", 24))
label_inicio.pack(pady=50)

boton_a_config = ctk.CTkButton(frame_inicio, text="Ir a Configuración", 
                                command=lambda: mostrar_frame(frame_config))
boton_a_config.pack(pady=20)

# Contenido del frame de configuración
label_config = ctk.CTkLabel(frame_config, text="Configuración", font=("Arial", 24))
label_config.pack(pady=50)

boton_a_inicio = ctk.CTkButton(frame_config, text="Volver al Inicio", 
                                command=lambda: mostrar_frame(frame_inicio))
boton_a_inicio.pack(pady=20)

def mostrar_frame(frame):
    # Ocultar todos los frames
    frame_inicio.pack_forget()
    frame_config.pack_forget()
    
    # Mostrar el frame deseado
    frame.pack(fill="both", expand=True)

# Mostrar el frame inicial
mostrar_frame(frame_inicio)

app.mainloop()