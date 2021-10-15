from tkinter import *
from tkinter import ttk 
import random
import tkinter.messagebox
import datetime
import time
import tempfile, os #printer
import employee_database

#front_end

class Employee:
    def __init__(self,root): 
        self.root = root #name of the system
        self.root.title('Employee Database Management System') #title of DB
        self.root.geometry('1200x800+0+0') #+0+0 are coordinates
        self.root.configure(bg='#89abed')
        
        
        
        
        
        
        #create frames
        main_frame = Frame(self.root, bd=2, width=1200, height=450, bg='#89abed', relief = FLAT)
        main_frame.grid()
        
        top_frame_1 = Frame(self.root, bd=2, width=1200, height=50, bg='#89abed', relief=FLAT)
        top_frame_1.grid(row=2, column=0)
        
        top_frame_2 = Frame(self.root, bd=2, width=168, height=70, bg='#89abed', relief=FLAT)
        top_frame_2.grid(row=1, column=0)
        
        top_frame_3 = Frame(self.root, bd=2, width=1200, height=300, bg='#AAABE6', relief=FLAT)
        top_frame_3.grid(row=0, column=0)

        left_frame = Frame(top_frame_3, bd=5, width=1200, height=300, padx=2, bg='#AAABE6', relief=FLAT)
        left_frame.pack(side=LEFT)
        left_frame_1 = Frame(left_frame, bd=5, width=168, height=180, padx=4, pady=4, bg='#AAABE6', relief=FLAT)
        left_frame_1.pack(side=TOP)
        
        left_frame_2 = Frame(left_frame, bd=5, width=600, height=180, padx=2, bg='#AAABE6', relief=FLAT)
        left_frame_2.pack(side=TOP)
        left_frame_2_left = Frame(left_frame_2, bd=5, width=300, height=170, padx=2, bg='#AAABE6', relief=FLAT)
        left_frame_2_left.pack(side=LEFT)
        left_frame_2_right = Frame(left_frame_2, bd=5, width=300, height=170, padx=2, bg='#AAABE6', relief=FLAT)
        left_frame_2_right.pack(side=RIGHT)
        
        right_frame_1 = Frame(top_frame_3, bd=5, width=320, height=400, padx=2, bg='#AAABE6', relief=FLAT)
        right_frame_1.pack(side=RIGHT)
        right_frame_1a = Frame(right_frame_1, bd=5, width=310, height=300, padx=2, bg='#AAABE6', relief=FLAT)
        right_frame_1a.pack(side=TOP)
        
        
        right_frame_2 = Frame(top_frame_3, bd=5, width=300, height=400, padx=2, bg='#AAABE6', relief=FLAT)
        right_frame_2.pack(side=RIGHT)
        right_frame_2a = Frame(right_frame_2, bd=2, width=280, height=50, padx=2, bg='#AAABE6', relief=FLAT)
        right_frame_2a.pack(side=TOP)
        right_frame_2b = Frame(right_frame_2, bd=5, width=280, height=180, padx=2, bg='#AAABE6', relief=FLAT)
        right_frame_2b.pack(side=TOP)
        right_frame_2c = Frame(right_frame_2, bd=5, width=280, height=100, padx=2, bg='#AAABE6', relief=FLAT)
        right_frame_2c.pack(side=TOP)
        right_frame_2d = Frame(right_frame_2, bd=5, width=280, height=50, padx=2, bg='#AAABE6', relief=FLAT)
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
        self.txt_receipt = Text(right_frame_1a, bg='#ffffff', height=28, width=30, bd=10, font=('arial', 9,'bold'))
        self.txt_receipt.grid(row=0,column=0)
        #=========================================Heading===========================================================
        
        self.lb_label = Label(top_frame_2, font=('arial', 10, 'bold'), padx=2, pady=2, bg='#89abed', width=197,bd=2,
        text='Reference\tFirstname\tLastname\tAddress\t\tGender\tMobile\tNI Number\tStudent Loan\tTax\tPension \ Deductions\tNet Pay\t\tGross Pay')
        self.lb_label.grid(row=0, column=0, columnspan=17)
        
        
        
        
        #=============================Listbox and Scrollbar==================================================
        scrollbar = Scrollbar(top_frame_2)
        scrollbar.grid(row=1, column=1, sticky='ns')
        
        first_employee = Listbox(top_frame_2, width=168, height=5, bg='#ffffff',font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        first_employee.bind('<<Listbox_Select>>')
        first_employee.grid(row=1, column=0, padx=1, sticky='nsew')
        scrollbar.config(command = first_employee.xview)
        #=========================================Reference============================================================
        self.lb_reference= Label(left_frame_1, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Reference', bd=1, anchor='w')
        self.lb_reference.grid(row=0,column=0)
        self.txt_reference= Entry(left_frame_1, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=60, justify= 'left', textvariable = reference)
        self.txt_reference.grid(row=0,column=1)
        
        
        #------------------------------------------First Name-----------------------------------------------------------
        self.lb_first_name= Label(left_frame_1, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'First Name', bd=1, anchor='w')
        self.lb_first_name.grid(row=1,column=0)
        self.txt_first_name= Entry(left_frame_1, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=60, justify= 'left', textvariable = first_name)
        self.txt_first_name.grid(row=1,column=1)
        
        #------------------------------------------Last Name-----------------------------------------------------------
        self.lb_last_name= Label(left_frame_1, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Last Name', bd=1, anchor='w')
        self.lb_last_name.grid(row=2,column=0)
        self.txt_last_name= Entry(left_frame_1, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=60, justify= 'left', textvariable = last_name)
        self.txt_last_name.grid(row=2,column=1)
        
        #------------------------------------------Address-----------------------------------------------------------
        self.lb_address= Label(left_frame_1, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Address', bd=1, anchor='w')
        self.lb_address.grid(row=3,column=0)
        self.txt_address= Entry(left_frame_1, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=60, justify= 'left', textvariable = address)
        self.txt_address.grid(row=3,column=1)
        
        
        #------------------------------------------Gender-----------------------------------------------------------
        self.lb_gender= Label(left_frame_1, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Gender', bd=1, anchor='w')
        self.lb_gender.grid(row=4,column=0)
        self.txt_gender= Entry(left_frame_1, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=60, justify= 'left', textvariable = gender)
        self.txt_gender.grid(row=4,column=1)
        
        #------------------------------------------Phone-----------------------------------------------------------
        self.lb_phone= Label(left_frame_1, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Phone', bd=1, anchor='w')
        self.lb_phone.grid(row=5,column=0)
        self.txt_phone= Entry(left_frame_1, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=60, justify= 'left', textvariable = phone)
        self.txt_phone.grid(row=5,column=1)
        
        #------------------------------------------City Weighting-----------------------------------------------------------
        self.lb_city_weighting= Label(left_frame_2_left, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'City Weighting', bd=1, anchor='e')
        self.lb_city_weighting.grid(row=0,column=0)
        self.txt_city_weighting= Entry(left_frame_2_left, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = city_weighting)
        self.txt_city_weighting.grid(row=0,column=1)
        
        #------------------------------------------Basic Salary-----------------------------------------------------------
        self.lb_basic_salary= Label(left_frame_2_left, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Salary', bd=1, anchor='e')
        self.lb_basic_salary.grid(row=1,column=0)
        self.txt_basic_salary= Entry(left_frame_2_left, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = basic_salary)
        self.txt_basic_salary.grid(row=1,column=1)
        
        #------------------------------------------Over Time-----------------------------------------------------------
        self.lb_over_time= Label(left_frame_2_left, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Over Time', bd=1, anchor='e')
        self.lb_over_time.grid(row=2,column=0)
        self.txt_over_time= Entry(left_frame_2_left, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = over_time)
        self.txt_over_time.grid(row=2,column=1)
        
        #------------------------------------------Other Payment Due-----------------------------------------------------------
        self.lb_other_payment_due= Label(left_frame_2_left, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Other Payment', bd=1, anchor='e')
        self.lb_other_payment_due.grid(row=3,column=0)
        self.txt_other_payment_due= Entry(left_frame_2_left, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = other_payment_due)
        self.txt_other_payment_due.grid(row=3,column=1)
        
        #------------------------------------------Tax-----------------------------------------------------------
        self.lb_tax= Label(left_frame_2_right, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Tax', bd=1, anchor='e')
        self.lb_tax.grid(row=0,column=0)
        self.txt_tax= Entry(left_frame_2_right, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = tax)
        self.txt_tax.grid(row=0,column=1)
        
        #------------------------------------------Pension-----------------------------------------------------------
        self.lb_pension= Label(left_frame_2_right, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Pension', bd=1, anchor='e')
        self.lb_pension.grid(row=1,column=0)
        self.txt_pension= Entry(left_frame_2_right, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = pension)
        self.txt_pension.grid(row=1,column=1)
        
        #------------------------------------------Student Loan-----------------------------------------------------------
        
        self.lb_std_loan= Label(left_frame_2_right, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Student Loan', bd=1, anchor='e')
        self.lb_std_loan.grid(row=2,column=0)
        self.txt_std_loan= Entry(left_frame_2_right, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = std_loan)
        self.txt_std_loan.grid(row=2,column=1)
        
        #------------------------------------------NI Payment-----------------------------------------------------------
        self.lb_ni_payment= Label(left_frame_2_right, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'NI Payment', bd=1, anchor='e')
        self.lb_ni_payment.grid(row=3,column=0)
        self.txt_ni_payment= Entry(left_frame_2_right, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = ni_payment)
        self.txt_ni_payment.grid(row=3,column=1)
    
    #------------------------------------------Pay Day-----------------------------------------------------------
        self.lb_payday= Label(right_frame_2a, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Pay Day', bd=2,anchor='w', justify=LEFT)
        self.lb_payday.grid(row=0,column=0, sticky =W)
        self.txt_payday= Entry(right_frame_2a, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=19, justify= 'left', textvariable = payday)
        self.txt_payday.grid(row=0,column=1)
        
        
        
        
        #------------------------------------------Tax Period-----------------------------------------------------------
        self.lb_tax_period= Label(right_frame_2b, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Tax Period', bd=1, anchor='w', justify=LEFT)
        self.lb_tax_period.grid(row=0,column=0, sticky =W)
        self.txt_tax_period= Entry(right_frame_2b, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = tax_period)
        self.txt_tax_period.grid(row=0,column=1)
        
        
        #------------------------------------------Tax Code-----------------------------------------------------------
        self.lb_tax_code= Label(right_frame_2b, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Tax Code', bd=1, anchor='w', justify=LEFT)
        self.lb_tax_code.grid(row=1,column=0, sticky =W)
        self.txt_tax_code= Entry(right_frame_2b, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = tax_code)
        self.txt_tax_code.grid(row=1,column=1)
        
         #------------------------------------------NI Number-----------------------------------------------------------
        self.lb_ni_number= Label(right_frame_2b, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'NI Number', bd=1, anchor='w', justify=LEFT)
        self.lb_ni_number.grid(row=2,column=0, sticky =W)
        self.txt_ni_number= Entry(right_frame_2b, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = ni_number)
        self.txt_ni_number.grid(row=2,column=1)
        
         #------------------------------------------NI Code-----------------------------------------------------------
        self.lb_ni_code= Label(right_frame_2b, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'NI Code', bd=1, anchor='w', justify=LEFT)
        self.lb_ni_code.grid(row=3,column=0, sticky =W)
        self.txt_ni_code= Entry(right_frame_2b, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = ni_code)
        self.txt_ni_code.grid(row=3,column=1)
        
        #------------------------------------------Taxable Pay-----------------------------------------------------------
        self.lb_taxable_pay= Label(right_frame_2c, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Taxable Pay', bd=1, anchor='w', justify=LEFT)
        self.lb_taxable_pay.grid(row=0,column=0, sticky =W)
        self.txt_taxable_pay= Entry(right_frame_2c, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=12, justify= 'left', textvariable = taxable_pay)
        self.txt_taxable_pay.grid(row=0,column=1)
        
        
        
        #------------------------------------------Pensionable Pay-----------------------------------------------------------
        self.lb_pensionable_pay= Label(right_frame_2c, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Pensionable Pay', bd=1, anchor='w', justify=LEFT)
        self.lb_pensionable_pay.grid(row=1,column=0, sticky =W)
        self.txt_pensionable_pay= Entry(right_frame_2c, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=12, justify= 'left', textvariable = pensionable_pay)
        self.txt_pensionable_pay.grid(row=1,column=1)
        
        #-------------------------------------------Net Pay-----------------------------------------------------------
        self.lb_net_pay= Label(right_frame_2d, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Net Pay', bd=1, anchor='w', justify=LEFT)
        self.lb_net_pay.grid(row=0,column=0, sticky =W)
        self.txt_net_pay= Entry(right_frame_2d, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = net_pay)
        self.txt_net_pay.grid(row=0,column=1) 
        
        #-------------------------------------------Gross Pay-----------------------------------------------------------
        self.lb_gross_pay= Label(right_frame_2d, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Gross Pay', bd=1, anchor='w', justify=LEFT)
        self.lb_gross_pay.grid(row=1,column=0, sticky =W)
        self.txt_gross_pay= Entry(right_frame_2d, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = gross_pay)
        self.txt_gross_pay.grid(row=1,column=1)   
        
        #-------------------------------------------Deductions-----------------------------------------------------------
        self.lb_deductions= Label(right_frame_2d, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Deductions', bd=1, anchor='w', justify=LEFT)
        self.lb_deductions.grid(row=2,column=0, sticky =W)
        self.txt_deductions= Entry(right_frame_2d, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = deductions)
        self.txt_deductions.grid(row=2,column=1)  
        #======================================Buttons=============================================================
        self.button_add_new_total= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Add New/Total').grid(row=0, column=0, padx=1)
        
        self.button_print= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Print').grid(row=0, column=1, padx=1)
        
        self.button_display= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Display').grid(row=0, column=2, padx=1)
        
        self.button_update= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Update').grid(row=0, column=3, padx=1) 
        
        self.button_delete= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Delete').grid(row=0, column=4, padx=1)       

        self.button_search= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Search').grid(row=0, column=5, padx=1)
        
        self.button_Reset= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Reset').grid(row=0, column=6, padx=1)  
        
        self.button_Exit= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#ffffff', width=8, text = 'Exit').grid(row=0, column=7, padx=1)
                 
if __name__ == '__main__': #main name of the system
    root = Tk()
    application = Employee(root)
    root.mainloop()


















































































