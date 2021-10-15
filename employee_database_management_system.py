from tkinter import *
from tkinter import ttk 
import random
import tkinter.messagebox
import datetime
import time
import tempfile, os #printer

class Employee:
    def __init__(self,root): 
        self.root = root #name of the system
        self.root.title('Employee Database Management System') #title of DB
        self.root.geometry('1350x800+0+0') #+0+0 are coordinates
        self.root.configure(bg='#113B8E')
        
        #create frames
        main_frame = Frame(self.root, bd=7, width=1340, height=650, bg='#113B8E', relief = RIDGE)
        main_frame.grid()
        
        top_frame_1 = Frame(self.root, bd=7, width=1340, height=50, bg='#113B8E', relief=RIDGE)
        top_frame_1.grid(row=2, column=0)
        
        top_frame_2 = Frame(self.root, bd=7, width=1340, height=100, bg='#113B8E', relief=RIDGE)
        top_frame_2.grid(row=1, column=0)
        
        top_frame_3 = Frame(self.root, bd=7, width=1340, height=400, bg='#113B8E', relief=RIDGE)
        top_frame_3.grid(row=0, column=0)

        left_frame = Frame(top_frame_3, bd=5, width=1340, height=400, padx=2, bg='#113B8E', relief=RIDGE)
        left_frame.pack(side=LEFT)
        left_frame_1 = Frame(left_frame, bd=5, width=600, height=180, padx=4, pady=4, bg='#AAABE6', relief=RIDGE)
        left_frame_1.pack(side=TOP)
        
        left_frame_2 = Frame(left_frame, bd=5, width=600, height=180, padx=2, bg='#113B8E', relief=RIDGE)
        left_frame_2.pack(side=TOP)
        left_frame_2_left = Frame(left_frame_2, bd=5, width=300, height=170, padx=2, bg='#AAABE6', relief=RIDGE)
        left_frame_2_left.pack(side=LEFT)
        left_frame_2_right = Frame(left_frame_2, bd=5, width=300, height=170, padx=2, bg='#AAABE6', relief=RIDGE)
        left_frame_2_right.pack(side=RIGHT)
        
        right_frame_1 = Frame(top_frame_3, bd=5, width=320, height=400, padx=2, bg='#113B8E', relief=RIDGE)
        right_frame_1.pack(side=RIGHT)
        right_frame_1a = Frame(right_frame_1, bd=5, width=310, height=300, padx=2, bg='#AAABE6', relief=RIDGE)
        right_frame_1a.pack(side=TOP)
        
        right_frame_2 = Frame(top_frame_3, bd=5, width=300, height=400, padx=2, bg='#113B8E', relief=RIDGE)
        right_frame_2.pack(side=RIGHT)
        right_frame_2a = Frame(right_frame_2, bd=5, width=280, height=50, padx=2, bg='#AAABE6', relief=RIDGE)
        right_frame_2a.pack(side=TOP)
        right_frame_2b = Frame(right_frame_2, bd=5, width=280, height=180, padx=2, bg='#AAABE6', relief=RIDGE)
        right_frame_2b.pack(side=TOP)
        right_frame_2c = Frame(right_frame_2, bd=5, width=280, height=100, padx=2, bg='#AAABE6', relief=RIDGE)
        right_frame_2c.pack(side=TOP)
        right_frame_2d = Frame(right_frame_2, bd=5, width=280, height=50, padx=2, bg='#AAABE6', relief=RIDGE)
        right_frame_2d.pack(side=TOP)
        #==========================================variables======================================================
        global Ed #employee database
        first_name = StringVar()
        last_name = StringVar()
        address = StringVar()
        reference = StringVar()
        city_weighting = IntVar() #extra wages employees can get for living in the city
        phone = StringVar()
        basic_salary = StringVar()
        over_time = StringVar()
        gross_pay = StringVar()
        net_pay = StringVar()
        tax = StringVar()
        pension = StringVar()
        std_loan = StringVar()
        ni_payment = StringVar()
        deductions = StringVar()
        gender = StringVar()
        payday = StringVar()
        tax_period = StringVar()
        ni_number = StringVar()
        ni_code = StringVar()
        taxable_pay = StringVar()
        pensionable_pay = StringVar()
        other_payment_due = StringVar()
        tax_code = StringVar()
        
        city_weighting.set(" ")
        basic_salary.set(" ")
        other_payment_due.set("0.00")
        #=========================================Receipt============================================================
        self.txt_receipt = Text(right_frame_1a, bg='#c7f7fa', height=23, width=42, bd=10, font=('arial', 9,'bold'))
        self.txt_receipt.grid(row=0,column=0)
        #=========================================Heading===========================================================
        self.lb_label = Label(top_frame_2, font=('arial', 10, 'bold'), padx=6, pady=2,
        text='Reference\tFirstname\tLastname\tAddress\t\tGender\tMobile\tNI Number\tStudent Loan\tTax\tPension \ Deductions\tNet Pay\t\tGross Pay')
        self.lb_label.grid(row=0, column=0, columnspan=17)
        
        #=============================Listbox and Scrollbar==================================================
        scrollbar = Scrollbar(top_frame_2)
        scrollbar.grid(row=1, column=1, sticky='ns')
        
        first_employee = Listbox(top_frame_2, width=145, height=5, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        first_employee.bind('<<Listbox_Select>>')
        first_employee.grid(row=1, column=0, padx=1, sticky='nsew')
        scrollbar.config(command = first_employee.xview)
        #=========================================Reference============================================================
        self.lb_reference= Label(left_frame_1, font=('arial', 12, 'bold'), text = 'Reference', bd=7, anchor='w')
        self.lb_reference.grid(row=0,column=0)
        self.txt_reference= Entry(left_frame_1, font=('arial', 12, 'bold'), bg='#c7f7fa',bd=5, width=60, justify= 'left', textvariable = reference)
        self.txt_reference.grid(row=0,column=1)
        
        #------------------------------------------First Name-----------------------------------------------------------
        self.lb_first_name= Label(left_frame_1, font=('arial', 12, 'bold'), text = 'First Name', bd=7, anchor='w')
        self.lb_first_name.grid(row=1,column=0)
        self.txt_first_name= Entry(left_frame_1, font=('arial', 12, 'bold'), bg='#c7f7fa',bd=5, width=60, justify= 'left', textvariable = first_name)
        self.txt_first_name.grid(row=1,column=1)
        
        #------------------------------------------Last Name-----------------------------------------------------------
        self.lb_last_name= Label(left_frame_1, font=('arial', 12, 'bold'), text = 'Last Name', bd=7, anchor='w')
        self.lb_last_name.grid(row=2,column=0)
        self.txt_last_name= Entry(left_frame_1, font=('arial', 12, 'bold'), bg='#c7f7fa',bd=5, width=60, justify= 'left', textvariable = last_name)
        self.txt_last_name.grid(row=2,column=1)
        #==========================================================================================================
        
        
if __name__ == '__main__': #main name of the system
    root = Tk()
    application = Employee(root)
    root.mainloop()





























