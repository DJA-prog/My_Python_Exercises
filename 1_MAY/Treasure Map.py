#Don't change the code below

#🥲 getemoji.com for the emoji
row1 = ["🥸", "🥸", "🥸"]
row2 = ["🥸", "🥸", "🥸"]
row3 = ["🥸", "🥸", "🥸"]

treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ") # X Y
#Don't change the code above 🚫
#Write your code below

horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

selected_row = treasure_map[vertical]
selected_row[horizontal] = '❌'
#Write your code above

#Don't change the code below
print(f"{row1}\n{row2}\n{row3}")
