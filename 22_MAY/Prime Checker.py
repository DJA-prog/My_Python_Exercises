#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for x in range(2, number - 1):
        if (number%x == 0):
            is_prime = False
    if(is_prime == True):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is NOT a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
