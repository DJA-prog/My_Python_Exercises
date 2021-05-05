import random
import Rock_Paper_Scissors_img
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

print("You choose:")
Rock_Paper_Scissors_img.choice(user_choice)
print("Computer choose:")
Rock_Paper_Scissors_img.choice(computer_choice)

winner = ''
if (user_choice == 0):
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
