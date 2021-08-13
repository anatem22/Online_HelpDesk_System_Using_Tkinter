from tkinter import *
from tkinter import ttk
import pymysql as po
class hod:
    def hods(self,root):
        self.root=root
        self.root.title("Online Helpdesk")
        self.root.geometry("1300x800+215+95")

        title=Label(self.root,text="HOD INFORMATION",bd=10,relief=GROOVE,font=("helvetica",35,"bold"),bg="navyblue",fg="white")
        title.pack(side=TOP,fill=X)

        self.id_no = StringVar()
        self.name_var = StringVar()
        self.department_var = StringVar()
        self.gender_var = StringVar()
        self.contact_no = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        '''
        manage_frame = Frame(self.root, bd=10, relief=RIDGE, bg="navyblue")
        manage_frame.place(x=20, y=180, width=450, height=610)
        '''

        detail_frame = Frame(self.root, bd=20, relief=RIDGE, bg="navyblue")
        detail_frame.place(x=5, y=100, width=800, height=700)

        '''
        manage_frame2 = Frame(self.root,bd=5,relief=RIDGE,bg="grey")
        manage_frame2.place(x=20,y=100,width=450,height=80)
    
        n_title = Label(manage_frame2, text="        MANAGE DATA", font=("helvetica",30, "bold"),bg="grey",
                       fg="black")
        n_title.grid(row=0, columnspan=2, pady=10)

        m_title = Label(manage_frame, text="ENTER DETAILS", font=("helvetica", 20, "bold"), bg="blue",
                        fg="black")
        m_title.grid(row=0, columnspan=2, pady=10)

        lbl_id = Label(manage_frame, text="ID Number ", bg="grey",fg="black",
                         font=("helvetica", 15, "bold"))
        lbl_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")


        txt_id = Entry(manage_frame, textvariable=self.id_no, font=("helvetica",15, "bold"), bd=5,
                         relief=GROOVE)
        txt_id.grid(row=1, column=1, pady=10, padx=20, sticky="w")


        lbl_name = Label(manage_frame, text="Name         ", bg="grey",fg="black",font=("helvetica", 15, "bold"))
        lbl_name.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(manage_frame, textvariable=self.name_var, font=("helvetica", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_name.grid(row=3, column=1, pady=10, padx=20, sticky="w")



        lbl_gender = Label(manage_frame, text="Gender      ", bg="grey",fg="black",font=("helvetica", 15, "bold"))
        lbl_gender.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(manage_frame, textvariable=self.gender_var, font=("helvetica", 14, "bold"),
                                    state="readonly")
        combo_gender["values"] = ("male", "female", "other")
        combo_gender.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_depart = Label(manage_frame, text="Department", bg="grey",fg="black",font=("helvetica", 15, "bold"))
        lbl_depart.grid(row=7, column=0, pady=10, padx=20, sticky="w")


        txt_depart = Entry(manage_frame, textvariable=self.department_var, font=("helvetica", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_depart.grid(row=7, column=1, pady=10, padx=20, sticky="w")



        lbl_contactno = Label(manage_frame, text="Contact no.", bg="grey",fg="black",font=("helvetica", 15, "bold"))
        lbl_contactno.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        txt_contactno = Entry(manage_frame, textvariable=self.contact_no, font=("helvetica", 15, "bold"), bd=5,
                              relief=GROOVE)
        txt_contactno.grid(row=9, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(manage_frame, text="D.O.B        ", bg="grey",fg="black",font=("helvetica", 15, "bold"))
        lbl_dob.grid(row=11, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(manage_frame, textvariable=self.dob_var, font=("helvetica", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_dob.grid(row=11, column=1, pady=10, padx=20, sticky="w")


        but_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="grey")
        but_frame.place(x=15, y=500, width=410)

        addbut = Button(but_frame, text="ADD", width=10).grid(row=0, column=0, padx=10, pady=15)
        updatebut = Button(but_frame, text="Update", width=10).grid(row=0, column=1, padx=10, pady=15)
        deletebut = Button(but_frame, text="Delete", width=10).grid(row=0, column=2, padx=10, pady=15)
        resetbut = Button(but_frame, text="Reset", width=10).grid(row=0, column=3, padx=10, pady=15)
        '''
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="lightblue")
        detail_frame.place(x=5, y=100, width=1500, height=800)

        lbl_search = Label(detail_frame, text="Search By", bg="lightblue",fg="black",
                           font=("helvetica", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(detail_frame, textvariable=self.search_by, font=("helvetica", 12, "bold"),
                                    state="readonly", width=10)
        combo_search["values"] = ("id_no", "name", "department")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")


        txt_search = Entry(detail_frame, textvariable=self.search_txt, font=("helvetica", 10, "bold"), bd=5,
                           relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search = Button(detail_frame, text="Search", width=10,command=self.show_data).grid(row=0, column=3, padx=10,
                                                                                             pady=15)
        Showall = Button(detail_frame, text="Show All", width=10,command=self.show_all).grid(row=0, column=4, padx=10, pady=15)

        Reset = Button(detail_frame, text="Reset", width=10).grid(row=0, column=5, padx=10, pady=15)

        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="lightblue")
        table_frame.place(x=20, y=80, width=1450, height=600)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.hod_table = ttk.Treeview(table_frame,columns=("id_no", "name", "department", "gender", "contact", "dob"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hod_table.xview)
        scroll_y.config(command=self.hod_table.yview)

        self.hod_table.heading("id_no", text="ID")
        self.hod_table.heading("name", text="NAME")
        self.hod_table.heading("department", text="DEPARTMENT")
        self.hod_table.heading("gender", text="GENDER")
        self.hod_table.heading("contact", text="CONTACT")
        self.hod_table.heading("dob", text="D.O.B")
        self.hod_table["show"] = "headings"

        self.hod_table.column("id_no", width=200)
        self.hod_table.column("name", width=300)
        self.hod_table.column("department", width=300)
        self.hod_table.column("gender", width=200)
        self.hod_table.column("contact", width=200)
        self.hod_table.column("dob", width=200)
        self.hod_table.pack()
        self.show_all()

    def show_data(self):
        con=po.connect(host="localhost",user="root",port=3306,password="1234",db="online")
        cmd=con.cursor()
        cmd.execute("select * from hod where "+ str(self.search_by.get()) + " Like '%"+str(self.search_txt.get())+"%'")
        rows = cmd.fetchall()
        if len(rows) != 0:
            self.hod_table.delete(*self.hod_table.get_children())
            for row in rows:
                self.hod_table.insert('', END, values=row)
            con.commit()
        con.close()
    def show_all(self):
        con = po.connect(host="localhost", port=3306, password="1234", db="online", user="root")
        cmd = con.cursor()
        cmd.execute("select * from hod")
        rows=cmd.fetchall()
        if len(rows)!=0:
            self.hod_table.delete(* self.hod_table.get_children())
            for row in rows:
                self.hod_table.insert('',END,values=row)
            con.commit()
        con.close()



root = Tk()
ob = hod()
#ob.hods(root)
#root.mainloop()














