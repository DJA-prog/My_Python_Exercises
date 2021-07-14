#Student number:
#Date: 31/05/2021
#Description: Lab 2



#Ch9
#Q7,(a)
user_input =input("Enter a string: ")
letter = input("Letter to locate: ")
count =0
while  count <1:
    count+=1
    if letter in user_input:
        print(user_input.index(letter))
    else:
        print("Letter not found in word")
        
#(b)
user_input =input("Enter a string: ")
letter = input("Letter to locate: ")

for character in user_input:
    if character == letter:
        print(user_input.index(character))

        break
   
#Ch10,Q7
L=[int("1"*i) for i in range(1,111)]
print(L)


#Ch11,Q3

import operator

year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}

#a
user_input= input("Enter Name of a month: ")
for key, values in year.items():
     if user_input == key:  
        print( values)
      
#b
sorted_year ={key:year[key] for key in sorted(year)}
print(sorted_year.keys())

#c
for keys,values in year.items():
    if int(values) == 31:

      print(keys)

#d
sorted_bymonthdays = dict(sorted(year.items(),key= operator.itemgetter(1)))
print(sorted_bymonthdays)


#Ch13,Q6
def binomialCoeff(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1


    return binomialCoeff(n - 1, k - 1) + binomialCoeff(n - 1, k)

print(binomialCoeff(5,2))


