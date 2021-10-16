from tkinter import *
from tkinter import ttk 
import random
import tkinter.messagebox
import datetime
import time
import employee_database

#front_end


class Employee:
    def __init__(self,root): 
        self.root = root #name of the system
        self.root.title('Employee Database Management System') #title of DB
        self.root.geometry('1200x800+0+0') #+0+0 are coordinates
        self.root.configure(bg='#89abed')
        
 
    
        
        #create frames
        main_frame = Frame(self.root, bd=2, width=1200, height=450, bg='#89abed', relief = RIDGE)
        main_frame.grid()
        
        top_frame_1 = Frame(self.root, bd=2, width=1200, height=50, bg='#89abed', relief=FLAT)
        top_frame_1.grid(row=2, column=0)
        
        top_frame_2 = Frame(self.root, bd=2, width=168, height=70, bg='#89abed', relief=RIDGE)
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
    
       #==========================================Variables======================================================
        global Ed #employee database
        first_name = StringVar()
        last_name = StringVar()
        address = StringVar()
        reference = StringVar()
        reimbursement = IntVar() #extra wages employees can get for living in the city
        phone = StringVar()
        basic_salary = StringVar()
        over_time = StringVar()
        gross_pay = StringVar()
        net_pay = StringVar()
        tax = StringVar()
        pension = StringVar()
        std_loan = StringVar()
        ss_payment = StringVar()
        deductions = StringVar()
        gender = StringVar()
        payday = StringVar()
        tax_period = StringVar()
        ss_number = StringVar()
        bi_code = StringVar()
        taxable_pay = StringVar()
        pensionable_pay = StringVar()
        other_payment_due = StringVar()
        tax_code = StringVar()
        
        reimbursement.set(" ")
        basic_salary.set(" ")
        other_payment_due.set("0.00")
        
    #==========================================Functions=====================================================
        def add_data(): #add new data to the database
            if(len(reference.get())!=0): 
                employee_database.add_employee_record(reference.get(), first_name.get(), last_name.get(), address.get(), gender.get(), phone.get(), ss_number.get(),std_loan.get(),tax.get(),pension.get(),deductions.get(),net_pay.get(), gross_pay.get())
                first_employee.delete(0, END) #adds data to the Listbox fields
                first_employee.insert(END, (reference.get(), first_name.get(), last_name.get(), address.get(), gender.get(), phone.get(), ss_number.get(),std_loan.get(),tax.get(),pension.get(),deductions.get(),net_pay.get(), gross_pay.get()))
                
        def display_data(): #display employee data
            first_employee.delete(0, END)
            for row in employee_database.view_data():
                first_employee.insert(END, row, str(" "))
        
        def employee_record(event): #add all of the info into the listbox, call this function in listbox
            global ed 
            search_ed = first_employee.curselection()[0] #search inside employee data, curselection returns the index of currently selected items
            ed = first_employee.get(search_ed)
            
            self.txt_reference.delete(0,END)
            self.txt_reference.insert(END, ed[1])
            self.txt_first_name.delete(0,END)
            self.txt_first_name.insert(END, ed[2])           
            self.txt_last_name.delete(0,END)
            self.txt_last_name.insert(END, ed[3])
            self.txt_address.delete(0,END)
            self.txt_address.insert(END, ed[4])
            self.txt_gender.delete(0,END)
            self.txt_gender.insert(END, ed[5])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(END, ed[6])
            self.txt_ss_number.delete(0,END)
            self.txt_ss_number.insert(END, ed[7])
            self.txt_std_loan.delete(0,END)
            self.txt_std_loan.insert(END, ed[8])
            self.txt_tax.delete(0,END)
            self.txt_tax.insert(END, ed[9])   
            self.txt_pension.delete(0,END)
            self.txt_pension.insert(END, ed[10])     
            self.txt_deductions.delete(0,END)
            self.txt_deductions.insert(END, ed[11]) 
            self.txt_net_pay.delete(0,END)
            self.txt_net_pay.insert(END, ed[12])  
            self.txt_gross_pay.delete(0,END)
            self.txt_gross_pay.insert(END, ed[13])             
        
        def delete_data():
            if(len(reference.get())!=0):
                employee_database.delete_record(ed[0]) 
                reset()
                display_data()       
        
        def search_data():
            first_employee.delete(0, END)
            for row in employee_database.search_data (reference.get(), first_name.get(), last_name.get(), address.get(), gender.get(), phone.get(), ss_number.get(),std_loan.get(),tax.get(),pension.get(),deductions.get(),net_pay.get(), gross_pay.get()):
                first_employee.insert(END, row, str(" "))
                
        
        def update_data():
            if(len(reference.get())!=0):
                employee_database.delete_record(ed[0])
            if(len(reference.get())!=0):
                employee.database.add_employee_record(reference.get(), first_name.get(), last_name.get(), address.get(), gender.get(), phone.get(), ss_number.get(),std_loan.get(),tax.get(),pension.get(),deductions.get(),net_pay.get(), gross_pay.get())
                first_employee.delete(0, END)
                first_employee.insert(END, (reference(), first_name.get(), last_name.get(), address.get(), gender.get(), phone.get(), ss_number.get(),std_loan.get(),tax.get(),pension.get(),deductions.get(),net_pay.get(), gross_pay.get()))             
                
        def reset():
            first_name.set(" ")
            last_name.set(" ")
            address.set(" ")
            reference.set(" ")
            reimbursement.set(" ")
            phone.set(" ")
            basic_salary.set(" ")
            over_time.set(" ")
            gross_pay.set(" ")
            net_pay.set(" ")
            tax.set(" ")
            pension.set(" ")
            std_loan.set(" ")
            ss_payment.set(" ")
            deductions.set(" ")
            gender.set(" ")
            payday.set(" ")
            tax_period.set(" ")
            ss_number.set(" ")
            bi_code.set(" ")
            taxable_pay.set(" ")
            pensionable_pay.set(" ")
            tax_code.set(" ")
            other_payment_due.set("0.00")
            self.txt_receipt.delete("1.0", END)
            
        def exit_db_sys():
            exit_db_sys = tkinter.messagebox.askyesno("Employee Database System", "Confirm if you want to exit")
            if exit_db_sys < 0:
                root.destroy()
                return
        
        def pay_reference():
            payday.set(time.strftime('%d/%m/%Y')) #time
            ref_pay = random.randint (16462, 70488)
            ref_paid = ("ref" + str(ref_pay))
            reference.set(ref_paid)
        
        ss_pay = random.randint (344627326, 704884534)
        ss_paid = ("SSN" + str(ss_pay))
        ss_number.set = (ss_pay)
        
        i_date = datetime.datetime.now()
        tax_period.set(i_date.month)
        
        ben_id_code = random.randint (8000, 12000)
        code_bi = ("BIC" + str(ben_id_code))
        bi_code.set(code_bi)
        
        i_tax_code = random.randint (8000, 12000)
        payment_tax_code = ("TCode" + str(i_tax_code))
        tax_code.set(payment_tax_code)
        
        def monthly_salary():
            pay_reference()
            
            BS = float(basic_salary.get())
            RB = float(reimbursement())
            OT = float(over_time())
            OPD = float(other_payment_due())
            
            MTax = ((BS + RB + OT + OPD) * 0.3) 
            TTax = "$", str('%.2f'%(MTax))
            Tax.set(TTax)
            
            m_pension = ((BS + RB + OT + OPD) * 0.02)
            mm_pension = "$", str('%.2f'%(m_pension))
            pension.set(mm_pension)
            
            m_std_loan = ((BS + RB + OT + OPD) * 0.012)
            mm_std_loan = "$", str('%.2f'%(m_std_loan))
            
            m_ss_payment = ((BS + RB + OT + OPD) * 0.011)
            mm_ss_payment = "$", str('%.2f'%(m_ss_payment))
            ss_payment.set(mm_ss_payment)   
            
            deduct = (MTax + m_pension + m_std_loan + m_ss_payment) 
            deduct_payment = "$", str('.2f'%(deduct))
            deductions.set(deduct_payment)
            gross_pay = "$", str('.2f' % (BS + RB + OT + OPD))
            gross_pay.set(gross_pay)
            
            ney_pay_after = (BS + RB + OT + OPD) - deduct
            net_after = "$", str(".2f" % (net_pay_after))
            net_pay(net_after)
            
            taxable_pay.set(TTax)
            pensionable_pay.set(mm_pension)
            
            self.txt_receipt.insert(END, '\t\t Monthly Pay Slip' + "\n\n")
            self.txt_receipt.insert(END, 'Reference: \t\t\t' + reference.get() + "\n")
            self.txt_receipt.insert(END, 'Reference: \t\t\t' + payday.get() + "\n")
            self.txt_receipt.insert(END, 'Employer Name: \t\t\t' + last_name.get() + "\n")
            self.txt_receipt.insert(END, 'Employee Name: \t\t\t' + first_name.get() + "\n\n")
            self.txt_receipt.insert(END, 'Tax: \t\t\t' + tax.get() + "\n")
            self.txt_receipt.insert(END, 'Pension: \t\t\t' + pension.get() + "\n")
            self.txt_receipt.insert(END, 'Student Loan: \t\t\t' + std_loan.get() + "\n")
            self.txt_receipt.insert(END, 'SS Number: \t\t\t' + ss_number.get() + "\n")
            self.txt_receipt.insert(END, 'SS Payment: \t\t\t' + ss_payment.get() + "\n")
            self.txt_receipt.insert(END, 'Deductions: \t\t\t' + deductions.get() + "\n")
            self.txt_receipt.insert(END, 'Reimbursements: \t\t\t' + str('$ %.2f'%(reimbursement.get())) + "\n")
           
            self.txt_receipt.insert(END, '\nTax Paid:\t\t\t' + str( '$ %.2f'%(basic_salary.get())) + "\n")
            self.txt_receipt.insert(END, 'Overtime:\t\t\t' + "$" + over_time.get() + "\n")
            self.txt_receipt.insert(END, 'NetPay:\t\t\t' + net_pay.get() + "\n")
            self.txt_receipt.insert(END, 'Gross Pay:\t\t\t' + gross_pay.get() + "\n")  
        
                      
 
        #******************************************WIDGETS***********************************************************
        #=========================================Receipt============================================================
        self.txt_receipt = Text(right_frame_1a, bg='#ffffff', height=28, width=30, bd=10, font=('arial', 9,'bold'))
        self.txt_receipt.grid(row=0,column=0)
        #=========================================Heading===========================================================
        
        self.lbl_label = Label(top_frame_2, font=('arial', 10, 'bold'), padx=2, pady=2, bg='#89abed', width=160,bd=2,
        text='Reference\tFirstname\tLastname\tAddress\tGender\tMobile\tSS Number\tStudent Loan\tTax\tPension\Deductions\tNet Pay\t\tGross Pay')
        self.lbl_label.grid(row=0, column=0, columnspan=17)

        
        #=============================Listbox and Scrollbar==================================================
        scrollbar = Scrollbar(top_frame_2)
        scrollbar.grid(row=1, column=1, sticky='ns')
        
        first_employee = Listbox(top_frame_2, width=168, height=5, bg='#ffffff',font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        first_employee.bind('<<Listbox_Select>>', employee_record)
        first_employee.grid(row=1, column=0, padx=1, sticky='nsew')
        scrollbar.config(command = first_employee.xview)
        #=========================================Reference============================================================
        self.lbl_reference= Label(left_frame_1, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Reference', bd=1, anchor='w')
        self.lbl_reference.grid(row=0,column=0)
        self.txt_reference= Entry(left_frame_1, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=60, justify= 'left', textvariable = reference)
        self.txt_reference.grid(row=0,column=1)
        
        
        #------------------------------------------First Name-----------------------------------------------------------
        self.lbl_first_name= Label(left_frame_1, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'First Name', bd=1, anchor='w')
        self.lbl_first_name.grid(row=1,column=0)
        self.txt_first_name= Entry(left_frame_1, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=60, justify= 'left', textvariable = first_name)
        self.txt_first_name.grid(row=1,column=1)
        
        #------------------------------------------Last Name-----------------------------------------------------------
        self.lbl_last_name= Label(left_frame_1, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Last Name', bd=1, anchor='w')
        self.lbl_last_name.grid(row=2,column=0)
        self.txt_last_name= Entry(left_frame_1, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=60, justify= 'left', textvariable = last_name)
        self.txt_last_name.grid(row=2,column=1)
        
        #------------------------------------------Address-----------------------------------------------------------
        self.lbl_address= Label(left_frame_1, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Address', bd=1, anchor='w')
        self.lbl_address.grid(row=3,column=0)
        self.txt_address= Entry(left_frame_1, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=60, justify= 'left', textvariable = address)
        self.txt_address.grid(row=3,column=1)
        
        
        #------------------------------------------Gender-----------------------------------------------------------
        self.lbl_gender= Label(left_frame_1, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Gender', bd=1, anchor='w')
        self.lbl_gender.grid(row=4,column=0)
        self.txt_gender= Entry(left_frame_1, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=60, justify= 'left', textvariable = gender)
        self.txt_gender.grid(row=4,column=1)
        
        #------------------------------------------Phone-----------------------------------------------------------
        self.lbl_phone= Label(left_frame_1, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Phone', bd=1, anchor='w')
        self.lbl_phone.grid(row=5,column=0)
        self.txt_phone= Entry(left_frame_1, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=60, justify= 'left', textvariable = phone)
        self.txt_phone.grid(row=5,column=1)
        
        #------------------------------------------City Weighting-----------------------------------------------------------
        self.lbl_reimbursement= Label(left_frame_2_left, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'City Weighting', bd=1, anchor='e')
        self.lbl_reimbursement.grid(row=0,column=0)
        self.txt_reimbursement= Entry(left_frame_2_left, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = reimbursement)
        self.txt_reimbursement.grid(row=0,column=1)
        
        #------------------------------------------Basic Salary-----------------------------------------------------------
        self.lbl_basic_salary= Label(left_frame_2_left, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Salary', bd=1, anchor='e')
        self.lbl_basic_salary.grid(row=1,column=0)
        self.txt_basic_salary= Entry(left_frame_2_left, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = basic_salary)
        self.txt_basic_salary.grid(row=1,column=1)
        
        #------------------------------------------Over Time-----------------------------------------------------------
        self.lbl_over_time= Label(left_frame_2_left, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Over Time', bd=1, anchor='e')
        self.lbl_over_time.grid(row=2,column=0)
        self.txt_over_time= Entry(left_frame_2_left, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = over_time)
        self.txt_over_time.grid(row=2,column=1)
        
        #------------------------------------------Other Payment Due-----------------------------------------------------------
        self.lbl_other_payment_due= Label(left_frame_2_left, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Other Payment', bd=1, anchor='e')
        self.lbl_other_payment_due.grid(row=3,column=0)
        self.txt_other_payment_due= Entry(left_frame_2_left, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = other_payment_due)
        self.txt_other_payment_due.grid(row=3,column=1)
        
        #------------------------------------------Tax-----------------------------------------------------------
        self.lbl_tax= Label(left_frame_2_right, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Tax', bd=1, anchor='e')
        self.lbl_tax.grid(row=0,column=0)
        self.txt_tax= Entry(left_frame_2_right, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = tax)
        self.txt_tax.grid(row=0,column=1)
        
        #------------------------------------------Pension-----------------------------------------------------------
        self.lbl_pension= Label(left_frame_2_right, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Pension', bd=1, anchor='e')
        self.lbl_pension.grid(row=1,column=0)
        self.txt_pension= Entry(left_frame_2_right, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = pension)
        self.txt_pension.grid(row=1,column=1)
        
        #------------------------------------------Student Loan-----------------------------------------------------------
        
        self.lbl_std_loan= Label(left_frame_2_right, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Student Loan', bd=1, anchor='e')
        self.lbl_std_loan.grid(row=2,column=0)
        self.txt_std_loan= Entry(left_frame_2_right, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = std_loan)
        self.txt_std_loan.grid(row=2,column=1)
        
        #------------------------------------------SS Payment-----------------------------------------------------------
        self.lbl_ss_payment= Label(left_frame_2_right, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'SS Payment', bd=1, anchor='e')
        self.lbl_ss_payment.grid(row=3,column=0)
        self.txt_ss_payment= Entry(left_frame_2_right, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=20, justify= 'left', textvariable = ss_payment)
        self.txt_ss_payment.grid(row=3,column=1)
    
    #------------------------------------------Pay Day-----------------------------------------------------------
        self.lbl_payday= Label(right_frame_2a, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Pay Day', bd=2,anchor='w', justify=LEFT)
        self.lbl_payday.grid(row=0,column=0, sticky =W)
        self.txt_payday= Entry(right_frame_2a, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=19, justify= 'left', textvariable = payday)
        self.txt_payday.grid(row=0,column=1)
        
        
        
        
        #------------------------------------------Tax Period-----------------------------------------------------------
        self.lbl_tax_period= Label(right_frame_2b, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Tax Period', bd=1, anchor='w', justify=LEFT)
        self.lbl_tax_period.grid(row=0,column=0, sticky =W)
        self.txt_tax_period= Entry(right_frame_2b, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = tax_period)
        self.txt_tax_period.grid(row=0,column=1)
        
        
        #------------------------------------------Tax Code-----------------------------------------------------------
        self.lbl_tax_code= Label(right_frame_2b, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Tax Code', bd=1, anchor='w', justify=LEFT)
        self.lbl_tax_code.grid(row=1,column=0, sticky =W)
        self.txt_tax_code= Entry(right_frame_2b, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = tax_code)
        self.txt_tax_code.grid(row=1,column=1)
        
         #------------------------------------------SS Number-----------------------------------------------------------
        self.lbl_ss_number= Label(right_frame_2b, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'SS Number', bd=1, anchor='w', justify=LEFT)
        self.lbl_ss_number.grid(row=2,column=0, sticky =W)
        self.txt_ss_number= Entry(right_frame_2b, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = ss_number)
        self.txt_ss_number.grid(row=2,column=1)
        
         #------------------------------------------SS Code-----------------------------------------------------------
        self.lbl_bi_code= Label(right_frame_2b, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'SS Code', bd=1, anchor='w', justify=LEFT)
        self.lbl_bi_code.grid(row=3,column=0, sticky =W)
        self.txt_bi_code= Entry(right_frame_2b, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = bi_code)
        self.txt_bi_code.grid(row=3,column=1)
        
        #------------------------------------------Taxable Pay-----------------------------------------------------------
        self.lbl_taxable_pay= Label(right_frame_2c, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Taxable Pay', bd=1, anchor='w', justify=LEFT)
        self.lbl_taxable_pay.grid(row=0,column=0, sticky =W)
        self.txt_taxable_pay= Entry(right_frame_2c, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=12, justify= 'left', textvariable = taxable_pay)
        self.txt_taxable_pay.grid(row=0,column=1)
        
        #------------------------------------------Pensionable Pay-----------------------------------------------------------
        self.lbl_pensionable_pay= Label(right_frame_2c, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Pensionable Pay', bd=1, anchor='w', justify=LEFT)
        self.lbl_pensionable_pay.grid(row=1,column=0, sticky =W)
        self.txt_pensionable_pay= Entry(right_frame_2c, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=12, justify= 'left', textvariable = pensionable_pay)
        self.txt_pensionable_pay.grid(row=1,column=1)
        
        #-------------------------------------------Net Pay-----------------------------------------------------------
        self.lbl_net_pay= Label(right_frame_2d, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Net Pay', bd=1, anchor='w', justify=LEFT)
        self.lbl_net_pay.grid(row=0,column=0, sticky =W)
        self.txt_net_pay= Entry(right_frame_2d, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = net_pay)
        self.txt_net_pay.grid(row=0,column=1) 
        
        #-------------------------------------------Gross Pay-----------------------------------------------------------
        self.lbl_gross_pay= Label(right_frame_2d, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Gross Pay', bd=1, anchor='w', justify=LEFT)
        self.lbl_gross_pay.grid(row=1,column=0, sticky =W)
        self.txt_gross_pay= Entry(right_frame_2d, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = gross_pay)
        self.txt_gross_pay.grid(row=1,column=1)   
        
        #-------------------------------------------Deductions-----------------------------------------------------------
        self.lbl_deductions= Label(right_frame_2d, font=('arial', 16, 'bold'), bg='#AAABE6',text = 'Deductions', bd=1, anchor='w', justify=LEFT)
        self.lbl_deductions.grid(row=2,column=0, sticky =W)
        self.txt_deductions= Entry(right_frame_2d, font=('arial', 16, 'normal'), highlightcolor='#AAABE6', highlightbackground='#AAABE6', bg='#f4f5f8',bd=1, width=17, justify= 'left', textvariable = deductions)
        self.txt_deductions.grid(row=2,column=1)  
        #======================================Buttons=============================================================
        self.btn_add_new_total= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Add New/Total', command=monthly_salary).grid(row=0, column=0, padx=1)
        
        self.btn_display= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Display', command=display_data).grid(row=0, column=2, padx=1)
        
        self.btn_update= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Update', command=update_data).grid(row=0, column=3, padx=1) 
        
        self.btn_delete= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Delete', command=delete_data).grid(row=0, column=4, padx=1)       

        self.btn_search= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Search', command=search_data).grid(row=0, column=5, padx=1)
        
        self.btn_Reset= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#FFFFFF', width=8, text = 'Reset', command=reset).grid(row=0, column=6, padx=1)  
        
        self.btn_Exit= Button(top_frame_1, bd=1, padx=24, pady=1, font=('arial', 16, 'bold'), fg='black', bg='#ffffff', width=8, text = 'Exit', command=exit_db_sys).grid(row=0, column=7, padx=1)
                 
if __name__ == '__main__': #main name of the system
    root = Tk()
    application = Employee(root)
    root.mainloop()







