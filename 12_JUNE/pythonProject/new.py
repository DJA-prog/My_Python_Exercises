import turtle
import time
import random

timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.shape("turtle")
timmy.color("green")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_color = (r, g, b)
    return turtle_color

# for x in range(0, 4):
#     timmy.left(90)
#     timmy.forward(100)
#
# time.sleep(2)
#
# for x in range(0, 4):
#     timmy.right(90)
#     timmy.forward(100)
#
# time.sleep(2)
#
# for x in range(0, 4):
#     timmy.left(90)
#     timmy.backward(100)
#
# time.sleep(2)
#
# for x in range(0, 4):
#     timmy.right(90)
#     timmy.backward(100)

def dashed_for():
    for x in range(5):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

def dashed_back():
    for x in range(5):
        timmy.backward(10)
        timmy.penup()
        timmy.backward(10)
        timmy.pendown()

# for x in range(0, 4):
#     timmy.left(90)
#     dashed_for()
#
# time.sleep(2)
#
# for x in range(0, 4):
#     timmy.right(90)
#     dashed_for()
#
# time.sleep(2)
#
# for x in range(0, 4):
#     timmy.left(90)
#     dashed_back()
#
# time.sleep(2)
#
# for x in range(0, 4):
#     timmy.right(90)
#     dashed_back()

color = ["silver", "red", "blue", "green", "orange", "purple", "yellow", "violet", "pink"]

def shape(angle, sides):
    for z in range(sides):
        timmy.right(angle)
        dashed_for()



for x in range(3, 10):
    timmy.pencolor(random_color())
    shape(360/x, x)



screen.exitonclick()

print(timmy)

random.choice(0, 90, 180, 360)