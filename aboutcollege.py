from tkinter import *
from tkinter import ttk


class college:
    def about_a(self,root):
        self.root = root
        self.root.title("Online Helpdesk")
        self.root.geometry("1300x700+215+95")

        title = Label(self.root, relief=GROOVE, bd=4, text="CAMPUS DETAIL", font=("times new romen", 30, "bold"),
                      fg="white", bg="crimson")
        title.pack(side=TOP, fill=X)

        titler = Label(self.root, relief=GROOVE, bd=4, text="ITM GROUP OF INSTITUTIONS", font=("times new romen", 30, "bold"),
                      fg="crimson", bg="white")
        titler.pack(side=TOP, fill=X)

        text_var=("\n\n\tEstablished in 1997 by Samata Lok Sansthan Trust at Gwalior, ITM is an A-Grade institute having most number of courses in the state accredited by NBA. ITM is an approved \n  institution by AICTE, Govt. of India, and recognised by Govt. of M.P. and affiliated to Rajiv Gandhi Proudyogiki Vishwavidyalaya (University of Technology of M. P.), Bhopal. The Institute is   conceived with an objective to impart quality education in the field of engineering and technology so that it emerges out as a world-class institution by contributing towards research and     education and to produce high class engineers and technologists. The management of the institute is committed to rear this institution so that it becomes the apex centre for quality \n  teaching, development, innovation and extension services in engineering and technology.\n\n\tWith the evolution of interdisciplinary courses like quantum information theory, quantum computing and nano-technology, the Institute is striving to integrate engineering as a \n  concept with technology as a platform taking management as a back bone to convert knowledge to global wealth & prosperity. The Institute recognizes the importance and need of such \n  a scheme in the ideas and thoughts on various technological models. The teaching and learning methodologies follow a rigorous regime involving extended hours of work and challenging   assignments.\n\n\tCurriculum delivery is affected through group and self learning seminars, conferences, case studies, live projects with industry, guest lectures and panel discussions with senior    managers and professionals from the industry/Corporate sector /research organizations. The emphasis is on involving the students in learning and helping them to relate concepts and \n  themes to technical cum management requirements. The system of assessment is based on continuous evaluation through tests, surprise quizzes, home assignments, laboratory work, \n  industry projects, presentations etc. The sole objective is to provide value added technical education and to produce quality technologists and professionals who are capable to shape \n  the society for better and better advancement and to improve the quality of life of Mankind.\n\n\tToday, time compression has become one of the necessary conditions for successful functioning of an organization. Organizations need to recreate a lean, thin and agile entity \n  from the large scale behemoth that it is today. This institute’s rehabilitation process is knowledge driven in terms of strategy, technology or logic of competitive success. This is achieved     by developing amongst students a culture of inquiry and research through highly competitive academic environment, close student-faculty interaction and linkages with industry and other \n  teaching academic institutions. Monitoring of students by senior managers and professionals from technical world, summer internship projects are the significant measures to abreast \n  students with the latest development and requirements of professional, technological and corporate world.\n\n\tThe Institute provides an academic environment with accent on self-learning. Students are actively involved in academic and co-curricular activities. ITM is a recognised Centre     of Research in Engineering and Technology.")
        scroll=Scrollbar(self.root)

        scroll.pack(side=RIGHT, fill=Y)

        mylist= Text(self.root ,width=500 ,height=500 ,bg="lightyellow" ,fg="black" ,font=(40) ,yscrollcommand=scroll.set)
        mylist.insert(END,text_var)

        mylist.pack(side=LEFT ,fill=BOTH)
        scroll.config(command=mylist.yview)




#root = Tk()
#ob = college()
#root.mainloop()
