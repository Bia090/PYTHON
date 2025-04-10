import turtle

t = turtle.Turtle()
turtle.bgcolor("black")  # Schimbă culoarea fundalului
t.pensize(3)
t.speed(10)  # Viteza de generare

while True:  
    for i in range(36):  # Roția principală
        for colors in ["red", "blue", "magenta", "green", "yellow", "pink", "purple", "white"]:  # 8 culori
            t.color(colors)  # Setează culoarea curentă
            for _ in range(4):  # Desenează un pătrat
                t.forward(90)  # Mergi înainte cu 50 de unități
                t.left(90)  # Roție de 90 de grade pentru a forma un pătrat
            t.left(10)  # Roție ușoară pentru a obține efectul dorit
    t.hideturtle()  # Ascunde cursorul după desenare

turtle.mainloop()  # Menține fereastra deschisă
