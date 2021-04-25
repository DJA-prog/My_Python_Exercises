print("Welcome to the DSC Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name_chk = 0

name_str = name1+name2
name_str = name_str.lower()

name_chk += name_str.count("t")
name_chk += name_str.count("r")
name_chk += name_str.count("u")
name_chk += name_str.count("e")

print(name_chk)

score = name_chk

if score < 10: #1-9
    print("You go together like coke and mint.")
elif score > 90: #91-100
    print("You go together like coke and mint.")
elif score >= 40: #40-90
    print("You are alright together.")
elif score <= 50: #10-49
    print("You are alright together.")
else:
    print(f"The score: {score}")
