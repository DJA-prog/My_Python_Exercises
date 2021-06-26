from tkinter import *

root = Tk() # First lines(basic window)

#label Widget
mylabel1 = Label(root, text="Hello World!") #define / create widget
mylabel1.grid(row=0, column=0)

mylabel2 = Label(root, text="I am here for you!") #define / create widget
mylabel2.grid(row=1, column=0)
#012345
#1
#2
#3
#4
#5
#event loop
root.mainloop()
