from graphics import *

def main():
    win = GraphWin('Multiple Circles', 400, 300)  # Fereastra de 400x300
    
    # Lista cu centrele cercurilor și razele lor
    circles_data = [
   
        (Point(200, 150), 50, "red"),
        (Point(150, 220), 20, "yellow"),
    ]
    
    # Desenează fiecare cerc
    for center, radius, color in circles_data:
        circle = Circle(center, radius)
        circle.setFill(color)  # Umple cercul cu culoarea specificată
        circle.setOutline("black")  # Contur negru
        circle.setWidth(2)  # Grosime contur
        circle.draw(win)

    win.getMouse()  # Așteaptă un click pentru a închide fereastra
    win.close()

main()