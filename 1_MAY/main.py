# imports
import module_1
import random

# module_1
print(f"PI = {module_1.pi}\n")

# random
random_int = random.randint(1, 20)
print(f"Random integer = {random_int}\n")

random_int = random.random()
print(f"Random float = {random_int}\n")

random_int = random.random()*5
print(f"Random float integer = {random_int}\n")

random.seed(321)
random_int = random.random()*5
print(f"Random seed = {random_int}\n")

