print("Welcome to leap Year Checker!")
year  = int(input("Which year do you want to verify: "))

if year%4 == 0:
    if year%100 ==0:
        if year%400 == 0:
            print(f"The year {year} is a leap year (it has 366 days).")
        else:
            print(f"The year {year} is not a leap year (it has 365 days).")
    else:
        print(f"The year {year} is a leap year (it has 366 days).")
else:
    print(f"The year {year} is not a leap year (it has 365 days).")
