from tkinter import *
from tkinter import ttk
import pymysql as ph
class adm:
    def addmision_a(self,root):
        self.root=root
        self.root.title("Online Helpdesk")
        self.root.geometry("1300x800+215+95")

        title = Label(self.root, text="ADMISSION INFORMATION", bd=10, relief=GROOVE, font=("arial ", 30, "bold"),
                      bg="navyblue", fg="white")
        title.pack(side=TOP, fill=X)

        self.search = StringVar()
        self.grad_var = StringVar()
        self.course_var = StringVar()
        self.detail_var = StringVar()
        global detail_frame

        detail_frame = Frame(self.root, bd=5, relief=GROOVE, bg="lightblue")
        detail_frame.place(x=17, y=80, width=1270, height=710)

        lbl_name = Label(detail_frame, text="SELECT :-", bg="lightblue", fg="black", font=("helvetica", 14, "bold"))
        lbl_name.place(x=300, y=20)

        combo_grad = ttk.Combobox(detail_frame, textvariable=self.grad_var, font=("helvetica", 10, "bold"),
                                    state="readonly")
        combo_grad["values"] = ("UG", "PG")
        combo_grad.place(x=420, y=20)
        Button(detail_frame,text="ok",command=self.disp).place(x=600,y=20)


        search = Button(detail_frame, text="Search", width=10,command=self.show).place(x=350,y=160)

        Showall = Button(detail_frame, text="Show All", width=10,command=self.show_all).place(x=450,y=160)

        Reset = Button(detail_frame, text="Reset", width=10).place(x=550,y=160)

        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="lightblue")
        table_frame.place(x=30, y=220, width=1200, height=470)
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.adm_table = ttk.Treeview(table_frame, columns=("coursename", "duration", "elig","fees"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.adm_table.xview)
        scroll_y.config(command=self.adm_table.yview)
        self.adm_table.heading("coursename", text="COURSE NAME")
        self.adm_table.heading("duration", text="DURATION")
        self.adm_table.heading("elig", text="ELIGIBILITY CRITERIA")
        self.adm_table.heading("fees", text="FEES")

        self.adm_table["show"] = "headings"
        self.adm_table.column("coursename", width=300)
        self.adm_table.column("duration", width=300 )
        self.adm_table.column("elig", width=300 )
        self.adm_table.column("fees", width=300)

        self.adm_table.pack()

    def disp(self):
        lbl_name1 = Label(detail_frame, text="ENTER COURSE NAME :-", bg="lightblue", fg="black",
                          font=("helvetica", 14, "bold"))
        lbl_name1.place(x=168, y=90)

        #Label(detail_frame, text=self.grad_var, bg="purple", fg="orange", font=("helvetica", 14, "bold"))
        #lbl_name1.place(x=200, y=90)

        txt_detail = ttk.Combobox(detail_frame, textvariable=self.detail_var, font=("helvetica", 11, "bold"),
                                  state="readonly")
        if self.grad_var.get() == "UG":
            txt_detail["values"] = ("btech", "diploma")
        else:
            txt_detail["values"] = ("mtech", "mba")
        txt_detail.place(x=420, y=90)
    def show(self):
        con=ph.connect(host="localhost", port=3306, user="root", db="online", password="1234")
        cmd = con.cursor()
        cmd.execute("SELECT * from admission where coursename='"+ self.detail_var.get() +"'")
        rows = cmd.fetchall()
        if len(rows) != 0:
            self.adm_table.delete(*self.adm_table.get_children())
            for row in rows:
                self.adm_table.insert('', END, values=row)
            con.commit()
        con.close()

    def show_all(self):
        con = ph.connect(host="localhost", port=3306, user="root", db="online", password="1234")
        cmd = con.cursor()
        cmd.execute("select * from admission")
        rows = cmd.fetchall()
        if len(rows) != 0:
            self.adm_table.delete(*self.adm_table.get_children())
            for row in rows:
                self.adm_table.insert('', END, values=row)
            con.commit()
        con.close()

#root = Tk()
#ob = adm()
#ob.addmision_a(root)
#root.mainloop()
