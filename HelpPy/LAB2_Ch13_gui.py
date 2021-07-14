from tkinter import *

root = Tk()
root.title("Lab 2")
root.geometry('300x200+10+10')
root.config(bg='#84BF04')

Label(root, text="Number:").grid(row=0, column=0)
Label(root, text="D Root:").grid(row=1, column=0)

e0 = Entry(root)
e0.grid(row=0, column=1)

def button_enter():
    digital_root(eval(e0.get()))


e1 = Entry(root)
e1.grid(row=1, column=1)


def digital_root(num):
    num2 = 0
    num1 = str(num)
    print(num1)
    if num > 9:
        for i in num1:
            num2 = num2 + int(i)
        digital_root(num2)
    else:
        e1.delete(0, END)
        e1.insert(0, num)


button_enter = Button(root, text="Enter", width=8, pady=20, bg="green", command=button_enter)
button_exit = Button(root, text="Exit", width=8, pady=20, bg="red", command=root.destroy)
button_enter.grid(row=2, column=0)
button_exit.grid(row=2, column=1)

root.mainloop()
