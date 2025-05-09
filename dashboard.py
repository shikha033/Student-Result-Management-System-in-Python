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
        title = Label(self.root, text="Student Result Managment System",compound=LEFT,image=self.logo_dash , bg = "#033054", fg="white", font=("goudy old style ", 20, "bold"))
        title.place(x=0, y=0, relwidth=1, height=50)
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
