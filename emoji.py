from graphics import *

def draw_smiling_emoji():
    win = GraphWin('Smiling Emoji', 300, 300)

    # Fața (cerc galben)
    face = Circle(Point(150, 150), 100)
    face.setFill("yellow")
    face.draw(win)

    # Ochii (două cercuri negre)
    left_eye = Circle(Point(120, 120), 10)
    left_eye.setFill("black")
    left_eye.draw(win)

    right_eye = Circle(Point(180, 120), 10)
    right_eye.setFill("black")
    right_eye.draw(win)

    # Gura zâmbitoare (arc de cerc)
    smile = Circle(Point(150, 160), 40)  # Cercul ajutător pentru arc
    smile.setOutline("yellow")  # Ascundem conturul cercului
    smile.setFill("yellow")
    smile.draw(win)

    # Partea vizibilă a zâmbetului (arc din cerc)
    smile_curve = Line(Point(120, 170), Point(180, 170))  # Linia de sus a zâmbetului
    smile_curve.setWidth(3)
    smile_curve.draw(win)

    win.getMouse()  # Menține fereastra deschisă până la un click
    win.close()

draw_smiling_emoji()
