from tkinter import *
from tkinter import ttk , messagebox
import sqlite3 


from PIL import Image, ImageTk  

class StudentClass:
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
        self.var_roll= StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date= StringVar()
        self.var_state= StringVar()
        self.var_city= StringVar()
        self.var_pin= StringVar()


        #===============widgets==============
        #===========column1================
        lbl_roll=Label(self.root, text="Roll No.", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=60)
        lbl_name=Label(self.root, text="Name", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=100)
        lbl_email=Label(self.root, text="EMail", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=140)
        lbl_gender=Label(self.root, text="Gender", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=180)
        lbl_state=Label(self.root, text="State", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=220)
        

        lbl_address=Label(self.root, text="Address", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=260)
        



        # entries
        self.txt_roll=Entry(self.root, textvariable= self.var_roll, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.txt_roll.place(x=150, y=60, width=200)
        txt_name=Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=150, y=100, width=200)

        txt_email=Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, 'bold'),state='readonly',justify=CENTER).place(x=150, y=140, width=200)
        self.txt_gender=ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select","Male", "Female", "Other"),justify=CENTER,font=("goudy old style", 15, 'bold'))
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)
        txt_state=Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=150, y=220, width=150)
        
      #=================column2=================
        lbl_dob=Label(self.root, text="D.O.B.", font=("goudy old style", 15, 'bold'), bg='white').place(x=360, y=60)
        lbl_contact=Label(self.root, text="Contact", font=("goudy old style", 15, 'bold'), bg='white').place(x=360, y=100)
        lbl_admission=Label(self.root, text="Admisssion", font=("goudy old style", 15, 'bold'), bg='white').place(x=360, y=140)
        lbl_course=Label(self.root, text="Course", font=("goudy old style", 15, 'bold'), bg='white').place(x=360, y=180)

       # entries
        self.course_list=[]
        self.txt_dob=Entry(self.root, textvariable= self.var_dob, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.txt_dob.place(x=480, y=60, width=200)
        txt_contact=Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=480, y=100, width=200)

        txt_admisssion=Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15, 'bold'),state='readonly',justify=CENTER).place(x=480, y=140, width=200)
        self.txt_course=ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list,justify=CENTER,font=("goudy old style", 15, 'bold'))
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.set("Empty")
       #=================text address=================


        self.txt_address=Text(self.root, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.txt_address.place(x=150, y=260,width=540, height=100)

        # buttons==============
        self.btn_add=Button(self.root,text='Save', font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2" , command=self.add)
        self.btn_add.place(x=150, y=400, width=110,height=40)
        self.btn_update=Button(self.root,text='Update', font=("goudy old style", 15, "bold"), bg="#4caf50",fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y = 400, width=110,height=40)
        self.btn_delete=Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete)
        self.btn_delete.place( x = 390 ,y=400, width=110,height=40)
        self.btn_clear=Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="#607d8b",fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place( x = 510 , y = 400, width=110,height=40)

         #===Search Panel============
        self.var_search= StringVar()
        lbl_search_courseName=Label(self.root, text="Search By | Course Name", font=("goudy old style", 15, 'bold'), bg='white').place(x=720, y=60)
        txt_search_courseName=Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=950, y=60, width=180)
        btn_search=Button(self.root,text='Search', font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2",command=self.search)
        btn_search.place(x=1150, y=60, width=110,height= 30)


      #=====content========
        self.C_Frame=Frame(self.root, bd = 2, relief=RIDGE)
        self.C_Frame.place(x = 720 , y = 100 ,width=470, height=340) 
           
        scrolly=Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame, orient=HORIZONTAL)
        
        
        self.CourseTable=ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set )
        scrollx.pack(side=BOTTOM, fill=X) 
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="Course ID" )
        self.CourseTable.heading("name", text="Course Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")
        self.CourseTable["show"]="headings" # otherwise one extra empty column will be there
        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("description", width=100)
           
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()  
#==================================================
    def clear(self):
      self.show()
      self.var_roll.set("")
      self.var_name.set("")
      self.var_email.set("")
      self.var_gender.set("")
      self.var_search.set("")
      self.txt_address.delete("1.0", END)
      self.txt_roll.config(state=NORMAL)
    
    def delete(self): 
      con = sqlite3.connect(database="rms.db")
      cur = con.cursor()
      try:
        if self.var_course.get() == "":
            messagebox.showerror("Error", "Course Name must be required", parent=self.root)
            return
        else:
            cur.execute("SELECT * FROM course WHERE name=?", (self.var_course.get(),))
            row = cur.fetchone()
            
            if row is None:
                messagebox.showerror("Error", "Please select a valid course from the list", parent=self.root)
            else:
                op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                if op:
                    cur.execute("DELETE FROM course WHERE name=?", (self.var_course.get(),))
                    con.commit()
                    messagebox.showinfo("Delete", "Course deleted successfully", parent=self.root)
                    self.clear()

      except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
      finally:
        con.close()

    
      

  

#Adding event=None solves both:
#Works with .bind()
#Works if you call manually
    def get_data(self, event=None):
      self.txt_roll.config(state='readonly')
      r=self.CourseTable.focus()
      content=self.CourseTable.item(r)
      row=content['values'] 
      #print(row)


      

    def add(self):
      con=sqlite3.connect(database="rms.db")
      cur=con.cursor()
      try:
         if self.var_course.get()=="":
            messagebox.showerror("Error", "Course Name must be required", parent=self.root)
            return
         else:
          cur.execute("SELECT * FROM course WHERE name=?",(self.var_course.get(),)  )
          row=cur.fetchone()
          if row!=None:
            messagebox.showerror("Error", "Course already present, try different", parent=self.root)
          else:
            cur.execute("INSERT into course (name, duration, charges, description) values(?,?,?,?)",(
            self.var_course.get(),
            self.var_duration.get(),
            self.var_charges.get(),
            self.txt_description.get("1.0", END)
          ))
          con.commit()
          messagebox.showinfo("Success", "Course added successfully", parent=self.root) 
          self.show()    
      except Exception as ex:
        messagebox.showerror("Error", f"Error due to {str(ex)}")
      finally:
        con.close()
      
    def show(self):
      con=sqlite3.connect(database="rms.db")
      cur=con.cursor()
      try:
        
          cur.execute("SELECT * FROM course")
          rows=cur.fetchall()
          self.CourseTable.delete(*self.CourseTable.get_children())
          for row in rows:
            self.CourseTable.insert('',END, values=row)
         
               
      except Exception as ex:
        messagebox.showerror("Error", f"Error due to {str(ex)}")
      finally:
        con.close()



    def update(self):
      con=sqlite3.connect(database="rms.db")
      cur=con.cursor()
      try:
         if self.var_course.get()=="":
            messagebox.showerror("Error", "Course Name must be required", parent=self.root)
            return
         else:
          cur.execute("SELECT * FROM course WHERE name=?",(self.var_course.get(),)  )
          row=cur.fetchone()
          if row!=None:
            messagebox.showerror("Error", "Select Course From List", parent=self.root)
          else:
            cur.execute("UPDATE course  set  duration=? , charges=? , description=? where name=? ",(
    
            self.var_duration.get(),
            self.var_charges.get(),
            self.txt_description.get("1.0", END),
            self.var_course.get()
          ))
          con.commit()
          messagebox.showinfo("Success", "Course updated successfully", parent=self.root) 
          self.show()    
      except Exception as ex:
        messagebox.showerror("Error", f"Error due to {str(ex)}")
     
    def search(self):
      con=sqlite3.connect(database="rms.db")
      cur=con.cursor()
      try:
        
          cur.execute(f"SELECT * FROM course where name LIKE '%{self.var_search.get()}%'")
          rows=cur.fetchall()
          self.CourseTable.delete(*self.CourseTable.get_children())
          for row in rows:
            self.CourseTable.insert('',END, values=row)
         
               
      except Exception as ex:
        messagebox.showerror("Error", f"Error due to {str(ex)}")
      finally:
        con.close()


if __name__ == "__main__":

    root = Tk()
    obj = StudentClass(root)
    root.mainloop()