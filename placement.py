from tkinter import *
from tkinter import ttk


class placement:
    def place_a(self,root):
        self.root = root
        self.root.title("Online Helpdesk")
        self.root.geometry("1300x700+215+95")

        title = Label(self.root, relief=GROOVE, bd=4, text="PLACEMENT DETAILS", font=("times new romen", 30, "bold"),
                      fg="white", bg="CRIMSON")
        title.pack(side=TOP, fill=X)

        text_var=("\n   ITM Universe has always given training, augmentation and placements an utmost priority and to implement it into action an exclusive training, augmentation and placement assistance \n   cell (TAP) has been established with state–of-art facilities. The cell is headed by experienced professional from Industry.\n\n  The TAP Cell of ITM Universe has timely identified the gap & introduced a unique model of providing Augmentation & Training on required skill sets which can complement the formal \n  education. The programs are structured on the basis of feedback from leading industries academics & research institutions in different fields.\n\n\t\t\t\t\t\t\tTAP TEAM ITM GOI\n\t\t\t\t\t\t\tMr. Arpit Singh Chauhan\n\t\t\t\t\t\t\t(Sr. Placement officer)\n\t\t\t\t\t\t\tEmail id : arpit.chauhan@itmuniversity.ac.in\n\t\t\t\t\t\t\tPhone No : +91-9691973919\n\t\t\t\t\t\t\tMrs. Sangeeta Sharma\n\t\t\t\t\t\t\t(Placement officer)\n\t\t\t\t\t\t\tEmail id : sangeeta.sharma@itmuniversity.ac.in\n\t\t\t\t\t\t\tPhone No : +91-8962541634\n\t\t\t\t\t\t\tMr. Mudit Sachdeva\n\t\t\t\t\t\t\t(Placement officer)\n\t\t\t\t\t\t\tEmail id : muditsachdeva.tap@itmuniversity.ac.in\n\t\t\t\t\t\t\tPhone No : +91-7879738389\n\t\t\t\t\t\t\tMs. Shvetambri Sharma\n\t\t\t\t\t\t\t(Training Officer)\n\t\t\t\t\t\t\tEmail id : shvetambri.sharma.tap@itmuniversity.ac.in\n\t\t\t\t\t\t\tPhone No : +91 751 2440036\n\t\t\t\t\t\t\tMs. Ayushi Khan\n\t\t\t\t\t\t\t(Asst.Placement Officer)\n\t\t\t\t\t\t\tEmail id : ayushi.khan.tap@itmuniversity.ac.in\n\t\t\t\t\t\t\tPhone No : +91-8839445351\n\t\t\t\t\t\t\tMs. Trishla Upadhyay\n\t\t\t\t\t\t\t(Placement Coordinator)\n\t\t\t\t\t\t\tEmail id : trishla.upadhyay.tap@itmuniversity.ac.\n\t\t\t\t\t\t\tPhone No : +91 7974161749\n\t\t\t\t\t\t\tMr. Shubham Pandey\n\t\t\t\t\t\t\t(Office Executive)\n\t\t\t\t\t\t\tEmail id : shubham.pandey@itmgoi.in\n\t\t\t\t\t\t\tPhone No : +91 8982694030\n\n\n\n\n\t\t\t\t\t------MAJOR COMPANIES CONDUCTED CAMPUS RECRUITMENT DRIVE------\n\n\n\t\t\t•  Infosys	•  Cognizant	•  Wipro	•  IBM	•  iGate•  Persistent	•  Mphasis	•  Aon Hewitt	•  Capgemini	\n\t\t\t•  TCS   •  Accenture	•  Amdocs	•  Syntel	•  Zensar	•  IDPL   •  Tech Mahindra	•  Neon Infotech	•  L&T Infotech	 \n\t\t\t •  IGT	•  Birlasoft  •  CSC	•  Sapient	•  Hexaware	•  HCL Technologies	•  Daman Deep Alchohal\n\t\t\t •  HCL Infosystems	•  Impetus	•  HP	•  Amdale	•  Premier Biosoft•  American Mega Trends	•  Diaspark	•  Mu Sigma	\n\t\t\t •  Paragon Infotech	•  Robert BOSCH  •  ICICI Infotech	•  Honeywell Automation	•  L & T	•  Hettich	•  Punj Lloyd \n\t\t\t •  AIS Glass	•  J.K.Tyres	•  Moser Bear	•  Lona Bearings	•  Lohia Group Designco  •  Vermeer	\n\t\t\t•  Cimcon	•  Coca Cola	•  Ipca	•  BORL  •  Alchem	•  Cadbury	•  Godrej	•  SRF	•  Oswal Fertilizers\n\t\t\t•  Grasim Industries	•  Artech	•  Satyam	•  Cadilla	•  Diamond Cement  •  Sharad Constructions	•  ERA Group	\n\t\t\t•  Shobha Developers  •  Slipco Construction	•  Torry Harris  •  Airtel	•  Fedex	•  Jackson	•  Essel Power	\n\t\t\t •  HPCL Mittal Energy  •  Indian Army	•  Indian Navy	•  Metacube	•  Innoeye	•  Cavission  •  Eastern Software Systems	\n\t\t\t •  Globallogic(Formerly Induslogic)	•  Uflex(Formerly Flex Chemical)	•  Sofcon	•  Eureka Forbes\n\n\n")

        scroll=Scrollbar(self.root)

        scroll.pack(side=RIGHT, fill=Y)

        mylist= Text(self.root ,width=500 ,height=500 ,bg="lightyellow" ,fg="black" ,font=(40) ,yscrollcommand=scroll.set)
        mylist.insert(END,text_var)

        mylist.pack(side=LEFT ,fill=BOTH)
        scroll.config(command=mylist.yview)




#root = Tk()
#ob = placement()
#ob.place_a(root)
#root.mainloop()
