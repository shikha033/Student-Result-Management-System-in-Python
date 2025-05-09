from tkinter import *

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Managment System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
             
        title = Label(self.root, text="Student Result Managment System", bg = "#033054", fg="white", font=("goudy old style ", 20, "bold"))
        title.place(x=0, y=0, relwidth=1, height=50)
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
