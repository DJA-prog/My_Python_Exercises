height = int(input("Height:"))
height_min = 120
#child 50 <=18
#adult 180 >18
if height <= height_min:
    print("Too short to enter ride!")
        
else:
    age = int(input("Age: "))
    print("Please take a seat after paying.")
    if age <= 18:
        print("As a child you pay N$50")
    else:
        print("As an adult you pay N$180")
