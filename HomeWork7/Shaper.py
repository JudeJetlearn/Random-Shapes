import turtle
import random

turtle.colormode(255)

screen = turtle.Screen()
screen.setup(width = 800, height = 600)  
screen.bgcolor("black")        
screen.tracer(0)      

Turtle = turtle.Turtle()
Turtle.shape("turtle")
Turtle.speed(0)
Turtle.color(255,255,255)
Turtle.hideturtle()

def DrawShape():

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    Shape = random.randint(1,3)
    Size = random.randint(25,100)

    Turtle.penup()
    Turtle.goto(random.randint(-400,400),random.randint(-300,300))
    Turtle.pendown()

    if Shape == 1:

        Turtle.color(r,g,b)
        Turtle.begin_fill()
            
        Turtle.circle(Size)
        Turtle.end_fill()

    elif Shape == 2:

        Turtle.color(r,g,b)
        Turtle.begin_fill()

        for i in range(4):

            Turtle.forward(Size*2)
            Turtle.right(90)

        Turtle.end_fill()
        
    elif Shape == 3:

        Turtle.color(r,g,b)
        Turtle.begin_fill()

        for i in range(3):

            Turtle.forward(Size)
            Turtle.left(120)

        Turtle.end_fill()

    screen.update()
    screen.ontimer(DrawShape, 50)

DrawShape()
turtle.mainloop()