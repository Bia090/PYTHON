import tkinter as tk
from PIL import Image, ImageTk
import math

# Variabile globale pentru animația GIF și cerc
stop_animation = False
stop_circle = False  # Variabila pentru oprirea cercului

# Funcție pentru generarea unui fractal (arbore fractal)
def draw_fractal(canvas, x, y, length, angle, depth):
    if depth == 0:
        return
    
    # Calculăm coordonatele noii ramuri
    x_end = x + length * math.cos(math.radians(angle))
    y_end = y - length * math.sin(math.radians(angle))
    
    canvas.create_line(x, y, x_end, y_end, width=2, fill="green")
    
    # Apelăm recursiv pentru ramurile stânga și dreapta
    draw_fractal(canvas, x_end, y_end, length * 0.7, angle - 25, depth - 1)
    draw_fractal(canvas, x_end, y_end, length * 0.7, angle + 25, depth - 1)

# Funcție pentru a porni gif-ul
def start_gif():
    global stop_animation
    stop_animation = False  # Permite animația GIF
    update_gif()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

# Funcție pentru a opri gif-ul
def stop_gif():
    global stop_animation
    stop_animation = True  # Oprește animația GIF
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# Funcție pentru actualizarea gif-ului
def update_gif():
    global gif_frame, stop_animation
    if stop_animation:
        return  # Oprește animația când variabila stop_animation este True
    
    gif_frame += 1
    gif_frame %= len(gif_frames)
    canvas.create_image(200, 200, image=gif_frames[gif_frame])
    canvas.after(100, update_gif)  # actualizare la fiecare 100 ms

# Funcție pentru a desena un cerc animat pe canvas
def draw_moving_circle():
    global circle_x, circle_y, stop_circle
    if stop_circle:
        return  # Oprește animația cercului dacă variabila stop_circle este True
    
    canvas.delete("all")  # Șterge orice desen existent pe canvas
    circle_x += 5  # Deplasare pe axa X
    if circle_x > 400:  # Dacă cercul iese din canvas, îl resetăm la stânga
        circle_x = 0
    canvas.create_oval(circle_x - 25, circle_y - 25, circle_x + 25, circle_y + 25, fill="blue")
    canvas.after(30, draw_moving_circle)  # Actualizare la fiecare 30 ms pentru animație

# Funcție pentru a opri mișcarea cercului
def stop_circle_movement():
    global stop_circle
    stop_circle = True  # Oprește mișcarea cercului

# Crearea ferestrei principale
root = tk.Tk()
root.title("Interfață Grafică cu GIF și Fractal")
root.geometry("600x600")

# Canvas pentru desenare
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=20)

# Încărcarea GIF-urilor
gif_frames = []
gif_frame = 0
gif_image = Image.open("pisici.gif")  # Asigurați-vă că aveți un fișier GIF în directorul curent
for frame in range(0, gif_image.n_frames):
    gif_image.seek(frame)
    frame_image = ImageTk.PhotoImage(gif_image.copy())
    gif_frames.append(frame_image)

# Butoane pentru controlul GIF-ului
start_button = tk.Button(root, text="Start GIF", command=start_gif)
start_button.pack(side=tk.LEFT, padx=20)

stop_button = tk.Button(root, text="Stop GIF", command=stop_gif, state=tk.DISABLED)
stop_button.pack(side=tk.LEFT)

# Buton pentru a desena cercul animat
circle_button = tk.Button(root, text="Desenează Cerc Animat", command=draw_moving_circle)
circle_button.pack(pady=20)

# Buton pentru a opri mișcarea cercului
stop_circle_button = tk.Button(root, text="Oprește Cercul", command=stop_circle_movement)
stop_circle_button.pack(pady=20)

# Inițializare variabile pentru animația cercului
circle_x, circle_y = 0, 200  # Poziția inițială a cercului

# Lansați aplicația
root.mainloop()
