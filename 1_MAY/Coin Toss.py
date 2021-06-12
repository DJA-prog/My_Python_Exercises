# Remember to use the random module
import random

#Don't change the code below
coin_seed = int(input("Create a see number: "))
random.seed(coin_seed)
#Don't change the code above

#You code goes below
if (random.randint(0, 1) == 0):
    print("Tails")
else:
    print("Heads")
