from tkinter import *
from tkinter import ttk
import pymysql as a
class facult:
    def record(self,root):
        self.root=root
        root.title("Faculties Records")
        root.geometry("1300x800+215+95")

        self.name_var=StringVar()
        self.dept_var=StringVar()
        self.block_var=StringVar()
        self.deskno_var=StringVar()
        self.subject_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        title=Label(self.root,relief=GROOVE,bd=4,text="Faculties Data",font=("times new romen",30,"bold"),fg="white",bg="navyblue")
        title.pack(side=TOP,fill=X)

        facult_frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
        facult_frame.place(x=1,y=65,width=1290,height=700)

        lbl_search = Label(facult_frame, text="Search By", bg="lightblue", fg="black",font=("times new romen", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(facult_frame,textvariable=self.search_by, font=("times new romen", 12, "bold"),
                                    state="readonly", width=10)
        combo_search["values"] = ("name", "dept", "subject")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Entry(facult_frame, textvariable=self.search_txt,font=("times new romen", 10, "bold"), bd=5,
                           relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search = Button(facult_frame, text="Serach", width=10,command=self.show_data ).grid(row=0, column=3, padx=10,
                                                                                             pady=15)
        Showall = Button(facult_frame, text="Show All", width=10,command=self.show_all).grid(row=0, column=4, padx=10, pady=15)

        # =====Table Frame=========
        table_frame = Frame(facult_frame, bd=4, relief=RIDGE, bg="lightblue")
        table_frame.place(x=10, y=70, width=1250, height=600)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.facult_table = ttk.Treeview(table_frame,
                                          columns=("name", "dept", "block", "deskno", "contact", "subject"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=TOP, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.facult_table.xview)
        scroll_y.config(command=self.facult_table.yview)
        self.facult_table.heading("name", text="Name")
        self.facult_table.heading("dept", text="Department")
        self.facult_table.heading("block", text="Block")
        self.facult_table.heading("deskno", text="Desk No")
        self.facult_table.heading("contact", text="Contact")
        self.facult_table.heading("subject", text="Subject")
        self.facult_table["show"] = "headings"
        self.facult_table.column("name", width=200)
        self.facult_table.column("dept", width=200)
        self.facult_table.column("block", width=200)
        self.facult_table.column("deskno", width=200)
        self.facult_table.column("contact", width=200)
        self.facult_table.column("subject", width=200)
        self.facult_table.pack()

    def show_data(self):
        con=a.connect(host="localhost",port=3306,user="root",db="online",password="1234")
        cmd=con.cursor()
        cmd.execute("select * from faculties where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cmd.fetchall()
        if len(rows)!=0:
            self.facult_table.delete(* self.facult_table.get_children())
            for row in rows:
                self.facult_table.insert('',END,values=row)
            con.commit()
        con.close()

    def show_all(self):
        con = a.connect(host="localhost", port=3306, user="root", db="online", password="1234")
        cmd = con.cursor()
        cmd.execute("select * from faculties")
        rows=cmd.fetchall()
        if len(rows)!=0:
            self.facult_table.delete(* self.facult_table.get_children())
            for row in rows:
                self.facult_table.insert('',END,values=row)
            con.commit()
        con.close()
#root=Tk()
#ob=facult()
#ob.record(root)
#root.mainloop()

