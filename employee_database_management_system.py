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


if __name__ == '__main__': #main name of the system
    root = Tk()
    application = Employee(root)
    root.mainloop()














