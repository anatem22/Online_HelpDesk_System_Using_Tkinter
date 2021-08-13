from tkinter import *
from tkinter import ttk
import pymysql as ph
class student:
    def abhi(self,root):
        self.root=root
        self.root.title("Student Data")
        self.root.geometry("1300x800+215+95")


        title=Label(self.root,text="Student Record System",bd=10,relief=GROOVE,font=("times new romen ",30,"bold"),bg="navyblue",fg="white")
        title.pack(side=TOP,fill=X)

        #======== All variables===========

        self.roll_no=StringVar()
        self.name_var=StringVar()
        self.email_id=StringVar()
        self.gender_var=StringVar()
        self.contact_no=StringVar()
        self.dob_var=StringVar()
        self.searchby=StringVar()
        self.search_txt=StringVar()

        #=======Manage Fram===============
        '''

        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        manage_frame.place(x=20,y=80,width=450,height=800)
        '''
        #=========Detail Frame===================

        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="lightblue")
        detail_frame.place(x=1, y=80, width=1300, height=800)
        '''
        m_title=Label(manage_frame,text="manage student",font=("times new romen",30,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,columnspan=2,pady=10)

        lbl_roll = Label(manage_frame, text="Roll Number", bg="crimson", fg="white",font=("times new romen",15,"bold"))
        lbl_roll.grid(row=1, column=0, pady=10,padx=20,sticky="w")

        txt_roll = Entry(manage_frame,textvariable=self.roll_no, font=("times new romen", 15, "bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(manage_frame, text="Name", bg="crimson", fg="white",font=("times new romen", 15, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(manage_frame,textvariable=self.name_var, font=("times new romen", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(manage_frame, text="Gender", bg="crimson", fg="white", font=("times new romen", 15, "bold"))
        lbl_gender.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(manage_frame,textvariable=self.gender_var,font=("times new romen",12,"bold"),state="readonly")
        combo_gender["values"]=("male","female","other")
        combo_gender.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_email = Label(manage_frame, text="Email", bg="crimson", fg="white",font=("times new romen", 15, "bold"))
        lbl_email.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(manage_frame, textvariable=self.email_id,font=("times new romen", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_contactno = Label(manage_frame, text="Contact nu.", bg="crimson", fg="white",font=("times new romen", 15, "bold"))
        lbl_contactno.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contactno = Entry(manage_frame, textvariable=self.contact_no,font=("times new romen", 15, "bold"), bd=5, relief=GROOVE)
        txt_contactno.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(manage_frame, text="D.O.B", bg="crimson", fg="white",font=("times new romen", 15, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(manage_frame, textvariable=self.dob_var,font=("times new romen", 15, "bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(manage_frame, text="Address", bg="crimson", fg="white",font=("times new romen", 15, "bold"))
        lbl_address.grid(row=7, column=0, pady=20, padx=20, sticky="w")

        self.txt_address = Text(manage_frame, font=("times new romen", 15, "bold"), bd=5, relief=GROOVE,width=20,height=5)
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

       #==========Button===========

        but_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="crimson")
        but_frame.place(x=15, y=550, width=420)

        addbut=Button(but_frame,text="ADD",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=15)
        updatebut = Button(but_frame, text="Update", width=10).grid(row=0, column=1, padx=10, pady=15)
        deletebut = Button(but_frame, text="Delete", width=10).grid(row=0, column=2, padx=10, pady=15)
        clearbut = Button(but_frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=15)
        '''
        #============Detail Frame===============
        '''
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        detail_frame.place(x=500, y=100, width=800, height=800)
        '''
        lbl_search = Label(detail_frame, text="Search By", bg="lightblue", fg="black", font=("times new romen", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(detail_frame,textvariable=self.searchby, font=("times new romen", 12, "bold"), state="readonly",width=10)
        combo_search["values"] = ("roll", "name", "contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Entry(detail_frame,textvariable=self.search_txt, font=("times new romen", 10, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search = Button(detail_frame, text="Serach", width=10,command=self.get_search).grid(row=0, column=3, padx=10, pady=15)
        Showall = Button(detail_frame, text="Show All", width=10).grid(row=0, column=4, padx=10, pady=15)

        #=====Table Frame=========
        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="lightblue")
        table_frame.place(x=10, y=70, width=1250, height=600)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=TOP,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("address", text="Address")
        self.student_table["show"]="headings"
        self.student_table.column("roll", width=150)
        self.student_table.column("name", width=150)
        self.student_table.column("email", width=200)
        self.student_table.column("gender", width=150)
        self.student_table.column("contact", width=200)
        self.student_table.column("dob", width=150)
        self.student_table.column("address", width=230)
        self.student_table.pack()
        self.show_student()

    def add_student(self):
        con=ph.connect(host="localhost",port=3306,password="1234",db="online",user="root")
        cmd=con.cursor()
        cmd.execute("insert into rahul values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no.get(),self.name_var.get(),self.email_id.get(),self.gender_var.get(),self.contact_no.get(),self.dob_var.get(),self.txt_address.get('1.0',END) ))
        con.commit()
        self.show_student()
        self.clear()
        con.close()
    def show_student(self):
        con = ph.connect(host="localhost", port=3306, password="1234", db="online", user="root")
        cmd = con.cursor()
        cmd.execute("select * from rahul")
        rows=cmd.fetchall()
        if len(rows)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.roll_no.set("")
        self.name_var.set("")
        self.email_id.set("")
        self.gender_var.set("")
        self.contact_no.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    def get_search(self):
        con = ph.connect(host="localhost", port=3306, password="1234", db="online", user="root")
        cmd = con.cursor()
        cmd.execute("select * from rahul where  "+str(self.searchby.get())+" LIKE'%"+str(self.search_txt.get())+"%'")
        rows = cmd.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()

root=Tk()
#ob=student()
#ob.abhi(root)
#root.mainloop()