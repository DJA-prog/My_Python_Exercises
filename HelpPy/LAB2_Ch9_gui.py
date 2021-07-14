from tkinter import *

root = Tk()
root.title("Lab 2")
root.geometry('350x200+10+10')
root.config(bg='#84BF04')

ch9_count = 0
ch9_average = 0
ch9_scores = []


def ch9_new():
    global ch9_scores
    global ch9_average
    global ch9_count
    ch9_count = 0
    ch9_average = 0
    ch9_scores = []
    ch9_entry.delete(0, END)
    ch9_outlab()


def ch9_enter():
    global ch9_scores
    ch9_scores.append(int(ch9_entry.get()))
    global ch9_average
    ch9_average = sum(ch9_scores) / len(ch9_scores)
    if int(ch9_entry.get()) >= 90:
        global ch9_count
        ch9_count += 1
    ch9_entry.delete(0, END)
    ch9_outlab()


Label(root, text="Enter Test Scores:").grid(row=0, column=0)
ch9_entry = Entry(root)
ch9_entry.grid(row=0, column=1, columnspan=2)

Button(root, text="New", command=ch9_new, width=10, pady=10, bg="yellow").grid(row=1, column=0)
Button(root, text="Enter", command=ch9_enter, width=10, pady=10, bg="green").grid(row=1, column=1)
Button(root, text="Exit", command=root.destroy, width=10, pady=10, bg="red").grid(row=1, column=2)

Label(root, text="Count A grade: ").grid(row=2, column=0)
Label(root, text="Average: ").grid(row=3, column=0)

ch9_cnt = Entry(root, bg="#A9CF54")
ch9_cnt.insert(0, ch9_count)
ch9_cnt.grid(row=2, column=1, columnspan=2)
ch9_ave = Entry(root, bg="#BEEB9F")
ch9_ave.insert(0, ch9_average)
ch9_ave.grid(row=3, column=1, columnspan=2)


def ch9_outlab():
    global ch9_cnt
    global ch9_ave
    ch9_cnt.delete(0, END)
    ch9_cnt.insert(0, ch9_count)
    ch9_ave.delete(0, END)
    ch9_ave.insert(0, ch9_average)


root.mainloop()
