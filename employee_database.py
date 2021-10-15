import sqlite3
#back_end

def employee_data():
    con = sqlite3.connect('employee.db') #connect the database called employee
    cur = con.cursor() #area within the memory will the variable con will add all the data
    cur.execute('CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY,reference text, first_name text,last_name text, address text,gender text, phone text,ni_number text,std_loan text,tax text,pension text,deductions text,net_pay text, gross_pay text)')
    con.commit()
    con.close()

#now, add all to the database
def add_employee_record(reference, first_name, last_name, gender, phone, ni_number, std_loan, tax, pension, deductions, net_pay, gross_pay):
    con = sqlite3.connect('employee.db')
    cur = con.cursor() 
    cur.execute('CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY,reference text, first_name text,last_name text, address text,gender text, phone text,ni_number text,std_loan text,tax text,pension text,deductions text,net_pay text, gross_pay text)')
    con.commit()
    con.close()
        
    
    