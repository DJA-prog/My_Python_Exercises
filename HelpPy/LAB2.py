# Student number:
# Date: 01/06/2021
# Description: Lab 2


# Ch9,Q5
scores = []
count = 0
while True:
    testscore = eval(input("Enter Test Scores: "))
    scores.append(testscore)
    if testscore >= 90:
        count += 1

    if testscore == 0:
        print("Count A grade", count)
        print("Average", sum(scores) / len(scores))
    if testscore < 0:
        break

# Ch10,Q7
# 7. Write a program that creates the list [1,11,111,1111,...,111...1] , where the entries
# have an ever increasing number of ones, with the last entry having 100 ones.
L = [int("1" * i) for i in range(1, 111)]
print(L)

# Ch11,Q3

import operator

year = {"January": "31", "Febuary": "28", "March": "30", "April": "30", "May": "31", "June": "30"}

# a
user_input = input("Enter Name of a month: ")
for key, values in year.items():
    if user_input == key:
        print(values)

# b
sorted_year = {key: year[key] for key in sorted(year)}
print(sorted_year.keys())

# c
for keys, values in year.items():
    if int(values) == 31:
        print(keys)

# d
sorted_bymonthdays = dict(sorted(year.items(), key=operator.itemgetter(1)))
print(sorted_bymonthdays)


# Ch13,Q4
def digital_root(num):
    num = str(num)
    sum = 0
    for i in range(len(num)):
        sum = sum + int(num[i]) % 9

    if sum == 0:
        return 9
    else:
        return sum % 9


print(digital_root(45893))
