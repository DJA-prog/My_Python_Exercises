#don't change the code below
student_marks = input("Input a list of student marks: ").split()
for n in range(0, len(student_marks)):
    student_marks[n] = float(student_marks[n])
print(student_marks)
# don't change the code above

#Write your code below
total_mark = 0
num_student_marks = 0
for mark in student_marks:
    num_student_marks += 1
    total_mark += mark
average_mark = round(total_mark / num_student_marks)
print(f"The average mark for {num_student_marks} students are {average_mark}")
# 75 60 85 45 63 50 70
