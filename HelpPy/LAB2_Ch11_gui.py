from tkinter import *

root = Tk()
root.title("Lab 2")
root.geometry('450x450+10+10')
root.config(bg='#84BF04')

days = {' January ': 31, ' February ': 28, ' March ': 31, ' April ': 30,
        ' May ': 31, ' June ': 30, ' July ': 31, ' August ': 31,
        ' September ': 30, ' October ': 31, ' November ': 30, ' December ': 31}
ch11_day = 0

Label(root, text="Month: ").grid(row=0, column=0)
ch11_e = Entry(root, width=25, fg="black", borderwidth=2)
ch11_e.grid(row=0, column=1, padx=10, pady=5)

ch11_days = Entry(root, width=10, bg="#A9CF54", fg="black")
ch11_days.insert(0, ch11_day)
ch11_days.grid(row=0, column=2)

tex = Listbox(root, height=13, width=40)
tex.grid(row=2, column=0, columnspan=3)


def textBox(message, n):
    tex.insert(n, message)


def button_enter():
    ch11_days.delete(0, END)
    ch11_days.insert(0, days[' ' + ch11_e.get() + ' '])


def button_facts():
    n = 0
    textBox("Alphabetical:", n)
    for key in sorted(days):
        key = "--" + key
        n += 1
        textBox(key, n)

    n += 1
    textBox("", n)
    n += 1
    textBox("Months of 31:", n)
    for month in days:
        if days[month] == 31:
            month = "--" + month
            n += 1
            textBox(month, n)

    s_days = sorted(days.items(), key=lambda x: x[1])
    s_days = dict(s_days)
    n += 1
    textBox("", n)
    n += 1
    textBox("Sorted by days:", n)
    for key, value in s_days.items():
        output = (key, ':', value)
        n += 1
        textBox(output, n)


button_enter = Button(root, text="Enter", width=8, pady=20, bg="green", command=button_enter)
button_facts = Button(root, text="Facts", width=8, pady=20, bg="yellow", command=button_facts)
button_exit = Button(root, text="Exit", width=8, pady=20, bg="red", command=root.destroy)
button_enter.grid(row=1, column=0)
button_facts.grid(row=1, column=1)
button_exit.grid(row=1, column=2)
Label(root, text="Scrollable").grid(row=3, column=1)
# for key in sorted(days):
#     print(key)
#
# for month in days:
#     if days[month] == 31:
#         print(month)
#
# s_days = sorted(days.items(), key=lambda x: x[1])
# s_days = dict(s_days)
# for key, value in s_days.items():
#     print(key, ':', value)

root.mainloop()
