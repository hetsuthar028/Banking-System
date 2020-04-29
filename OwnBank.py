# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:44:08 2020

@author: Het Suthar
"""

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import pymysql
from tkinter import simpledialog
from datetime import date
#import OwnBank_Client as ck
import tkinter.font as font
import re

root = Tk(className = " Main Window")

root.geometry("1360x600")

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

"""SET FOCUS FOR ALL THE CHILD WINDOWS"""    
root.after(1, lambda: root.focus_force())
app = Frame(root)
app.pack()

BankData = []
 
ID = 18012021000

def update_progress_bar():
    x = barVar.get()
    if x < 100:
        barVar.set(x+10)
        mainWindow.after(500, update_progress_bar)
    else:
        print("Complete")


""" Function used for establishing connection with
database and to pass the query and execute 
in on particular database"""
def connection(db= None,query = None):
    try:
        con = pymysql.connect(host = "localhost", passwd = "", user = "root", database = db)
        cursor = con.cursor()
        if query !=None:
            cursor.execute(query)
        con.commit()
    except pymysql.DatabaseError as e:
        print(e)

""" Class used to create PyBank Details """
class Create1:
    def __init__(self):
        self.root = Tk(className = " PyBank Details")
        self.root.geometry("1024x1024")
        self.root.config(bg = "#FDFBF2")
        self.create_widgets()
    
    def create_widgets(self):
        con = pymysql.connect(host = "localhost", passwd = "", user = "root", database = "PyBank")
        cursor = con.cursor()
        query = "select * from pybank_details"
        cursor.execute(query)
        Bankdata = []
        for i in cursor:
            for j in i:
                BankData.append(j)
        con.commit()
        con.close()
        ### Button to check for Bank Details ###        
        self.b1 = Button(self.root, text ="Bank Details", command = self.showData, bg = 'red2', activebackground = 'blue', activeforeground = 'white', border = 5, width = 15, font = "Courier 15 bold", relief = RAISED)
        self.b1.place(x = 150, y = 20)
        ### Button to check the Employee Details ###
        self.b2 = Button(self.root, text ="Employee Details", command = connection("PyBank"), bg = 'red2', activebackground = 'blue', activeforeground = 'white', border = 5, width = 18, font = "Courier 15 bold", relief = RAISED)
        self.b2.config(command = self.show123)
        self.b2.place(x = 765, y = 20)
    
    ### Method for Showing the Treeview and other features when clicked on Employee Details button ###  
    def show123(self):
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        
        self.tw = ttk.Treeview(self.root, style ="mystyle.Treeview")
        self.tw["columns"] = (2,3,4,5,6,7,8,9,10)
        
        self.tw.column("#0s", width=70, minwidth=50, stretch=YES)
        self.tw.heading("#0s", text = "Name")
        self.tw.column(2, width=70, minwidth=50, stretch=NO)
        self.tw.heading(2, text = "PNO")
        self.tw.column(3, width=70, minwidth=50, stretch=NO)
        self.tw.heading(3, text = "ACCNO")
        self.tw.column(4, width=70, minwidth=50, stretch=NO)
        self.tw.heading(4, text = "ADD")
        self.tw.column(5, width=70, minwidth=50, stretch=NO)
        self.tw.heading(5, text = "Email")
        self.tw.column(6, width=70, minwidth=50, stretch=NO)
        self.tw.heading(6, text = "Sal")
        self.tw.column(7, width=70, minwidth=50, stretch=NO)
        self.tw.heading(7, text = "Post")
        self.tw.column(8, width=70, minwidth=50, stretch=NO)
        self.tw.heading(8, text = "WH")
        self.tw.column(9, width=70, minwidth=50, stretch=NO)
        self.tw.heading(9, text = "Exp")
        self.tw.column(10, width=70, minwidth=50, stretch=NO)
        self.tw.heading(10, text = "ID")
        
        self.tw.place(x = 530, y = 150)
        
        self.query = "SELECT * from `employee`"     
        self.con = pymysql.connect(host="localhost", user = "root", passwd ="", database = "PyBank")
        self.cursor = self.con.cursor()
        self.cursor.execute(self.query)
        j=0
        
        ### Inserting one by one data into Treeview fetched from Database ###
        for i in self.cursor:            
            self.tw.insert('',j,text = i[0], values = (i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))            
            j = j + 1
        
        """ Below that add Two Button to Create an Entry into the
        list or to delete a particular employee from the Bank """
        self.btAddEmployee = Button(self.root, text  = " Add Employee ", command = connection("PyBank"), font = "Courier 12 bold", bg = 'navy blue', fg = 'white', activebackground = 'red', activeforeground='white')
        self.btAddEmployee.config(command = window4)
        self.btAddEmployee.place(x = 720, y= 400)
        
        self.btDeleteEmployee = Button(self.root, text  = "Remove Employee ", command = connection("PyBank"), font = "Courier 12 bold", bg = 'navy blue', fg = 'white', activebackground = 'red', activeforeground='white')
        self.btDeleteEmployee.config(command = self.show1212)
        self.btDeleteEmployee.place(x = 890, y= 400)
    
    ### Method for Deleting an Employee from Bank ###
    def show1212(self):
        self.ID = simpledialog.askinteger("Information", "Enter Employee ID : ", parent = self.root)
        self.removeEmp()
    
    ### Method for Deleting an Employee from Bank ###
    def removeEmp(self):
        answer = simpledialog.askstring("Input", "Enter Valid Reason?",parent=self.root)
        date1 = date.today()
        if answer != "" and answer != None and answer != "0" and answer != " " and "None" not in answer and type(answer)!=None:
            print("Your Reason is :", answer)
            print(type(answer))
            query = "delete from employee where ID = '%s'"%(self.ID)
            connection("PyBank",query)
            
            query = "insert into Emp_Leave_Reason values('%s','%s','%s')"%(self.ID, answer, date1)
            connection("PyBank",query)
            
            query = "select Employee_Count from Pybank_details"
            self.cursor.execute(query)
            
            ### Decreasing Employee count when an employee is removed from the bank ###
            for i in self.cursor:
                data3 = int(i[0])
            data3 -=1
            connection("PyBank","update Pybank_details set Employee_Count = '%s'"%(data3))
        else:
            messagebox.showinfo("Warning", "Please enter valid reason to leave.")
            
    ### Displaying Bank Details using labels ###
    def showData(self):
        self.labelBankName = Label(self.root, text = "Bank Name : " + BankData[0] + " ",fg = 'navy', font = "Courier 17 bold")
        self.labelBankName.place(x = 50, y= 100)
        self.estabYear = Label(self.root, text = "Establishment Year : " + BankData[1] + " ",fg = 'navy', font = "Courier 17 bold")
        self.estabYear.place(x = 50, y= 140)
        self.founder = Label(self.root, text = "Founder : " + BankData[2] + " ",fg = 'navy', font = "Courier 17 bold")
        self.founder.place(x = 50, y= 180)
        self.ceo = Label(self.root, text = "CEO : " + BankData[3] + " ",fg = 'navy', font = "Courier 17 bold")
        self.ceo.place(x = 50, y= 220)
        self.empCount = Label(self.root, text = "Employee Count : " + str(BankData[4]) + " ",fg = 'navy', font = "Courier 17 bold")
        self.empCount.place(x = 50, y= 260)
        self.accCount = Label(self.root, text = "Account Count : " + str(BankData[5]) + " ",fg = 'navy', font = "Courier 17 bold")
        self.accCount.place(x = 50, y= 300)
        self.totalAmount = Label(self.root, text = "Total Amount : " + str(BankData[6]) + " ",fg = 'navy', font = "Courier 17 bold")
        self.totalAmount.place(x = 50, y= 340)
        self.logFile = Label(self.root, text = "Log File: " + BankData[7] + " ",fg = 'navy', font = "Courier 17 bold")
        self.logFile.place(x = 50, y= 380)
            
        
"""
Window is created for Adding a New Employee
to the bank.
This is invoked when Add Employee button in clicked...
"""
class Create3:
    def __init__(self):
        self.root = Tk(className = " Add Employee")
        self.root.config(bg = "#FDFBF2")
        self.root.geometry("600x600")
        self.create_widgets()
        
    def create_widgets(self):
        self.lbHead = Label(self.root, text = "Add Employee Details", font = "Times 30 bold", fg = 'red2')
        self.lbHead.place(x = 100, y = 20)
        
        self.lbName = Label(self.root, text = " Name : ", font = "Courier 15 bold", fg = "navy")
        self.lbName.place(x = 120, y = 120)
        self.lbPNO = Label(self.root, text = " Phone Number : ", font = "Courier 15 bold", fg = "navy")
        self.lbPNO.place(x = 120, y = 160)
        self.lbACCNO = Label(self.root, text = " Account No : ", font = "Courier 15 bold", fg = "navy")
        self.lbACCNO.place(x = 120, y = 200)
        self.lbADD = Label(self.root, text = " Address : ", font = "Courier 15 bold", fg = "navy")
        self.lbADD.place(x = 120, y = 240)
        self.lbEmail = Label(self.root, text = " Email Add. : ", font = "Courier 15 bold", fg = "navy")
        self.lbEmail.place(x = 120, y = 280)
        self.lbSal = Label(self.root, text = " Salary : ", font = "Courier 15 bold", fg = "navy")
        self.lbSal.place(x = 120, y = 320)
        self.lbPost = Label(self.root, text = " Post : ", font = "Courier 15 bold", fg = "navy")
        self.lbPost.place(x = 120, y = 360)
        self.lbWH = Label(self.root, text = " Working Hours : ", font = "Courier 15 bold", fg = "navy")
        self.lbWH.place(x = 120, y = 400)
        self.lbExp = Label(self.root, text = " Experience : ", font = "Courier 15 bold", fg = "navy")
        self.lbExp.place(x = 120, y = 440)
                
        self.entName  = Entry(self.root,bd = 3)
        self.entName.place(x = 350, y = 120)
        self.entPNO  = Entry(self.root,bd = 3)
        self.entPNO.place(x = 350, y = 160)
        self.entACCNO  = Entry(self.root,bd = 3)
        self.entACCNO.place(x = 350, y = 200)
        self.entADD  = Entry(self.root,bd = 3)
        self.entADD.place(x = 350, y = 240)
        self.entEmail  = Entry(self.root,bd = 3)
        self.entEmail.place(x = 350, y = 280)
        self.entSal  = Entry(self.root,bd = 3)
        self.entSal.place(x = 350, y = 320)
        self.entPost  = Entry(self.root,bd = 3)
        self.entPost.place(x = 350, y = 360)
        self.entWH  = Entry(self.root,bd = 3)
        self.entWH.place(x = 350, y = 400)
        self.entExp  = Entry(self.root,bd = 3)
        self.entExp.place(x = 350, y = 440)
        
        self.btn = Button(self.root, command = self.insertData, text = "Submit")
        self.btn.place(x = 250,y = 500)
        
    ### Method use for fetching data from widgets, validating and then storing to database ###
    def insertData(self):
        print(self.entName.get())
        print(self.entPNO.get())
        print(self.entACCNO.get())
        print(self.entADD.get())
        print(self.entEmail.get())
        print(self.entSal.get())
        print(self.entPost.get())
        print(self.entWH.get())
        print(self.entExp.get())
        if(re.search(regex, self.entEmail.get())):
            if(len(self.entPNO.get()) == 10):
                self.con = pymysql.connect(host="localhost",user="root",passwd="", database="PyBank")
                self.cursor = self.con.cursor()
                self.cursor.execute("select Employee_ID from imp_values")
                for i in self.cursor:
                    self.ID = int(i[0])
                
                print("FROM TABLE",self.ID)
                
                query = "insert into employee values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.entName.get(), self.entPNO.get(), self.entACCNO.get(), self.entADD.get(), self.entEmail.get(), self.entSal.get(), self.entPost.get(), self.entWH.get(), self.entExp.get(), self.ID)
                
                self.ID1 = str(self.ID + 1)
                connection("PyBank",query)
                query = "update imp_values set Employee_ID='%s' where Employee_ID='%s'"%(self.ID1,self.ID)
                connection("PyBank",query)
                query = "select Employee_Count from Pybank_details"
                self.cursor.execute(query)
                
                ### Incrementing Employee Counts in database ###
                for i in self.cursor:
                    data3 = int(i[0])
                data3 +=1
                connection("PyBank","update Pybank_details set Employee_Count = '%s'"%(data3))
                messagebox.showinfo("Informatiom","Employee Added Successfully!!")
            else:
                messagebox.showinfo("Warning", "Invalid Phone Number")
        else:
            messagebox.showinfo("Warning", "Invalid Email Address")

        
def window1():
    cr1 = Create1()
        
def window2():    
    cr7 = ck.Create7()
        
def window4():
    cr3 = Create3()
    

img4 = Image.open("C:\\Users\\Het Suthar\\Downloads\\text.gif")
img44 = ImageTk.PhotoImage(img4)
labelHeading = Label(app, image = img44)
labelHeading.image = img44
labelHeading.pack(pady = 10)

img = Image.open("C:\\Users\\Het Suthar\\Downloads\\LOGO3-removebg-preview.png")
render = ImageTk.PhotoImage(img)

l1 =Label(app, image = render)
l1.image = render
l1.pack()

pg = ttk.Progressbar(app, mode='determinate', maximum=50)
pg.start()
pg.step(5)

pg.pack()

myFont = font.Font(family = 'Times', weight = 'bold')

staffButton = Button(app, text = "Staff", command = window1, border = 5, activebackground='black', bg='red2', width=10, activeforeground = 'white', font=myFont)
staffButton.pack(side = LEFT)

clientButton = Button(app, text = "Client", command = window2, border = 5, activebackground='black', bg='red2', width = 10, activeforeground='white', font = myFont)
clientButton.pack(side = RIGHT)

mainloop()

