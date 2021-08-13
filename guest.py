from tkinter import *
from tkinter import ttk
import pymysql as py
class guest1:
    def recode1(self,root):
        self.root=root
        root.title("Guest Record")
        root.geometry("1300x800+215+95")
        title=Label(self.root,text="Guest Record",bd=4,fg="white",bg="navyblue",font=("times new romen",30,"bold"),relief=RIDGE)
        title.pack(side=TOP,fill=X)

        self.name_var=StringVar()
        self.phone_var=StringVar()
        self.disp_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        add_frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
        add_frame.place(x=5,y=65,width=400,height=700)

        disp_frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
        disp_frame.place(x=405,y=65,width=890,height=700)

        title1=Label(add_frame,text="ADD GUEST RECORD",bd=4,font=("times new romen",20,"bold"),bg="lightblue",fg="black")
        title1.grid(row=0,columnspan=2,pady=10,padx=35)

        lbl_name=Label(add_frame,text="Name",font=("times new romen",15,"bold"),bg="lightblue",fg="black")
        lbl_name.grid(row=1,column=0,pady=10,padx=5,sticky="w")

        ent_name=Entry(add_frame,textvariable=self.name_var,font=("times new romen",15,"bold"),bd=5,relief=GROOVE)
        ent_name.grid(row=1,column=1,pady=10,padx=5,sticky="w")


        lbl_phone=Label(add_frame,text="Phone No.",font=("times new romen",15,"bold"),bg="lightblue",fg="black")
        lbl_phone.grid(row=2,column=0,pady=10,padx=5,sticky="w")

        ent_phone=Entry(add_frame,textvariable=self.phone_var,font=("times new romen",15,"bold"),bd=5,relief=GROOVE)
        ent_phone.grid(row=2,column=1,pady=10,padx=5,sticky="w")


        lbl_designation=Label(add_frame,text="Designation",font=("times new romen",15,"bold"),bg="lightblue",fg="black")
        lbl_designation.grid(row=3,column=0,pady=10,padx=5,sticky="w")

        ent_designation=Entry(add_frame,textvariable=self.disp_var,font=("times new romen",15,"bold"),bd=5,relief=GROOVE)
        ent_designation.grid(row=3,column=1,pady=10,padx=5,sticky="w")

      #==============BUTTON FRAME===========================
        but_frame=Frame(add_frame,bd=4,relief=RIDGE , bg="lightblue")
        but_frame.place(x=2,y=300,width=380,height=50)

      #=============BUTTONS===============================

        submit=Button(but_frame,text="Submit",width=10,command=self.add_guest).grid(row=0,column=0,padx=55,pady=10)
        clear = Button(but_frame, text="Clear", width=10,command=self.clear1).grid(row=0, column=1, padx=25, pady=10)

      #=============DISPLAY FRAME===========================
        disp_frame = Frame(self.root, bd=4, relief=RIDGE, bg="lightblue")
        disp_frame.place(x=405, y=65, width=890, height=700)

        lbl_search=Label(disp_frame,text="Search By",bg="lightblue",fg="black",font=("times new romen",20,"bold"),relief=GROOVE)
        lbl_search.grid(row=0,column=1,padx=5,pady=10,sticky="W")

      #==============COMBOBOX====================================

        cmb_search=ttk.Combobox(disp_frame,textvariable=self.search_by,width=10,font=("times new romen",15,"bold"),state="readonly")
        cmb_search['values']=("name","phone")
        cmb_search.grid(row=0,column=2,padx=5,pady=10,sticky="w")

        ent_search=Entry(disp_frame,textvariable=self.search_txt,bd=4,relief=RIDGE,font=("times new romen",15,"bold"))
        ent_search.grid(row=0,column=3,padx=5,pady=10,sticky="w")

        but_search=Button(disp_frame,text="Search ",width=10,command=self.search_data).grid(row=0,column=4,pady=10,padx=40)
        but_show = Button(disp_frame, text="Show All ", width=10,command=self.show_guest).grid(row=0, column=5, pady=10, padx=10)

      #================TABLE FRAME===================================

        tabe_frame=Frame(disp_frame,bd=4,relief=RIDGE,bg="lightblue")
        tabe_frame.place(x=10,y=70,width=850,height=600)

      #===============SCROLL BAR===================================

        scroll_x=Scrollbar(tabe_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(tabe_frame,orient=VERTICAL)
        self.guest_table=ttk.Treeview(tabe_frame,column=("name","phone","disp"),xscrollcommand=scroll_x.set ,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=TOP,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.guest_table.xview)
        scroll_y.config(command=self.guest_table.yview)
        self.guest_table.heading("name",text="Name")
        self.guest_table.heading("phone",text="Phone")
        self.guest_table.heading("disp",text="Disignation")
        self.guest_table["show"]="headings"
        self.guest_table.column("name",width=200)
        self.guest_table.column("phone",width=200)
        self.guest_table.column("disp",width=400)
        self.guest_table.pack()

    def search_data(self):
        con=py.connect(host="localhost",user="root",port=3306,db="online",password="1234")
        cmd=con.cursor()
        cmd.execute("select * from guest where "+str(self.search_by.get())+" LIke '%"+str(self.search_txt.get())+"%'")
        rows=cmd.fetchall()
        if len(rows)!=0:
            self.guest_table.delete(* self.guest_table.get_children())
            for row in rows:
                self.guest_table.insert('',END,values=row)
            con.commit()
        con.close()

    def show_guest(self):
        con = py.connect(host="localhost", port=3306, password="1234", db="online", user="root")
        cmd = con.cursor()
        cmd.execute("select * from guest")
        rows = cmd.fetchall()
        if len(rows) != 0:
            self.guest_table.delete(*self.guest_table.get_children())
            for row in rows:
                self.guest_table.insert('', END, values=row)
            con.commit()
        con.close()

    def add_guest(self):
        con = py.connect(host="localhost", port=3306, password="1234", db="online", user="root")
        cmd = con.cursor()
        cmd.execute("insert into guest values(%s,%s,%s)",(self.name_var.get(),self.phone_var.get(),self.disp_var.get()))
        con.commit()
        self.show_guest()
        self.clear1()
        con.close()
    def clear1(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.disp_var.set("")


root=Tk()
#s=guest1()
#s.recode1(root)
#root.mainloop()