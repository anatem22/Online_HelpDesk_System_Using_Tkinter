from tkinter import *
from tkinter import ttk


class placement:
    def acco_a(self,root):
        self.root = root
        self.root.title("Online Helpdesk")
        self.root.geometry("1300x700+215+95")

        title = Label(self.root, relief=GROOVE, bd=5, text="ACCOUNT SECTION DETAILS", font=("helvetica", 30, "bold"),
                      fg="white", bg="crimson")
        title.pack(side=TOP, fill=X)

        text_var=("\n\n\n\t\t\t\t\t\t----- ACCOUNT SECTION -----\n\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n\tADDRESS :-\t\tNEAR  RAMANUJAN  BLOCK , ITM  GROUP  OF  INSTITUTIONS , SITHOULI ,  GWALIOR  (M.P.)\n\n\n\n\tWORKING DAYS :-\t\tMONDAY to SATURDAY (SUNDAY CLOSED)\n\n\n\n\tOPENING HOURS :-  9:30 A.M. to 4:00 P.M.\n\n\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        scroll=Scrollbar(self.root)

        scroll.pack(side=RIGHT, fill=Y)

        mylist= Text(self.root ,width=500 ,height=500 ,bg="lightyellow" ,fg="blue" ,font=(80,15) ,yscrollcommand=scroll.set)
        mylist.insert(END,text_var)

        mylist.pack(side=LEFT ,fill=BOTH)
        scroll.config(command=mylist.yview)




#root = Tk()
#ob = placement()
#ob.acco_a(root)
#root.mainloop()
