import turtle 

t = turtle.Turtle() 
turtle.bgcolor("grey") 
t.pensize(3) 
t.speed(10) 

while True:  
    for i in range(4):  
        for colors in ["red", "blue", "magenta", "green" , "yellow" , "pink" , "purple" , "white"]:  
            t.color(colors)  
            t.circle(50)  
            t.left(10)  
    t.hideturtle()  # Ascunde cursorul după desenare

turtle.mainloop()  # Menține fereastra deschisă
