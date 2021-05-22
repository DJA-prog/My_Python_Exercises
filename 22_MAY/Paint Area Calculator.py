#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
    cans = (width * height) / cover
    print(f"You'll need {math.ceil(cans)} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
h = int(input("Height of wall: "))
w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=h, width=w, cover=coverage)
