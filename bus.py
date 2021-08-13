from tkinter import *
from tkinter import ttk
import pymysql as a


class bus:
    def record(self, root):
        self.root = root
        root.title("Bus Records")
        root.geometry("1300x800+215+95")

        self.name_var = StringVar()
        self.dept_var = StringVar()
        self.block_var = StringVar()
        self.deskno_var = StringVar()
        self.subject_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        title = Label(self.root, relief=GROOVE, bd=4, text="Bus Data", font=("times new romen", 30, "bold"),
                      fg="white", bg="navyblue")
        title.pack(side=TOP, fill=X)

        data_frame = Frame(self.root, bd=4, relief=RIDGE, bg="lightblue")
        data_frame.place(x=1, y=65, width=1290, height=700)

        lbl_search = Label(data_frame, text="Search By", bg="lightblue", fg="black",
                           font=("times new romen", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(data_frame, textvariable=self.search_by, font=("times new romen", 12, "bold"),
                                    state="readonly", width=10)
        combo_search["values"] = ("Busno", "Busroute")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Entry(data_frame, textvariable=self.search_txt, font=("times new romen", 10, "bold"), bd=5,
                           relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search = Button(data_frame, text="Search", width=10, command=self.show_data).grid(row=0, column=3, padx=10,
                                                                                            pady=15)
        Showall = Button(data_frame, text="Show All", width=10, command=self.show_all).grid(row=0, column=4, padx=10,
                                                                                              pady=15)

        # =====Table Frame=========
        table_frame = Frame(data_frame, bd=4, relief=RIDGE, bg="lightblue")
        table_frame.place(x=10, y=70, width=1250, height=600)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.bus_table = ttk.Treeview(table_frame, columns=("busno", "busroute", "drivername"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=TOP, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.bus_table.xview)
        scroll_y.config(command=self.bus_table.yview)
        self.bus_table.heading("busno", text="BUS NO")
        self.bus_table.heading("busroute", text="BUS ROUTE")
        self.bus_table.heading("drivername", text="Driver NAME")
        self.bus_table["show"] = "headings"
        self.bus_table.column("busno", width=200)
        self.bus_table.column("busroute", width=200)
        self.bus_table.column("drivername", width=200)
        self.bus_table.pack()

    def show_data(self):
        con = a.connect(host="localhost", port=3306, user="root", db="online", password="1234")
        cmd = con.cursor()
        cmd.execute("SELECT * from bus WHERE " + str(self.search_by.get()) + " like '%" + str(self.search_txt.get()) + "%'")
        rows = cmd.fetchall()
        if len(rows) != 0:
            self.bus_table.delete(*self.bus_table.get_children())
            for row in rows:
                self.bus_table.insert('', END, values=row)
            con.commit()
        con.close()

    def show_all(self):
        con = a.connect(host="localhost", port=3306, user="root", db="online", password="1234")
        cmd = con.cursor()
        cmd.execute("select * from bus")
        rows = cmd.fetchall()
        if len(rows) != 0:
            self.bus_table.delete(*self.bus_table.get_children())
            for row in rows:
                self.bus_table.insert('', END, values=row)
            con.commit()
        con.close()
#root = Tk()
#s=bus()
#s.record(root)
#root.mainloop()

