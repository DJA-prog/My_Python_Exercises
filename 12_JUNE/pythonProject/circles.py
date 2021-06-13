import turtle
import my_turtle

timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.pensize(5)
for x in range(36):
    screen.colormode(255)
    timmy.pencolor(my_turtle.random_color())
    timmy.right(10)
    timmy.circle(100)
    timmy.heading()

screen.exitonclick()

print(timmy)
