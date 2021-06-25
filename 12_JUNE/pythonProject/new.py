import turtle as t
import random
import colorgram

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
timmy = t.Turtle()
screen = t.Screen()

e_colors = []
colors = colorgram.extract('img.png', 3)

for z in range(3):
    c_color = colors[z].rgb
    #c_color = colors[z].hsl
    r = c_color[0]
    g = c_color[1]
    b = c_color[2]
    rainbow = (r, g, b)
    e_colors.append(rainbow)
print(e_colors)

timmy.penup()
timmy.right(90)
timmy.forward(200)
timmy.right(90)
timmy.forward(200)
timmy.right(180)
for x in range(10):
    for y in range(10):
        timmy.pendown()
        screen.colormode(255)
        # timmy.pencolor(random.choice(e_colors))
        timmy.dot(20, random.choice(e_colors))
        # timmy.dot(20, "red")
        timmy.penup()
        timmy.forward(50)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.right(180)

screen.exitonclick()

print(timmy)
