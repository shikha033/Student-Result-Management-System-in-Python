from tkinter import *
from PIL import Image, ImageTk  
from course import CourseClass
class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Managment System")
        self.root.geometry("1380x700+0+0")
        self.root.config(bg="white")

        # icons---
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_ch.png")

        # title--  
        title = Label(self.root, text="Student Result Managment System",padx=10,compound=LEFT,image=self.logo_dash , bg = "#033054", fg="white", font=("goudy old style", 20, "bold"))
        title.place(x=0, y=0, relwidth=1, height=50)


        # menu=================
        m_frame=LabelFrame(self.root, text="Menu",font=("times new roman",15) ,bg="white")
        m_frame.place(x=5, y=70, width=1260, height=80)
        # buttons---
        btn_course = Button(m_frame, text="COURSES",cursor="hand2", command=self.add_course,width=20, font=("goudy old style", 15,"bold"), bg="#0b5377", fg="white")
        btn_course.place(x=20, y=5,width=180,height=40)
        # can be hand1  and others
        btn_student= Button(m_frame, text="STUDENT",cursor="hand2", width=20, font=("goudy old style", 15,"bold"), bg="#0b5377", fg="white")
        btn_student.place(x=220, y=5,width=180,height=40)
        btn_result= Button(m_frame, text="RESULT",cursor="hand2", width=20, font=("goudy old style", 15,"bold"), bg="#0b5377", fg="white")
        btn_result.place(x=420, y=5,width=180,height=40)
        btn_view = Button(m_frame, text="VIEW RESULT",cursor="hand2", width=20, font=("goudy old style", 15,"bold"), bg="#0b5377", fg="white")
        btn_view.place(x=620, y=5,width=180,height=40)
        btn_logout = Button(m_frame, text="LOGOUT",cursor="hand2", width=20, font=("goudy old style", 15,"bold"), bg="#0b5377", fg="white")
        btn_logout.place(x=820, y=5,width=180,height=40)
        btn_exit = Button(m_frame, text="EXIT",cursor="hand2", width=20, font=("goudy old style", 15,"bold"), bg="#0b5377", fg="white")
        btn_exit.place(x=1020, y=5,width=180,height=40)


        #==============content=================
        self.bg_img =Image.open("images/bg2.jpg")
        self.bg_img = self.bg_img.resize((800, 300), Image.Resampling.LANCZOS)  #  resize image
        self.bg_bg = ImageTk.PhotoImage(self.bg_img)

        self_lbl_bg=Label(self.root, image=self.bg_bg)
        self_lbl_bg.place(x=400, y=180, width=800, height=300)


        #========update_details=======
        self.lbl_course=Label(self.root, text="Total Courses\n[0]", font=("goudy old style", 20), bg="#e43b06",fg="white", bd=10,relief=RIDGE)
        self.lbl_course.place(x=450, y=500, width=200, height=100)    
        
        self.lbl_student=Label(self.root, text="Total Students\n[0]", font=("goudy old style", 20), bg="#0676ad",fg="white", bd=10,relief=RIDGE)
        self.lbl_student.place(x=670, y=500, width=200, height=100)    

        self.lbl_result=Label(self.root, text="Total Results\n[0]", font=("goudy old style", 20), bg="#038074",fg="white", bd=10,relief=RIDGE)
        self.lbl_result.place(x=890, y=500, width=200, height=100)    






        #==============footer-================

        #footer=Label(self.root, text="SRMS-Student Result Management System\nContact Us for ant Technical Issue: srms.45@gmail.com, 987xxxxx01", font=("goudy old style", 12), bg="#262626", fg="white")
        #footer.pack(side=BOTTOM,fill=X)
        footer=Label(self.root, text="© 2025 Student Result Management System | Developed by Shikha", font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM,fill=X,  ipady=5) # ipady=10 adds padding inside the widget
         
        '''
        footer = Frame(root, bg="#222222", height=30)
        footer.pack(side="bottom", fill="x")

        # Footer Label
        footer_label = Label(footer,text="© 2025 Student Result Management System | Developed by Your Name",
                 fg="white",
             bg="#222222",
                 font=("Arial", 10))
        footer_label.pack(pady=5)'''

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj= CourseClass(self.new_win )

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
