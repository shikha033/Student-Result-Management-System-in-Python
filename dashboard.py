from tkinter import *

from PIL import Image, ImageTk  

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Managment System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # icons---
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_ch.png")

        # title--  
        title = Label(self.root, text="Student Result Managment System",padx=10,compound=LEFT,image=self.logo_dash , bg = "#033054", fg="white", font=("goudy old style ", 20, "bold"))
        title.place(x=0, y=0, relwidth=1, height=50)


        # menu---
        m_frame=LabelFrame(self.root, text="Menu",font=("times new roman ",15) ,bg="white")
        m_frame.place(x=10, y=70, width=1250, height=80)
        # buttons---
        btn_course = Button(m_frame, text="COURSES",cursor="hand2", width=20, font=("goudy old style", 15,"bold"), bg="#0b5377", fg="white")
        btn_course.place(x=20, y=5,width=200,height=40)
        # can be hand1 and 3

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
