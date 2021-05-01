height = int(input("Height:"))
height_min = 120
#<12 50
#12-18 90
#>18 110
if height <= height_min:
    print("Too short to enter ride!")

else:
    age = int(input("Age: "))
    print("Please take a seat after paying.")
    if (age < 12):
        print("As a child you pay N$50")
    elif (age <= 18):
        print("As an adult you pay N$90")
    else:
        print("As an adult you pay N$110")
