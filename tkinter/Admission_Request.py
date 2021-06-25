# "student number" "5* symbols" "pass or not"
#one at a time

from tkinter import *

root = Tk()
root.title("Admission Request")

students = []


def button_enter():
    student = {}
    student["number"] = e0.get()
    if eval(e1b.get()) < 3 or eval(e2b.get()) < 3 or eval(e1b.get()) + eval(e2b.get()) + eval(e3b.get()) + eval(e4b.get()) + eval(e5b.get()) < 12:
        student["pass_"] = "false"
    else:
        student["pass_"] = "true"
    student["math"] = e1b.get()
    student["physics"] = e2b.get()
    student[e3a.get()] = e3b.get()
    student[e4a.get()] = e4b.get()
    student[e5a.get()] = e5b.get()
    prints(student)
    students.append(student)
    e0.delete(0, END)
    e1b.delete(0, END)
    e2b.delete(0, END)
    e3a.delete(0, END)
    e3b.delete(0, END)
    e4a.delete(0, END)
    e4b.delete(0, END)
    e5a.delete(0, END)
    e5b.delete(0, END)


Label(root, text="Student Number:").grid(row=0,column=0)
e0 = Entry(root)
e0.grid(row=0,column=1)

Label(root, text="Subject").grid(row=1,column=0)
Label(root, text="Symbol").grid(row=1,column=1)
e1a = Label(root, text="Math")
e1a.grid(row=2,column=0)
e1b = Entry(root)
e1b.grid(row=2,column=1)
e2a = Label(root, text="Physics")
e2a.grid(row=3,column=0)
e2b = Entry(root)
e2b.grid(row=3,column=1)
e3a = Entry(root)
e3a.grid(row=4,column=0)
e3b = Entry(root)
e3b.grid(row=4,column=1)
e4a = Entry(root)
e4a.grid(row=5,column=0)
e4b = Entry(root)
e4b.grid(row=5,column=1)
e5a = Entry(root)
e5a.grid(row=6,column=0)
e5b = Entry(root)
e5b.grid(row=6,column=1)

Button(root, text="Enter", command=button_enter, bg="green").grid(row=7,column=1)

def prints(int):
    Label(root, text=int).grid(row=8,column=0)

root.mainloop()#event loop
