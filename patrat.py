from graphics import *

def draw_square():
    win = GraphWin('Square', 300, 300)  # Creează fereastra grafică
    square = Rectangle(Point(100, 100), Point(200, 200))  # Creează un pătrat
    square.draw(win)  # Desenează pătratul
    win.getMouse()  # Așteaptă un click pentru a menține fereastra deschisă
    win.close()

draw_square()
