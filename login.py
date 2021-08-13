from tkinter import *
#def login():

#def register():

def mainscreen():
    global screen1
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text="Notes 1.0", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30").pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30").pack()
    screen.mainloop()
mainscreen()
