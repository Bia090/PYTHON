from graphics import *

def draw_colored_squares():
    win = GraphWin('Three Squares', 300, 300)  # Creează fereastra grafică
    
    red_square = Rectangle(Point(50, 50), Point(150, 150))  
    red_square.setFill("red")
    red_square.draw(win)
    
    green_square = Rectangle(Point(150, 50), Point(250, 150))  
    green_square.setFill("green")
    green_square.draw(win)
    
    blue_square = Rectangle(Point(100, 150), Point(200, 250))  
    blue_square.setFill("blue")
    blue_square.draw(win)
    
    win.getMouse()  # Așteaptă un click pentru a menține fereastra deschisă
    win.close()

draw_colored_squares()
