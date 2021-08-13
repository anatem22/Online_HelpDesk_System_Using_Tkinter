from tkinter import *
import tkinter.messagebox as messagebox
import pymysql as a
import _datetime


class login:
    def user(self,root):
        self.root=root
        root.title("online helpdesk")
        root.geometry("650x250")


        self.username=StringVar()
        self.password=StringVar()

        Label(self.root, text="ONLINE HELPDESK", bg="white", font=("arial", 40, 'bold')).pack()
        Label(self.root, text="USERANAME", fg='black', font=('arial', 10, 'bold')).place(x=150, y=100)
        us = Entry(self.root, textvariable=self.username).place(x=280, y=100)
        Label(root, text="PASSWORD", fg='black', font=('arial', 10, 'bold')).place(x=150, y=140)
        pa = Entry(root, textvariable=self.password).place(x=280, y=140)
        login = Button(root, text="LOGIN", font=('arial', 10, 'bold'), fg='black', command=self.data).place(x=280, y=200)
        signup = Button(root, text="SIGNUP", font=('arial', 10, 'bold'), fg='black').place(x=360, y=200)

    def data(self):
        con = a.connect(host='localhost', port=3306, password='1234', user='root', db='online')
        cmd = con.cursor()
        if cmd.execute("select * from supply where first='{}' or last='{}'".format(self.username.get(),self.password.get())):

         messagebox.showinfo("show status","login")
         import menu as m

         root4 = m.Tk()
         me = m.display()
         me.disp(root4)
         root4.mainloop()
         con.commit()
         con.close()

        else:
              messagebox.showinfo("show status","data not matched")
def exitt():
    x = _datetime.datetime.now()
    print(x)
    exit()
root=Tk()
s=login()
s.user(root)
root.mainloop()
