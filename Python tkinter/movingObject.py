from tkinter import *

#Okno s widgedotom, ki se ga premikat z miško. ALi s tipkovnico.


#
MOUSE = TRUE
FRAMESIZE = 50
#

#Funkcije


def mouseMove(e):
    '''Premik dragLabel na mesto klika miske.'''
    x = e.x #+ mainFrame.winfo_rootx()
    y = e.y #+ mainFrame.winfo_rooty()
    print(x,y)
    dragLabel.place(relx=x/180,rely=y/120)
    return

def keysMove():
    '''Premik glede na klik.'''
    return

def status():
    '''Spremeni status - spremenljivka MOUSE. Ali se premikamo z misko ali z tipkovnico.'''
    MOUSE = not MOUSE
    return 


#Izgled

root = Tk()
root.geometry("400x400")

mainFrame = Frame(root)
mainFrame.pack()

mouseButton = Button(mainFrame,text = "Miška",padx=5,pady=10)
mouseButton.grid(row=0,column=0,padx=10,pady=10)

keysButton = Button(mainFrame,text = "Tipkovnica",padx=5,pady=10)
keysButton.grid(row=0,column=1)

statusLabel = Label(mainFrame,text="Miška")
statusLabel.grid(row=2,column=0,columnspan=2)

gameFrame = Frame(mainFrame,pady=FRAMESIZE,padx=FRAMESIZE,highlightbackground="black",highlightthickness=1.)
gameFrame.grid(row=3,column=0,columnspan=2)

dragLabel = Label(gameFrame,text="Premakni me!",borderwidth=1,relief="solid")
dragLabel.pack()



#Akcije

gameFrame.bind('<Button-1>',mouseMove)



root.mainloop()
