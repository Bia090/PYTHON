from graphics import *

def main():
    win = GraphWin('My Graphics', 300, 250)  # Creează fereastra grafică
    g = Point(150, 150)  # Creează un punct la coordonatele (150, 150)
    g.draw(win)  # Desenează punctul în fereastră
    win.getMouse()  # Așteaptă un click pentru a menține fereastra deschisă
    win.close()  # Închide fereastra după click

main()