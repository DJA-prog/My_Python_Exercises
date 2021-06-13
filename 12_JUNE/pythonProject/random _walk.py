import turtle
import random
import my_turtle

shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
ortho = [0, 90, 180, 360]
lengt = [0, 20, -20]

timmy = turtle.Turtle()
screen = turtle.Screen()

for x in range(1000):
    timmy.shape(random.choice(shapes))
    timmy.right(random.choice(ortho))
    timmy.forward(random.choice(lengt))
    screen.colormode(255)
    timmy.pencolor(my_turtle.random_color())
    timmy.pensize(5)

screen.exitonclick()

print(timmy)