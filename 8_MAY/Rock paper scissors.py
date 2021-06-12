rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

hand_choice = {rock, paper, scissors}

import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

print(f"You choose: \n {hand_choice[user_choice]}")
print(f"Computer choose: \n {hand_choice[computer_choice]}")

if (user_choice > 2 or user_choice < 0):
    print("Input Error")

elif (user_choice == 0):
    if (computer_choice == 0):
        print("It's a Draw")
    if (computer_choice == 1):
        print("You lost ☹️")
    if (computer_choice == 2):
        print("You Won 😃")

elif (user_choice == 1):
    if (computer_choice == 0):
        print("You Won 😃")
    if (computer_choice == 1):
        print("It's a Draw")
    if (computer_choice == 2):
        print("You lost ☹️")

elif (user_choice == 2):
    if (computer_choice == 0):
        print("You lost ☹️")
    if (computer_choice == 1):
        print("You Won 😃")
    if (computer_choice == 2):
        print("It's a Draw")
