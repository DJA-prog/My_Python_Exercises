import turtle
import time
import random

timmy = turtle.Turtle()
screen = turtle.Screen()

def random_color():
    screen.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rainbow = (r,g,b)
    return rainbow

def dashed_for(sets, penOn, penOff):
    for x in range(sets):
        timmy.forward(penOn)
        timmy.penup()
        timmy.forward(penOff)
        timmy.pendown()

def dashed_back(sets, penOn, penOff):
    for x in range(sets):
        timmy.backward(penOn)
        timmy.penup()
        timmy.backward(penOff)
        timmy.pendown()