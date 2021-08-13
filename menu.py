import _datetime
from tkinter import *
import a as d
import faculties as e
import guest as g
import hodnewnewnew as h
import bus as b
import aboutcollege as a_b
import placement as pl
import hostelnewnew as hos
import admission as ad
import account as ac
def acco():
    root10=ac.Tk()
    acc=ac.placement()
    acc.acco_a(root10)
    root10.mainloop()
def addmi():
    root9=ad.Tk()
    add=ad.adm()
    add.addmision_a(root9)
    root9.mainloop()
def hostal_a():
    root8=hos.Tk()
    host=hos.hostel()
    host.hostaldata(root8)
    root8.mainloop()

def place():
    root7=pl.Tk()
    pla=pl.placement()
    pla.place_a(root7)
    root7.mainloop()
def abo():
    root5=a_b.Tk()
    ab=a_b.college()
    ab.about_a(root5)
    root5.mainloop()
def bu():
    root6=b.Tk()
    be=b.bus()
    be.record(root6)
    root6.mainloop()
def ho():
    root5=h.Tk()
    hu=h.hod()
    hu.hods(root5)
    root5.mainloop()
def gue():
    root4=g.Tk()
    gu=g.guest1()
    gu.recode1(root4)
    root4.mainloop()
def sb():
    root1=d.Tk()
    p=d.student()
    p.abhi(root1)
    root1.mainloop()
def fac():
    root3=e.Tk()
    r = e.facult()
    r.record(root3)
    root3.mainloop()


class display:

    def disp(self,root2):
        self.root2=root2
        self.root2.title("Main Menu")
        self.root2.geometry("2150x800+0+0")
        x = _datetime.datetime.now()
        Label(self.root2, text=x).place(x=180,y=5)

        l1=Label(root2,text="Welcome To ITM Online Helpdesk",fg="red",bg="moccasin",font=("times new romen",30,"bold"),bd=10,relief=GROOVE)


        l1.pack(side=TOP,fill=X)
        menu_frame=Frame(self.root2,bd=5,relief=RIDGE,bg="lavender")
        menu_frame.place(x=1,y=65,width=210,height=800)

        display_frame=Frame(self.root2,bd=5,relief=RIDGE,bg="pink")
        display_frame.place(x=210,y=65,width=1300,height=800)

        b10=Button(menu_frame,text="Guest Detail",font=("times new romen",10,"bold"),bd=5,width=23,command=gue)
        b10.grid(column=0,row=1,pady=3)

        b1=Button(menu_frame,text="Student Detail",font=("times new romen",10,"bold"),bd=5,width=23,command=sb)
        b1.grid(column=0,row=2,pady=3)
        b2=Button(menu_frame,font=("times new romen",10,"bold"),bd=5,text="Faculties",width=23,command=fac)
        b2.grid(column=0,row=3,pady=3)

        b3=Button(menu_frame,font=("times new romen",10,"bold"),bd=5,text="Bus Route",command=bu,width=23)
        b3.grid(column=0,row=4,pady=3)

        b4=Button(menu_frame,font=("times new romen",10,"bold"),bd=5,text="Admission Department",command=addmi,width=23)
        b4.grid(column=0,row=5,pady=3)
        b5=Button(menu_frame,font=("times new romen",10,"bold"),bd=5,text="Account Section",command=acco,width=23)
        b5.grid(column=0,row=6,pady=3)
        b6=Button(menu_frame,font=("times new romen",10,"bold"),bd=5,text="HOD'S",command=ho,width=23)
        b6.grid(column=0,row=7,pady=3)
        b8=Button(menu_frame,font=("times new romen",10,"bold"),bd=5,text="Placement Detail",command=place,width=23)
        b8.grid(column=0,row=9,pady=3)
        b9=Button(menu_frame,font=("times new romen",10,"bold"),bd=5,text="Campus Detail",command=abo,width=23)
        b9.grid(column=0,row=10,pady=3)
        b11 = Button(menu_frame, font=("times new romen", 10, "bold"), bd=5, text="Hostal Detail", command=hostal_a, width=23)
        b11.grid(column=0, row=11, pady=3)


root2=Tk()
o=display()
o.disp(root2)
root2.mainloop()


