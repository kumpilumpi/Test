# Importing Tkinter module
from tkinter import *
# from tkinter.ttk import *

# Creating master Tkinter window
window = Tk()

'''
    pack <- natlači če se da
    geometry <- točno določena velikost
    grid(row = #, column = #) <- mreža 
'''

e = Entry(window)
e.pack()

def myClick():
    myLabel = Label(window, text = e.get())
    myLabel.pack()
    return

myButton = Button(window, text = "Klikni me!", command = myClick)
myButton.pack()

mainloop()
