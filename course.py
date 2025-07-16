from tkinter import *

from PIL import Image, ImageTk  

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Managment System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force() 

         # title--  
        title = Label(self.root, text="Manage Course Details", bg = "#033054", fg="white", font=("goudy old style", 20, "bold"))
        title.place(x=10, y=15, width=1250, height=35)

         #===variables=======
        self.var_courseName = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
     


if __name__ == "__main__":

    root = Tk()
    obj = CourseClass(root)
    root.mainloop()