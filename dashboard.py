from tkinter import *

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Managment System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
             
        title-Label(self.root, text="STUDENT RESULT MANAGEMENT SYSTEM", bd=10, relief=GROOVE, font=("times new roman", 30, "bold)
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
