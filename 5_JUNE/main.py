def factorial(n):
    #base parameter
    if (n < 2):
        return n #end of loop

    #recursive parameter
    return n * factorial(n - 1) #recursive
