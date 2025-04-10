import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def animate(counter):
    # Actualizează cadrul afișat
    label.config(image=frames[counter])
    # Calculează indicele următor
    counter = (counter + 1) % len(frames)
    # Apelează funcția din nou după 100ms
    root.after(100, animate, counter)

root = tk.Tk()
root.title("GIF Animat")
root.geometry("500x500")
root.config(bg="#AED6F1")

# Deschide GIF-ul animat
gif = Image.open("pisici.gif")

# Extrage toate cadrele și redimensionează-le dacă este necesar
frames = [ImageTk.PhotoImage(frame.copy().resize((500, 500)))
          for frame in ImageSequence.Iterator(gif)]

# Creează un label pentru a afișa cadrul curent
label = tk.Label(root, bg="#AED6F1")
label.pack(pady=50)

# Pornește animația, începând cu cadrul 0
animate(0)

root.mainloop()