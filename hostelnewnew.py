from tkinter import *
from tkinter import ttk
import pymysql as a


class hostel:
    def hostaldata(self, root):
        self.root = root
        root.title("Online Helpdesk")
        root.geometry("1300x800+215+95")


        self.search_by = StringVar()
        self.search_txt = StringVar()

        title = Label(self.root, relief=GROOVE, bd=4, text="HOSTEL INFORMATION", font=("times new romen", 30, "bold"),
                      fg="white", bg="navyblue")
        title.pack(side=TOP, fill=X)

        data_frame = Frame(self.root, bd=5, relief=RIDGE, bg="lightblue")
        data_frame.place(x=17, y=80, width=1280, height=710)

        lbl_search = Label(data_frame, text="Search By :- ", bg="lightblue", fg="black",
                           font=("times new romen", 14, "bold"))
        lbl_search.place(x=350, y=20)

        combo_search = ttk.Combobox(data_frame, textvariable=self.search_by, font=("times new romen", 10, "bold"),
                                    state="readonly")
        combo_search["values"] = ("stdname", "roomno")
        combo_search.place(x=500, y=20 )

        txt_search = Entry(data_frame, textvariable=self.search_txt, font=("times new romen", 10, "bold"), bd=5,
                           relief=GROOVE)
        txt_search.place(x=700,y=20 )

        search = Button(data_frame, text="Search", width=10, command=self.show_data).place(x=480,y=100)
        Showall = Button(data_frame, text="Show All", width=10, command=self.show_all).place(x=600,y=100)

        # =====Table Frame=========
        table_frame = Frame(data_frame, bd=4, relief=RIDGE, bg="lightblue")
        table_frame.place(x=30, y=160, width=1200, height=530)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.hostel_table = ttk.Treeview(table_frame, columns=("build", "roomno", "stdname", "purcrse","yos"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=TOP, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hostel_table.xview)
        scroll_y.config(command=self.hostel_table.yview)
        self.hostel_table.heading("build", text="BLOCK")
        self.hostel_table.heading("roomno", text="ROOM NO.")
        self.hostel_table.heading("stdname", text="STUDENT NAME")
        self.hostel_table.heading("purcrse", text="PURSUING COURSE")
        self.hostel_table.heading("yos", text="YEAR OF STUDYING")
        self.hostel_table["show"] = "headings"
        self.hostel_table.column("build", width=220)
        self.hostel_table.column("roomno", width=220)
        self.hostel_table.column("stdname", width=220)
        self.hostel_table.column("purcrse", width=220)
        self.hostel_table.column("yos", width=220)
        self.hostel_table.pack()

    def show_data(self):
        con = a.connect(host="localhost", port=3306, user="root", db="online", password="1234")
        cmd = con.cursor()
        cmd.execute("SELECT * from hostel WHERE " + str(self.search_by.get()) + " Like '%" + str(self.search_txt.get()) + "%'")
        rows = cmd.fetchall()
        if len(rows) != 0:
            self.hostel_table.delete(*self.hostel_table.get_children())
            for row in rows:
                self.hostel_table.insert('', END, values=row)
            con.commit()
        con.close()

    def show_all(self):
        con = a.connect(host="localhost", port=3306, user="root", db="online", password="1234")
        cmd = con.cursor()
        cmd.execute("select * from hostel")
        rows = cmd.fetchall()
        if len(rows) != 0:
            self.hostel_table.delete(*self.hostel_table.get_children())
            for row in rows:
                self.hostel_table.insert('', END, values=row)
            con.commit()
        con.close()
#root = Tk()
#ob=hostel()
#ob.hostaldata(root)
#root.mainloop()