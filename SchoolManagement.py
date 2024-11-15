#*********************************************************************************#
"""
Name: Henry Akinjayeju
Course Name: Software Developer
Course Code: 2574/3486
Instructor: Mr Oliver Kahrmann
"""
#**********************************************************************************#

import tkinter as tk    #import the tk inter libary from the GUI component
from tkinter import RIDGE, TOP, Button, Entry, Frame, Label, StringVar, Tk #importing specific tk inter widget
from tkinter import ttk # import for the tk inter Treeview
from tkinter import messagebox,filedialog # import for message Dialogs and file dialog
import mysql.connector # import for the project to interact with mySQL database
from fpdf import FPDF # importing FPDF for generating pdf report

# To protect the system for unwanted guest, a Login page is first created by creating a class

class Login:
    def __init__(self, root): # A constructor method was created to initialized the class
        self.root = root # Assigning the root to the main window
        self.root.title("Login Page") # Titile of the page was set
        self.root.geometry("500x300")# The dimension of the window was set

        self.username = StringVar() # The Stringvar was created to hold the username input
        self.password = StringVar() # The Stringvar was created to hold the password input

        lbltitle = Label(self.root, text="Login", font=("Arial", 20, "bold")) # The label title was created for the Login page
        lbltitle.pack(side=TOP, pady=20)# Positioned at it appropriate place

         
        lblusername = Label(self.root, text="Username", font=("Arial", 12)) # Label for username was created 
        lblusername.place(x=100, y=100)# Positioned at appropriate place
        txtusername = Entry(self.root, textvariable=self.username, font=("Arial", 12)) # Input field for the username was created
        txtusername.place(x=200, y=100) # Positioned at appropriate place

        # The same process as the username is repeated for the password. Creating and positioning the password label and input field

        lblpassword = Label(self.root, text="Password", font=("Arial", 12))
        lblpassword.place(x=100, y=150)
        txtpassword = Entry(self.root, textvariable=self.password, font=("Arial", 12), show='*')
        txtpassword.place(x=200, y=150)

        #A login Button is created for the login which will be clicked after the username and password has been entered
        btnlogin = Button(self.root, text="Login", command=self.login_function, font=("Arial", 12), width=10, bg="green", fg="white")
        btnlogin.place(x=200, y=200)

    def login_function(self): # A function was created to handle the login
        username = self.username.get()#Retrieve entered username 
        password = self.password.get()#Retrieve entered password


        if username == "admin" and password == "admin123":  #Then compare the entered username and password with the stored username if the match
            messagebox.showinfo("Login Success", "Welcome to School Management System")#If yes a success message is displayed
            self.root.destroy()#Then the login page is closed
            self.open_student_page()# And the main page of the student management system is opened
        else:#If the entered login credentials is not correct, a login error message is displayed
            messagebox.showerror("Login Error", "Invalid Username or Password")

    def open_student_page(self):#Function to open the student page
        root = Tk()#A new window is created for the student page
        SchoolManagementSystem(root)
        root.mainloop()#Run the new window in the main loop


#A class definition is made for the school management system
class SchoolManagementSystem:
    def __init__(self, root):
        #The root is initialize and the dimension and title are set
        self.root = root
        self.root.geometry('1540x800+0+0')
        self.root.title('School Management System')

        self.create_option_frame()# sidebar option frame was created to hold the navigation buttons
         #The database variables was initialize and set to none
        self.db = None  
        self.cursor = None  

        # Main content frame was created displaying welcome message

        self.main_frame = tk.Frame(self.root)
        self.main_frame = tk.Label(text="Welcome to the School Management System", fg="green",font=("arial",40,"bold"))
        self.main_frame.place(x=150, y=0, width=1375, height=780)   

         #Variables for teachers details was created which intended to store data related to a teacher’s personal and professional information.
         #This is created as a StringVar() object, which is a special variable class provided by Tkinter in Python.
        self.NameOfTeacher = StringVar()
        self.TeacherId = StringVar()
        self.DateOfBirth = StringVar()
        self.AssignedClass = StringVar()
        self.Gender = StringVar()
        self.YearEmployed = StringVar()
        self.TeacherAddress = StringVar()
        self.TeacherEmail = StringVar()
        self.TeacherPhone = StringVar()
        self.EducationalLevel = StringVar()
        self.SalaryAmount = StringVar()

        #The same process above is repeated for the student

        self.NameOfStudent = StringVar()
        self.StudentId = StringVar()
        self.DateOfBirth = StringVar()
        self.StudentClass = StringVar()
        self.Gender = StringVar()
        self.ParentName = StringVar()
        self.ParentAddress = StringVar()
        self.ParentEmail = StringVar()
        self.ParentPhone = StringVar()
        self.ParentOccupation = StringVar()

    def create_option_frame(self):   # Method to create the sidebar option frame with buttons

        # Sidebar options frame is created

        self.option_frame = tk.Frame(self.root, bg='#BE253D')
        self.option_frame.place(x=0, y=0, width=150, height=800)

        # Enrollment button and indicator label

        self.Enroll_sign = tk.Label(self.option_frame, text='', bg='#852030')
        self.Enroll_sign.place(x=3, y=50, width=5, height=40)
        Enroll_btn = tk.Button(self.option_frame, text='Enrollment', font=('Bold', 15), fg='#000000', bg='#FFFFFF', width=10,
                               command=lambda: self.indicator(self.Enroll_sign, self.enrollment_page))
        Enroll_btn.place(x=10, y=50)

        self.Acc_sign = tk.Label(self.option_frame, text='', bg='#852030')
        self.Acc_sign.place(x=3, y=100, width=5, height=40)
        Account_btn = tk.Button(self.option_frame, text='Account', font=('Bold', 15), fg='#000000', bg='#FFFFFF', width=10,
                                command=lambda: self.indicator(self.Acc_sign, self.account_page))
        Account_btn.place(x=10, y=100)
       
    
        self.Teach_sign = tk.Label(self.option_frame, text='', bg='#852030')
        self.Teach_sign.place(x=3, y=150, width=5, height=40)
        Teacher_btn = tk.Button(self.option_frame, text='Teacher', font=('Bold', 15), fg='#000000', bg='#FFFFFF', width=10,
                                command=lambda: self.indicator(self.Teach_sign, self.teacher_page))
        Teacher_btn.place(x=10, y=150)

    def hide_indicator(self):
        self.Enroll_sign.config(bg='#BE253D')
        self.Acc_sign.config(bg='#BE253D')
        self.Teach_sign.config(bg='#BE253D')

    def delete_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

    def indicator(self, lb, page):
        self.hide_indicator()
        self.delete_page()
        page()
        lb.config(bg='#000000')
#----------------------------------------------------------EnrollmentPage---------------------------------------------------------#


        


    def enrollment_page(self):
        enroll_frame = tk.Frame(self.main_frame)
        enroll_frame.place(x=0, y=0, width=1375, height=780)
        lb = tk.Label(enroll_frame, text='Student Enrollment', fg='#208529', font=('Bold', 30))
        lb.place(x=500, y=20)
                                                
       

        self.create_form_fields(enroll_frame)

        self.create_enrollment_table(enroll_frame)



    def create_form_fields(self, main_frame):
        self.stud_name = tk.Label(main_frame, text="Student Name:",fg="black",font=("Arial",12))
        self.stud_name.place(x=50, y=100)
        self.studEntry = tk.Entry(main_frame, textvariable=self.NameOfStudent,font=("Arial",12))
        self.studEntry.place(x=250, y=100, width=300)

        self.studId=tk.Label(main_frame, text="Student ID:",font=("Arial",12))
        self.studId.place(x=50,y=150)
        self.studIdEntry=tk.Entry(main_frame, textvariable=self.StudentId,font=("Arial",12))
        self.studIdEntry.place(x=250, y=150, width=300)

        self.dateOfBirth=tk.Label(main_frame, text="Date of Birth:",font=("Arial",12))
        self.dateOfBirth.place(x=50, y=200)
        self.dateEntry=tk.Entry(main_frame, textvariable=self.DateOfBirth,font=("Arial",12))
        self.dateEntry.place(x=250, y=200, width=300)

        self.studClass=tk.Label(main_frame, text="Class:",font=("Arial",12))
        self.studClass.place(x=50, y=250)
        self.studClassEntry=tk.Entry(main_frame, textvariable=self.StudentClass,font=("Arial",12))
        self.studClassEntry.place(x=250, y=250, width=300)

        self.gender=tk.Label(main_frame, text="Gender:",font=("Arial",12))
        self.gender.place(x=50, y=300)
        self.genderEntry=tk.Entry(main_frame, textvariable=self.Gender,font=("Arial",12))
        self.genderEntry.place(x=250, y=300, width=300)

        self.parentName=tk.Label(main_frame, text="Parent's Name:",font=("Arial",12))
        self.parentName.place(x=50, y=350)
        self.parentNameEntry=tk.Entry(main_frame, textvariable=self.ParentName,font=("Arial",12))
        self.parentNameEntry.place(x=250, y=350, width=300)

        self.parentAdd=tk.Label(main_frame, text="Parent's Address:",font=("Arial",12))
        self.parentAdd.place(x=50, y=400)
        self.parentAddEntry=tk.Entry(main_frame, textvariable=self.ParentAddress,font=("Arial",12))
        self.parentAddEntry.place(x=250, y=400, width=300)

        self.parentEmail=tk.Label(main_frame, text="Parent's Email:",font=("Arial",12))
        self.parentEmail.place(x=50, y=450)      
        self.parentEmailEntry=tk.Entry(main_frame, textvariable=self.ParentEmail,font=("Arial",12))
        self.parentEmailEntry.place(x=250, y=450, width=300)

        self.parentPhone=tk.Label(main_frame, text="Parent's Phone:",font=("Arial",12))
        self.parentPhone.place(x=50, y=500)
        self.parentPhoneEntry=tk.Entry(main_frame, textvariable=self.ParentPhone,font=("Arial",12))
        self.parentPhoneEntry.place(x=250, y=500, width=300)

        self.parentOccu=tk.Label(main_frame, text="Parent's Occupation:",font=("Arial",12))
        self.parentOccu.place(x=50, y=550)
        self.parentOccuEntry=tk.Entry(main_frame, textvariable=self.ParentOccupation,font=("Arial",12))
        self.parentOccuEntry.place(x=250, y=550, width=300)

        ButtonFrame = tk.Frame(main_frame, bd=20)
        ButtonFrame.place(x=10, y=710, width=1400, height=70)

        BtnAdd = tk.Button(ButtonFrame, text="Add New", bg="green", fg="white",
                                 font=("arial", 12, "bold"), width=15, command=self.BtnAdd)
        BtnAdd.place(x=5, y=0)

        BtnData = tk.Button(ButtonFrame, text="Fetch Data", bg="green", fg="white",
                         font=("arial", 12, "bold"), width=15, command=self.fetch_data)
        BtnData.place(x=200, y=0)

        BtnUpdate = tk.Button(ButtonFrame,text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=15,command=self.update)
        BtnUpdate.place(x=450, y=0)

        BtnDelete = tk.Button(ButtonFrame, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=15,command=self.delete)
        BtnDelete.place(x=700, y=0)

        BtnClear = tk.Button(ButtonFrame, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=15,command=self.clear)
        BtnClear.place(x=950, y=0)

        BtnExit = tk.Button(ButtonFrame, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=15,command=self.iExit)
        BtnExit.place(x=1180, y=0)

        

        

    def create_enrollment_table(self, frame):
        
        enroll_frame = tk.Frame(frame)
        enroll_frame.place(x=600, y=100, width=750, height=600)


        scroll_x = ttk.Scrollbar(enroll_frame, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(enroll_frame, orient=tk.VERTICAL)

        self.enrollment_table = ttk.Treeview(enroll_frame, columns=("NameOfStudent", "StudentId", "DateOfBirth",
                                                                    "StudentClass", "Gender", "ParentName", 
                                                                    "ParentAddress", "ParentEmail", 
                                                                    "ParentPhone", "ParentOccupation"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_x.config(command=self.enrollment_table.xview)
        scroll_y.config(command=self.enrollment_table.yview)

        
        self.enrollment_table.heading("NameOfStudent", text="Name of Student")
        self.enrollment_table.heading("StudentId", text="Student ID")
        self.enrollment_table.heading("DateOfBirth", text="Date Of Birth")
        self.enrollment_table.heading("StudentClass", text="Class")
        self.enrollment_table.heading("Gender", text="Gender")
        self.enrollment_table.heading("ParentName", text="Parent Name")
        self.enrollment_table.heading("ParentAddress", text="Parent Address")
        self.enrollment_table.heading("ParentEmail", text="Parent Email")
        self.enrollment_table.heading("ParentPhone", text="Parent Phone")
        self.enrollment_table.heading("ParentOccupation", text="Parent Occupation")

        
        self.enrollment_table["show"] = "headings"

        
        self.enrollment_table.column("NameOfStudent", width=100)
        self.enrollment_table.column("StudentId", width=100)
        self.enrollment_table.column("DateOfBirth", width=100)
        self.enrollment_table.column("StudentClass", width=100)
        self.enrollment_table.column("Gender", width=100)
        self.enrollment_table.column("ParentName", width=100)
        self.enrollment_table.column("ParentAddress", width=100)
        self.enrollment_table.column("ParentEmail", width=100)
        self.enrollment_table.column("ParentPhone", width=100)
        self.enrollment_table.column("ParentOccupation", width=100)

        self.enrollment_table.pack(fill=tk.BOTH, expand=1)
        self.enrollment_table.bind("<ButtonRelease-1>", self.get_cursor_enroll)

        self.db = mysql.connector.connect(host='localhost', user='root', password='Oluwaseyi,2019', database='schoolmanagementsystem')
        self.cursor = self.db.cursor()

    def BtnAdd(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='Oluwaseyi,2019', database='schoolmanagementsystem')
        self.cursor = self.db.cursor()
        
        sql = "INSERT INTO studentinfo (NameOfStudent, StudentId, DateOfBirth, StudentClass, Gender, ParentName, ParentAddress, ParentEmail, ParentPhone, ParentOccupation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.NameOfStudent.get(), self.StudentId.get(), self.DateOfBirth.get(), self.StudentClass.get(), self.Gender.get(), self.ParentName.get(), self.ParentAddress.get(), self.ParentEmail.get(), self.ParentPhone.get(), self.ParentOccupation.get())
        self.cursor.execute(sql, val)
        self.db.commit()
        self.db.close()
        messagebox.showinfo("Success", "Student Added Successfully")
        self.fetch_data()  
        
    def fetch_data(self):
       try:
            
            if not hasattr(self, 'enrollment_table'):
                messagebox.showerror("Error", "Enrollment table not defined.")
                return
            self.db = mysql.connector.connect(
                host="localhost", 
                user="root",  
                password="Oluwaseyi,2019", 
                database="schoolmanagementsystem"
            )
            self.cursor = self.db.cursor()
        
            self.cursor.execute("SELECT * FROM studentinfo")
            rows = self.cursor.fetchall()

            if len(rows) != 0:
                self.enrollment_table.delete(*self.enrollment_table.get_children())
                for row in rows:
                    self.enrollment_table.insert("", tk.END, values=row)

       except mysql.connector.Error as e: 
                messagebox.showerror("Error", f"An error occurred while fetching data: {str(e)}")

       finally:
               
                if self.cursor:
                    self.cursor.close()
                if self.db.is_connected():  
                    self.db.close()



    

    def update(self):
        if self.StudentId.get() == "":
            messagebox.showerror("Error", "Please select a record to update")
        else:
            self.db = mysql.connector.connect(host="localhost", username="root", password="Oluwaseyi,2019", database="schoolmanagementsystem")
            self.cursor = self.db.cursor()
            self.cursor.execute("UPDATE studentinfo SET NameOfStudent=%s, DateOfBirth=%s, StudentClass=%s, Gender=%s, ParentName=%s, ParentAddress=%s, ParentEmail=%s, ParentPhone=%s, ParentOccupation=%s WHERE StudentId=%s", (
                self.NameOfStudent.get(),
                self.DateOfBirth.get(),
                self.StudentClass.get(),
                self.Gender.get(),
                self.ParentName.get(),
                self.ParentAddress.get(),
                self.ParentEmail.get(),
                self.ParentPhone.get(),
                self.ParentOccupation.get(),
                self.StudentId.get()
            ))
            self.db.commit()
            self.fetch_data()
            self.db.close()
            messagebox.showinfo("Success", "Record has been updated")

   


    def get_cursor_enroll(self, event=""):
        cursor_row=self.enrollment_table.focus()
        content=self.enrollment_table.item(cursor_row)
        row=content['values']

        if row:
            self.NameOfStudent.set(row[0])
            self.StudentId.set(row[1])
            self.DateOfBirth.set(row[2])
            self.StudentClass.set(row[3])
            self.Gender.set(row[4])
            self.ParentName.set(row[5])
            self.ParentAddress.set(row[6])
            self.ParentEmail.set(row[7])
            self.ParentPhone.set(row[8])
            self.ParentOccupation.set(row[9])

    def delete(self):
       if self.StudentId.get() == "":
        messagebox.showerror("Error", "Please select a student to delete")
       else:
           conn = mysql.connector.connect(host="localhost", username="root", password="Oluwaseyi,2019", database="schoolmanagementsystem")
           cursor = conn.cursor()
           query = "DELETE FROM studentinfo WHERE StudentId=%s"
           value = (self.StudentId.get(),)
           cursor.execute(query, value)
           conn.commit()
           conn.close()
           self.fetch_data()
           self.clear()
           messagebox.showinfo("Success", "Student record has been deleted")


    def clear(self):
        self.NameOfStudent.set("")
        self.StudentId.set("")
        self.DateOfBirth.set("")
        self.StudentClass.set("")
        self.Gender.set("")
        self.ParentName.set("")
        self.ParentAddress.set("")
        self.ParentEmail.set("")
        self.ParentPhone.set("")
        self.ParentOccupation.set("")

    def iExit(self):
       iExit = messagebox.askyesno("School Management System", "Confirm you want to exit")
       if iExit:
          if hasattr(self, 'db') and self.db.is_connected():
             self.db.close()
             self.root.destroy()


        
#==============================================Account Page======================================================
    def account_page(self):
            account_frame = tk.Frame(self.main_frame)
            account_frame.place(x=0, y=0, width=1375, height=780)
            lb = tk.Label(account_frame, text='Fees and Payment Records', fg='#208529', font=('Bold', 30))
            lb.place(x=500, y=20)

            self.StudentName = StringVar()
            self.StudentId = StringVar()
            self.FirstTermFee = StringVar()
            self.SecondTermFee = StringVar()
            self.ThirdTermFee = StringVar()
            self.TotalFeePaid = StringVar()
            self.OutstandingBalance = StringVar()
            self.PaymentDate = StringVar()
            self.AcademicYear = StringVar()

            self.form_fields_account(account_frame)
            self.create_payment_table(account_frame)


    def form_fields_account(self, main_frame):
        student_name = tk.Label(main_frame, text="Student Name:", font=("Arial", 12))
        student_name.place(x=50, y=100)  
        StudentEntry = tk.Entry(main_frame, textvariable=self.StudentName, font=("Arial", 12))
        StudentEntry.place(x=270, y=100, width=300)


        StudentId=tk.Label(main_frame, text="Student ID:",font=("Arial",12))
        StudentId.place(x=50,y=150)
        StudentIdEntry=tk.Entry(main_frame, textvariable=self.StudentId,font=("Arial",12))
        StudentIdEntry.place(x=270, y=150, width=300)

        FirstTerm=tk.Label(main_frame, text="First Term Fees:",font=("Arial",12,))
        FirstTerm.place(x=50, y=200)
        FirstEntry=tk.Entry(main_frame, textvariable=self.FirstTermFee,font=("Arial",12))
        FirstEntry.place(x=270, y=200, width=300)

        SecondTerm=tk.Label(main_frame, text="Second Term Fees:",font=("Arial",12))
        SecondTerm.place(x=50, y=250)
        SecondTermEntry=tk.Entry(main_frame, textvariable=self.SecondTermFee,font=("Arial",12))
        SecondTermEntry.place(x=270, y=250, width=300)

        ThirdTerm=tk.Label(main_frame, text="Third Term Fees:",font=("Arial",12))
        ThirdTerm.place(x=50, y=300)
        ThirdEntry=tk.Entry(main_frame, textvariable=self.ThirdTermFee,font=("Arial",12))
        ThirdEntry.place(x=270, y=300, width=300)

        TotalFee=tk.Label(main_frame, text="Total Fees Paid:",font=("Arial",12))
        TotalFee.place(x=50, y=350)
        TotalFeeEntry=tk.Entry(main_frame, textvariable=self.TotalFeePaid,font=("Arial",12))
        TotalFeeEntry.place(x=270, y=350, width=300)

        Balance=tk.Label(main_frame, text="Outstanding Balance:",font=("Arial",12))
        Balance.place(x=50, y=400)
        BalanceEntry=tk.Entry(main_frame, textvariable=self.OutstandingBalance,font=("Arial",12))
        BalanceEntry.place(x=270, y=400, width=300)

        PayDate=tk.Label(main_frame, text="Payment Date (YYYY/MM/DD):",font=("Arial",12))
        PayDate.place(x=50, y=450)      
        PayDateEntry=tk.Entry(main_frame, textvariable=self.PaymentDate,font=("Arial",12,))
        PayDateEntry.place(x=270, y=450, width=300)

        AcaYear=tk.Label(main_frame, text="Academic Year(YYYY/MM/DD):",font=("Arial",12))
        AcaYear.place(x=50, y=500)
        AcaYearEntry=tk.Entry(main_frame, textvariable=self.AcademicYear,font=("Arial",12))
        AcaYearEntry.place(x=270, y=500, width=300)

        ButtonFrame = Frame(main_frame, bd=20)
        ButtonFrame.place(x=10, y=710, width=1400, height=70)

        BtnAdd = tk.Button(ButtonFrame, text="Add New", bg="green", fg="white",
                                 font=("arial", 12, "bold"), width=15, command=self.BtnAddPayment)
        BtnAdd.place(x=5, y=0)

        BtnData = tk.Button(ButtonFrame, text="Fetch Data", bg="green", fg="white",
                         font=("arial", 12, "bold"), width=15, command=self.fetch_data_payment)
        BtnData.place(x=200, y=0)

        BtnUpdate = tk.Button(ButtonFrame,text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=15,command=self.update_payment)
        BtnUpdate.place(x=400, y=0)

        BtnDelete = tk.Button(ButtonFrame, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=15,command=self.delete_payment)
        BtnDelete.place(x=600, y=0)

        BtnClear = tk.Button(ButtonFrame, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=15,command=self.clear_payment)
        BtnClear.place(x=800, y=0)

        BtnDownloadPDF = tk.Button(ButtonFrame, text="Download PDF", bg="green", fg="white", font=("arial", 12, "bold"), width=15, command=self.download_pdf_payment)
        BtnDownloadPDF.place(x=1000, y=0)


        BtnExit = tk.Button(ButtonFrame, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=15,command=self.iExit_payment)
        BtnExit.place(x=1200, y=0)

        self.db = mysql.connector.connect(host='localhost', user='root', password='Oluwaseyi,2019', database='schoolmanagementsystem')
        self.cursor = self.db.cursor()
        self.connection_timeout=300  

        
                
    def BtnAddPayment(self):
        try:
            if not self.cursor:
                messagebox.showerror("Error", "No database connection.")
                return

            sql_check = "SELECT * FROM fees WHERE StudentId=%s"
            val_check = (self.StudentId.get(),)
            self.cursor.execute(sql_check, val_check)
            result = self.cursor.fetchone()

            if result:
                messagebox.showerror("Error", "Student ID already exists. Please choose a new ID.")
            else:
                sql = """INSERT INTO fees (StudentName, StudentId, FirstTermFees, SecondTermFees, ThirdTermFees, 
                                        TotalFeesPaid, OutstandingBalance, PaymentDate, AcademicYear) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                val = (self.StudentName.get(), self.StudentId.get(), self.FirstTermFee.get(),
                    self.SecondTermFee.get(), self.ThirdTermFee.get(), self.TotalFeePaid.get(),
                    self.OutstandingBalance.get(), self.PaymentDate.get(), self.AcademicYear.get())
                self.cursor.execute(sql, val)
                self.db.commit()
                messagebox.showinfo("Success", "Payment Added Successfully")
                self.fetch_data_payment()

        except mysql.connector.Error as e:
            
            if self.db:
                self.db.rollback()
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        finally:
            
            if self.cursor:
                self.cursor.close()
            if self.db:
                self.db.close()



    def create_payment_table(self, frame):
        account_frame = tk.Frame(frame)
        account_frame.place(x=600, y=100, width=750, height=600)

        scroll_x = ttk.Scrollbar(account_frame, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(account_frame, orient=tk.VERTICAL)

        self.payment_table = ttk.Treeview(account_frame, columns=("StudentName", "StudentId", "FirstTermFees",
                                                                    "SecondTermFees", "ThirdTermFees", "TotalFeesPaid", 
                                                                    "OutstandingBalance", "PaymentDate", 
                                                                    "AcademicYear"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_x.config(command=self.payment_table.xview)
        scroll_y.config(command=self.payment_table.yview)

        
        self.payment_table.heading("StudentName", text="Student Name")
        self.payment_table.heading("StudentId", text="Student ID")
        self.payment_table.heading("FirstTermFees", text="First Term Fees")
        self.payment_table.heading("SecondTermFees", text="Second Term Fees")
        self.payment_table.heading("ThirdTermFees", text="Third Term Fees")
        self.payment_table.heading("TotalFeesPaid", text="Total Fees Paid")
        self.payment_table.heading("OutstandingBalance", text="Outstanding Balance")
        self.payment_table.heading("PaymentDate", text="Payment Date")
        self.payment_table.heading("AcademicYear", text="Academic Year")
        


        
        self.payment_table["show"] = "headings"

        
        self.payment_table.column("StudentName", width=100)
        self.payment_table.column("StudentId", width=100)
        self.payment_table.column("FirstTermFees", width=110)
        self.payment_table.column("SecondTermFees", width=110)
        self.payment_table.column("ThirdTermFees", width=110)
        self.payment_table.column("TotalFeesPaid", width=110)
        self.payment_table.column("OutstandingBalance", width=150)
        self.payment_table.column("PaymentDate", width=100)
        self.payment_table.column("AcademicYear", width=100)
        


        self.payment_table.pack(fill=tk.BOTH, expand=1)
        self.payment_table.bind("<ButtonRelease-1>", self.get_cursor_payment)


    def update_payment(self):
        if self.StudentId.get() == "":
            messagebox.showerror("Error", "Please select a record to update")
        else:
            try:
                self.db = mysql.connector.connect(host="localhost", username="root", password="Oluwaseyi,2019", database="schoolmanagementsystem")
                self.cursor = self.db.cursor()
                sql = """UPDATE fees 
                        SET StudentName=%s, FirstTermFees=%s, SecondTermFees=%s, ThirdTermFees=%s, TotalFeesPaid=%s, OutstandingBalance=%s, PaymentDate=%s, AcademicYear=%s
                        WHERE StudentId=%s"""
                val = (
                    self.StudentName.get(),
                    self.FirstTermFee.get(),
                    self.SecondTermFee.get(),
                    self.ThirdTermFee.get(),
                    self.TotalFeePaid.get(),
                    self.OutstandingBalance.get(),
                    self.PaymentDate.get(),
                    self.AcademicYear.get(),
                    self.StudentId.get(),
                )
                self.cursor.execute(sql, val)
                self.db.commit()
                self.fetch_data_payment()
                messagebox.showinfo("Success", "Record has been updated")
            except mysql.connector.Error as e:
                if self.db:
                    self.db.rollback()
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                if self.cursor:
                    self.cursor.close()
                if self.db.is_connected():
                    self.db.close()


    def fetch_data_payment(self):
        try:
            self.db = mysql.connector.connect(host="localhost", username="root", password="Oluwaseyi,2019", database="schoolmanagementsystem")
            self.cursor = self.db.cursor()
            self.cursor.execute("SELECT * FROM fees")
            rows = self.cursor.fetchall()

            if len(rows) != 0:
                self.payment_table.delete(*self.payment_table.get_children())
                for row in rows:
                    self.payment_table.insert("", tk.END, values=row)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"An error occurred while fetching data: {str(e)}")
        finally:
            if self.cursor:
                self.cursor.close()
            if self.db.is_connected():
                self.db.close()


    def get_cursor_payment(self, event=""):
        cursor_row=self.payment_table.focus()
        content=self.payment_table.item(cursor_row)
        row=content['values']
        self.StudentName.set(row[0])
        self.StudentId.set(row[1])
        self.FirstTermFee.set(row[2])
        self.SecondTermFee.set(row[3])
        self.ThirdTermFee.set(row[4])
        self.TotalFeePaid.set(row[5])
        self.OutstandingBalance.set(row[6])
        self.PaymentDate.set(row[7])
        self.AcademicYear.set(row[8])

    def delete_payment(self):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this payment?"):
            try:
                self.db = mysql.connector.connect(host="localhost", username="root", password="Oluwaseyi,2019", database="schoolmanagementsystem")
                self.cursor = self.db.cursor()
                sql = "DELETE FROM fees WHERE StudentId=%s"
                val = (self.StudentId.get(),)
                self.cursor.execute(sql, val)
                self.db.commit()
                self.fetch_data_payment()
                self.clear_payment()
                messagebox.showinfo("Success", "Record has been deleted")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                if self.cursor:
                    self.cursor.close()
                if self.db.is_connected():
                    self.db.close()


    def clear_payment(self):
        self.StudentName.set("")
        self.StudentId.set("")
        self.FirstTermFee.set("")
        self.SecondTermFee.set("")
        self.ThirdTermFee.set("")
        self.TotalFeePaid.set("")
        self.OutstandingBalance.set("")
        self.PaymentDate.set("")
        self.AcademicYear.set("")

    def download_pdf_payment(self):
        
        pdf = FPDF()
        pdf.add_page()

       
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="School Fee Payment Record", ln=True, align='C')

        
        pdf.set_font("Arial", '', 12)
        pdf.ln(10)
        pdf.cell(200, 10, f"Student Name: {self.StudentName.get()}", ln=True)
        pdf.cell(200, 10, f"Student ID: {self.StudentId.get()}", ln=True)
        pdf.cell(200, 10, f"First Term Fee: {self.FirstTermFee.get()}", ln=True)
        pdf.cell(200, 10, f"Second Term Fee: {self.SecondTermFee.get()}", ln=True)
        pdf.cell(200, 10, f"Third Term Fee: {self.ThirdTermFee.get()}", ln=True)
        pdf.cell(200, 10, f"Total Fees Paid: {self.TotalFeePaid.get()}", ln=True)
        pdf.cell(200, 10, f"Outstanding Balance: {self.OutstandingBalance.get()}", ln=True)
        pdf.cell(200, 10, f"Payment Date: {self.PaymentDate.get()}", ln=True)
        pdf.cell(200, 10, f"Academic Year: {self.AcademicYear.get()}", ln=True)

        
        save_location = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if save_location:
            pdf.output(save_location)
            messagebox.showinfo("Success", "PDF downloaded successfully")


    def iExit_payment(self):
        iExit = messagebox.askyesno("School Management System", "Confirm you want to exit")
        if iExit:
            try:
                if self.db.is_connected():
                    self.db.close()

                self.root.quit()
                self.root.destroy()  

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while exiting: {str(e)}")

                


        
#================================================Teachers Page===============================================

        

    def teacher_page(self):
        

        teacher_frame = tk.Frame(self.main_frame)
        teacher_frame.place(x=0, y=0, width=1375, height=780)
        lb = tk.Label(teacher_frame, text='Teachers Information', fg='#208529', font=('Bold', 30))
        lb.place(x=500, y=20)




        self.NameOfTeacher = StringVar()
        self.TeacherId = StringVar()
        self.DateOfBirth = StringVar()
        self.AssignedClass = StringVar()
        self.Gender = StringVar()
        self.YearEmployed = StringVar()
        self.TeacherAddress = StringVar()
        self.TeacherEmail = StringVar()
        self.TeacherPhone = StringVar()
        self.EducationalLevel = StringVar()
        self.SalaryAmount = StringVar()

        self.create_form_fields_teacher(teacher_frame)
        self.create_teachers_table(teacher_frame)


    def create_form_fields_teacher(self, main_frame):
        teacher_name = tk.Label(main_frame, text="Teacher's Name:", font=("Arial", 12))
        teacher_name.place(x=50, y=100)  
        TeacherEntry = tk.Entry(main_frame, textvariable=self.NameOfTeacher, font=("Arial", 12))
        TeacherEntry.place(x=250, y=100, width=300)


        TeachId=tk.Label(main_frame, text="Teacher ID:",font=("Arial",12))
        TeachId.place(x=50,y=150)
        TeachIdEntry=tk.Entry(main_frame, textvariable=self.TeacherId,font=("Arial",12))
        TeachIdEntry.place(x=250, y=150, width=300)

        dateOfBirth=tk.Label(main_frame, text="Date of Birth:",font=("Arial",12))
        dateOfBirth.place(x=50, y=200)
        dateEntry=tk.Entry(main_frame, textvariable=self.DateOfBirth,font=("Arial",12))
        dateEntry.place(x=250, y=200, width=300)

        AssignClass=tk.Label(main_frame, text="Assigned Class:",font=("Arial",12))
        AssignClass.place(x=50, y=250)
        AssignClassEntry=tk.Entry(main_frame, textvariable=self.AssignedClass,font=("Arial",12))
        AssignClassEntry.place(x=250, y=250, width=300)

        gender=tk.Label(main_frame, text="Gender:",font=("Arial",12))
        gender.place(x=50, y=300)
        genderEntry=tk.Entry(main_frame, textvariable=self.Gender,font=("Arial",12))
        genderEntry.place(x=250, y=300, width=300)

        EmployedYear=tk.Label(main_frame, text="Year Of Employment:",font=("Arial",12))
        EmployedYear.place(x=50, y=350)
        EmployedYearEntry=tk.Entry(main_frame, textvariable=self.YearEmployed,font=("Arial",12))
        EmployedYearEntry.place(x=250, y=350, width=300)

        TeacherAdd=tk.Label(main_frame, text="Teacher's Address:",font=("Arial",12))
        TeacherAdd.place(x=50, y=400)
        TeacherAddEntry=tk.Entry(main_frame, textvariable=self.TeacherAddress,font=("Arial",12))
        TeacherAddEntry.place(x=250, y=400, width=300)

        TeacherEmail=tk.Label(main_frame, text="Teacher's Email:",font=("Arial",12))
        TeacherEmail.place(x=50, y=450)      
        TeacherEmailEntry=tk.Entry(main_frame, textvariable=self.TeacherEmail,font=("Arial",12))
        TeacherEmailEntry.place(x=250, y=450, width=300)

        TeacherPhone=tk.Label(main_frame, text="Teachers's Phone:",font=("Arial",12))
        TeacherPhone.place(x=50, y=500)
        TeacherPhoneEntry=tk.Entry(main_frame, textvariable=self.TeacherPhone,font=("Arial",12))
        TeacherPhoneEntry.place(x=250, y=500, width=300)

        EduLevel=tk.Label(main_frame, text="Education Level:",font=("Arial",12))
        EduLevel.place(x=50, y=550)
        EduLevelEntry=tk.Entry(main_frame, textvariable=self.EducationalLevel,font=("Arial",12))
        EduLevelEntry.place(x=250, y=550, width=300)
        
        SalaryAmount=tk.Label(main_frame, text="Salary Amount:",font=("Arial",12))
        SalaryAmount.place(x=50, y=600)
        SalaryAmountEntry=tk.Entry(main_frame, textvariable=self.SalaryAmount,font=("Arial",12))
        SalaryAmountEntry.place(x=250, y=600, width=300)

        ButtonFrame = Frame(main_frame, bd=20)
        ButtonFrame.place(x=10, y=710, width=1400, height=70)

        BtnAdd = tk.Button(ButtonFrame, text="Add New", bg="green", fg="white",
                                 font=("arial", 12, "bold"), width=15, command=self.BtnAddTeacher)
        BtnAdd.place(x=5, y=0)

        BtnData = tk.Button(ButtonFrame, text="Fetch Data", bg="green", fg="white",
                         font=("arial", 12, "bold"), width=15, command=self.fetch_data_teacher)
        BtnData.place(x=200, y=0)

        BtnUpdate = tk.Button(ButtonFrame,text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=15,command=self.update_teacher)
        BtnUpdate.place(x=450, y=0)

        BtnDelete = tk.Button(ButtonFrame, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=15,command=self.delete_teacher)
        BtnDelete.place(x=700, y=0)

        BtnClear = tk.Button(ButtonFrame, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=15,command=self.clear_teacher)
        BtnClear.place(x=950, y=0)

        BtnExit = tk.Button(ButtonFrame, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=15,command=self.iExit_teacher)
        BtnExit.place(x=1180, y=0)

        self.db = mysql.connector.connect(host='localhost', user='root', password='Oluwaseyi,2019', database='schoolmanagementsystem')
        self.cursor = self.db.cursor()


   

    def BtnAddTeacher(self):
        try:
           
        
           sql_check = "SELECT * FROM teacher WHERE TeacherId=%s"
           val_check = (self.TeacherId.get(),)
           self.cursor.execute(sql_check, val_check)
           result = self.cursor.fetchone()

           if result:
               messagebox.showerror("Error", "Teacher ID already exists. Please use a unique ID.")
           else:
            
              sql = """INSERT INTO teacher (NameOfTeacher, TeacherId, DateOfBirth, Gender, YearEmployed, TeacherAddress, AssignedClass, TeacherPhone, TeacherEmail,EducationalLevel,SalaryAmount) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"""
              val = (self.NameOfTeacher.get(),self.TeacherId.get(),  self.DateOfBirth.get(), 
                     self.Gender.get(), self.YearEmployed.get(),self.TeacherAddress.get(),self.AssignedClass.get(), self.TeacherPhone.get(), self.TeacherEmail.get(),
                     self.EducationalLevel.get(),self.SalaryAmount.get())
              self.cursor.execute(sql, val)
              self.db.commit()

              messagebox.showinfo("Success", "Teacher Added Successfully")
              self.fetch_data()  
        except Exception as e:
            self.db.rollback()
            messagebox.showerror("Error", f"An error occurred: {str(e)}")




    def create_teachers_table(self, frame):
        
        teacher_frame = tk.Frame(frame)
        teacher_frame.place(x=600, y=100, width=750, height=600)

        scroll_x = ttk.Scrollbar(teacher_frame, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(teacher_frame, orient=tk.VERTICAL)

        self.teachers_table = ttk.Treeview(teacher_frame, columns=("NameOfTeacher", "TeacherId", "DateOfBirth",
                                                                    "AssignedClass", "Gender", "YearEmployed", 
                                                                    "TeacherAddress", "TeacherEmail", 
                                                                    "TeacherPhone", "EducationalLevel","SalaryAmount"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_x.config(command=self.teachers_table.xview)
        scroll_y.config(command=self.teachers_table.yview)

     
        self.teachers_table.heading("NameOfTeacher", text="Name of Teacher")
        self.teachers_table.heading("TeacherId", text="Teacher ID")
        self.teachers_table.heading("DateOfBirth", text="Date Of Birth")
        self.teachers_table.heading("AssignedClass", text="Assigned Class")
        self.teachers_table.heading("Gender", text="Gender")
        self.teachers_table.heading("YearEmployed", text="Year Employed")
        self.teachers_table.heading("TeacherAddress", text="Teacher Address")
        self.teachers_table.heading("TeacherEmail", text="Teacher Email")
        self.teachers_table.heading("TeacherPhone", text="Teacher Phone")
        self.teachers_table.heading("EducationalLevel", text="Educational Level")
        self.teachers_table.heading("SalaryAmount", text="Salary Amount")


        
        self.teachers_table["show"] = "headings"

       
        self.teachers_table.column("NameOfTeacher", width=100)
        self.teachers_table.column("TeacherId", width=100)
        self.teachers_table.column("DateOfBirth", width=100)
        self.teachers_table.column("AssignedClass", width=100)
        self.teachers_table.column("Gender", width=100)
        self.teachers_table.column("YearEmployed", width=100)
        self.teachers_table.column("TeacherAddress", width=100)
        self.teachers_table.column("TeacherEmail", width=100)
        self.teachers_table.column("TeacherPhone", width=100)
        self.teachers_table.column("EducationalLevel", width=100)
        self.teachers_table.column("SalaryAmount", width=100)


        self.teachers_table.pack(fill=tk.BOTH, expand=1)
        self.teachers_table.bind("<ButtonRelease-1>", self.get_cursor_teacher)


    def update_teacher(self):
        if self.TeacherId.get() == "":
            messagebox.showerror("Error", "Please select a record to update")
        else:
            self.db = mysql.connector.connect(host="localhost", username="root", password="Oluwaseyi,2019", database="schoolmanagementsystem")
            self.cursor = self.db.cursor()
            self.cursor.execute("UPDATE teacher SET NameOfTeacher=%s, DateOfBirth=%s, AssignedClass=%s, Gender=%s, YearEmployed=%s, TeacherAddress=%s, TeacherEmail=%s, TeacherPhone=%s, EducationalLevel=%s,SalaryAmount=%s WHERE TeacherId=%s", (
                self.NameOfTeacher.get(),
                self.DateOfBirth.get(),
                self.AssignedClass.get(),
                self.Gender.get(),
                self.YearEmployed.get(),
                self.TeacherAddress.get(),
                self.TeacherEmail.get(),
                self.TeacherPhone.get(),
                self.EducationalLevel.get(),
                self.SalaryAmount.get()
            ))
            self.db.commit()
            self.fetch_data()
            self.db.close()
            messagebox.showinfo("Success", "Record has been updated")

    def fetch_data_teacher(self):
        try:
            self.cursor.execute("SELECT * FROM teacher")
            rows = self.cursor.fetchall()

            if len(rows) != 0:
                self.teachers_table.delete(*self.teachers_table.get_children())
                for row in rows:
                    self.teachers_table.insert("", tk.END, values=row)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"An error occurred while fetching data: {str(e)}")
        finally:
            self.cursor.close()  

    def get_cursor_teacher(self, event=""):
        cursor_row=self.teachers_table.focus()
        content=self.teachers_table.item(cursor_row)
        row=content['values']
        self.NameOfTeacher.set(row[0])
        self.TeacherId.set(row[1])
        self.DateOfBirth.set(row[2])
        self.AssignedClass.set(row[3])
        self.Gender.set(row[4])
        self.YearEmployed.set(row[5])
        self.TeacherAddress.set(row[6])
        self.TeacherEmail.set(row[7])
        self.TeacherPhone.set(row[8])
        self.EducationalLevel.set(row[9])
        self.SalaryAmount.set(row[10])

    def delete_teacher(self):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this teacher?"):
            try:
                sql = "DELETE FROM teacher WHERE TeacherId=%s"
                val = (self.TeacherId.get(),)
                self.cursor.execute(sql, val)
                self.db.commit()
                self.fetch_data_teacher()
                self.clear_teacher()
                messagebox.showinfo("Success", "Record has been deleted")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def clear_teacher(self):
        self.NameOfTeacher.set("")
        self.TeacherId.set("")
        self.DateOfBirth.set("")
        self.AssignedClass.set("")
        self.Gender.set("")
        self.YearEmployed.set("")
        self.TeacherAddress.set("")
        self.TeacherEmail.set("")
        self.TeacherPhone.set("")
        self.EducationalLevel.set("")
        self.SalaryAmount.set("")


    def iExit_teacher(self):
       iExit = messagebox.askyesno("School Management System", "Confirm you want to exit")
       if iExit > 0:
          self.db.close()  
          self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
   # app = SchoolManagementSystem(root)
    root.mainloop()
