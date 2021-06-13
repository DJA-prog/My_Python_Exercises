import turtle as t
import random
import colorgram
num = [0,1,2,3,4,5,6,7,8,9]
timmy = t.Turtle()
screen = t.Screen()

ecolors = []
colors = colorgram.extract('img.png', 3)

for z in range(3):
    ccolor = colors[z].rgb
    #hex_color = ""
    # a=0
    # for y in ccolor:
    #     a+=1
    #     if (a < 3):
    #         hex_color += str(y) + ","
    #     else:
    #         hex_color += str(y)
    # ecolors.append("Rgb("+hex_color+")")
    ecolors.append(ccolor)
print(ecolors)


timmy.penup()
timmy.right(90)
timmy.forward(200)
timmy.right(90)
timmy.forward(200)
timmy.right(180)
for x in range(10):
    for x in range(10):
        timmy.pendown()
#         screen.colormode(255)
#         timmy.pencolor(random.choice(ecolors))
        timmy.dot(20, random.choice(ecolors))
        timmy.penup()
        timmy.forward(50)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.right(180)

screen.exitonclick()

print(timmy)
