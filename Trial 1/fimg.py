# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

win = Tk()

def img(a,v):
    while v == 0:
        # Define the geometry of the window
        win.geometry("1366x768")

        frame = Frame(win, width=600, height=400)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        # Create an object of tkinter ImageTk
        img = ImageTk.PhotoImage(Image.open(a))

        # Create a Label Widget to display the text or Image
        label = Label(frame, image = img)
        label.pack()

        win.mainloop()
