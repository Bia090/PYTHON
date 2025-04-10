from graphics import *

def main():
    win = GraphWin('My Graphics', 300, 250)  # Specifică dimensiunea ferestrei
    
    center = Point(150, 125)  # Creează un punct în centrul ferestrei
    circle = Circle(center, 50)  # Creează un cerc cu raza de 50
    circle.setOutline("blue")  # Setează culoarea conturului
    circle.setWidth(2)  # Setează grosimea liniei
    circle.draw(win)  # Desenează cercul în fereastră
    
    win.getMouse()  # Așteaptă un click înainte de a închide
    win.close()

main()