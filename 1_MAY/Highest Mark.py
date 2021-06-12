#don't change the code below
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = float(student_scores[n])
print(student_scores)
# don't change the code above

#Write your code below
highest_score = 0
for score in student_scores:
    if (score > highest_score):
        highest_score = score

print(f"The highest score is {round(highest_score)}")

# 75 60 85 45 63 50 70
