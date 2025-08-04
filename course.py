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
     


        #===============widgets==============
        lbl_courseName=Label(self.root, text="Course Name", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=60)
        lbl_duration=Label(self.root, text="Duration", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=100)
        lbl_charges=Label(self.root, text="Charges", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=140)
        lbl_description=Label(self.root, text="Description", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=180)

        # entries
        self.txt_courseName=Entry(self.root, textvariable=self.var_courseName, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.txt_courseName.place(x=150, y=60, width=200)
        txt_duration=Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=150, y=100, width=200)

        txt_charges=Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=150, y=140, width=200)
        self.txt_description=Text(self.root, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.txt_description.place(x=150, y=180,width=400, height=150)

        # buttons==============
        self.btn_add=Button(self.root,text='Save', font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2")
        self.btn_add.place(x=150, y=400, width=110,height=40)
if __name__ == "__main__":

    root = Tk()
    obj = CourseClass(root)
    root.mainloop()