# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:25:27 2020

@author: Het Suthar
"""

from tkinter import *
from tkinter import ttk
import shutil
import cv2
from PIL import Image, ImageTk
import pymysql
from tkinter import simpledialog
import datetime
import logging
import re
import tkinter.font as font
import time
import os
#logging.basicConfig(filename = 'hello.log',level = logging.DEBUG, format = '%(asctime)s:%(levelname)s:%(message)s')


def window1():
   
    b6 = Create6()
    


def window2():
    cr5 = Create5()

def window3():
    root = Tk(className = " Create Bank Account")
    root.geometry("512x512")
    Create8(root)
    mainloop()


def logs(fileName,msg):
    directory= r"C:/wamp64/www/Banking_System/Logs_Client"
    os.chdir(directory)
    with open(fileName, 'a') as f:
        f.write(msg)
    print("Log Updated")
 
def bankMoney(amt = 0, op=''):
    if amt>0 and op!='':
        try:
            con = pymysql.connect(host = "localhost", passwd = "", user = "root", database = "PyBank")
            cursor = con.cursor()
            query = "select Total_Amount from Pybank_details"
            cursor.execute(query)
            for i in cursor:
                data1 = float(i[0])
            data1 +=float(amt)
            data2 =data1 - float(amt)
            if op=='+':
                query = "update pybank_details set Total_amount = '%s'"%(str(data1))
                cursor.execute(query)
                con.commit()
                print("Bank Data Updated")
            elif op=='-':
                query = "update pybank_details set Total_amount = '%s'"%(str(data2))
                cursor.execute(query)
                con.commit()
                print("Bank data updated")
        except Exception as e:
            print(e)




def connection(db= None,query = None):
    try:
        con = pymysql.connect(host = "localhost", passwd = "", user = "root", database = db)
        cursor = con.cursor()
        if query !=None:

            cursor.execute(query)
                
            
        #for i in cursor:
         #   for j in i:
          #      BankData.append(j)
        #print(BankData)
        con.commit()
    except pymysql.DatabaseError as e:
        print(e)

class Create8(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack()
        self.create_widgets()
    
    def getData(self):
        self.con = pymysql.connect(host = "localhost", user = "root", passwd = "", database = "PyBank")
        self.cursor = self.con.cursor()
        self.l = []
        query = "SELECT * FROM bank_accounts WHERE ACC_NO = '%s'"%(getval2.h)
        self.cursor.execute(query)
        for i in self.cursor:
            for j in i:
                self.l.append(j)
        
                
    def create_widgets(self):
        self.getData()
        
        self.entACC = Label(self, text = self.l[11])
        #self.entACC.insert(0,self.l[12])
        self.entACC.pack()
        
        self.entFName = Label(self, text = self.l[0])
        #self.entFName.insert(0, self.l[0])
        self.entFName.pack()
        self.entMName = Label(self, text = self.l[1])
        #self.entMName.insert(0,self.l[1])
        self.entMName.pack()
        self.entLName = Label(self, text = self.l[2])
        #self.entLName.insert(0,self.l[2])
        self.entLName.pack()
        self.entMobNo = Entry(self)
        self.entMobNo.insert(0,self.l[3])
        self.entMobNo.pack()
        self.entAdd = Entry(self)
        self.entAdd.insert(0,self.l[4])
        self.entAdd.pack()
        self.entDOB = Label(self, text = self.l[5])
        #self.entDOB.insert(0,self.l[5])
        self.entDOB.pack()
        
        self.entGend = Label(self, text = self.l[6])
        #self.entGend.insert(0,self.l[6])
        self.entGend.pack()
        
        self.entEmail = Entry(self)
        self.entEmail.insert(0,self.l[7])
        self.entEmail.pack()
        self.v1 = StringVar(self)
        self.cbEmpStatus = ttk.Combobox(self, values = ["Labourer", "Farming/ Fishing","Retail trading","Business", "Engineer","Medical","Teaching","Civil Servant","Student"])
        
        self.cbEmpStatus.pack()
        self.cbEmpStatus.current(0)
        """
        self.imgAadhar = Image.open(self.l[9])
        self.imgAadhar.resize((100,100),Image.ANTIALIAS)
        self.imgAadharLabel = Label(self, image = ImageTk.PhotoImage(self.imgAadhar))
        self.imgAadharLabel.pack()
        
        self.imgPersonal = Image.open(self.l[10])
        self.imgPersonal.resize((100,100),Image.ANTIALIAS)
        self.imgPersonalLabel = Label(self, image = ImageTk.PhotoImage(self.imgPersonal))
        self.imgPersonalLabel.pack()
        
        """
        
        """
        
        self.img = Image.open(self.l[9])
        self.render = ImageTk.PhotoImage(self.img)
        self.another = PhotoImage(file = self.l[9])
        self.imgLabel = Label(self, image = self.another)
        self.imgLabel.pack()
        """
        
        """
        img = cv2.imread(self.l[9])
        img2 = ImageTk.PhotoImage(img)
        cv2.imshow("Image", img)
        self.lb = Label(self, image = img2)
        self.lb.pack()
        """
        #self.l[9] = self.l[9].replace("/","\")
        print(self.l[9])
        os.chdir("C:\wamp64\www\Banking_System\Aadhar_card")
        self.photo = PhotoImage(file = self.l[9])
        self.lb = Label(self, image = self.photo)
        self.lb.pack()
        
        self.lbCurrBal = Label(self, text = self.l[13])
        #self.lbCurrBal.config(text = self.l[13])
        self.lbCurrBal.pack()
        
        self.btnSubmit = Button(self, text = "Submit")
        self.btnSubmit.pack()
        
        



class Create5:
    def __init__(self):
        self.root = Tk(className = " Your Account Details")
        self.root.geometry("600x800")
        self.root.config(bg = "#FDFBF2")
        self.create_widgets()
    
    def create_widgets(self):
        
        self.lb = Label(self.root, text = "Account Number : ", font = "Times 20 bold", fg = "red2")
        self.lb.place(x = 150,y = 20)
        
        
        self.lbtry = Label(self.root, text = getval2.h, font = "Times 20 bold", fg = "red2")
        self.lbtry.place(x = 400,y = 20)
        
        self.btBalanceEnq = Button(self.root, text = "Check Balance", command = self.disContent(1), font = "Courier 12 bold", fg = "navy", width = 20)
        self.btBalanceEnq.place(x = 195,y = 100)
        self.btDebitAmount = Button(self.root, text = "Debit Amount", command = self.dbtAmount, font = "Courier 12 bold", fg = "navy", width = 20)
        self.btDebitAmount.place(x = 40,y = 180)
        self.btCreditAmoun = Button(self.root, text = "Credit Amount", command = self.credAmount, font = "Courier 12 bold", fg = "navy", width = 20)
        self.btCreditAmoun.place(x = 350,y = 180)
        self.btUpdateAccount = Button(self.root, text = "Update Account Info.", command = window3, font = "Courier 12 bold", fg = "navy", width = 20)
        self.btUpdateAccount.place(x = 40,y = 260)
        self.btChangePass = Button(self.root, text = "Regenerate PIN", command = self.regPIN, font = "Courier 12 bold", fg = "navy", width = 20)
        self.btChangePass.place(x = 350,y = 260)
        self.btTransMoney = Button(self.root, text = "Transfer Amount", command = self.transaction, font = "Courier 12 bold", fg = "navy", width = 20)
        self.btTransMoney.place(x = 40,y = 340)
        self.btnGenerateReport = Button(self.root, text = "Generate Report", font = "Courier 12 bold", fg = "navy", width = 20)
        self.btnGenerateReport.place(x = 350,y = 340)
        self.btnDelAcc = Button(self.root, text = "Delete Account", command = self.delaccount, font = "Courier 12 bold", fg = "navy", width = 20)
        self.btnDelAcc.place(x = 195, y = 420)
        #self.can = Canvas(self.root, width = 800, height=100, bg = '#afeeee')
        
        #self.text = self.can.create_text(100, 10, text = "Hello Canvas")
        
        #self.can.pack()
        #self.movement()
        ### TRY TO DRAW AN ATM HERE ###
        #self.canvas = Canvas(self, width = 500, height = 500)
        #self.canvas.create_rectangle(75,75,350,350)
        
        #self.canvas.pack()
    def delACC(self):
        self.entDelAcc = Entry(self.root, bd = 3)
        self.entDelAcc.place(x = 240, y = 450)
        self.btnDelAcc = Button(self.root,text = "Debit Amount", command = self.delaccount, font = "Courier 12 bold", fg = "navy", width = 15)
        self.btnDelAcc.place(x = 225, y = 490)
    
    def delaccount(self):
        query = "delete from bank_accounts where acc_no = '%s'"%(getval2.h)
        try:
            connection("PyBank",query)
            messagebox.showinfo("Information", "Account Deleted")
        except:
            messagebox.showinfo("Warning", "Account Not Deleted")
    
    def movement(self):
        self.can.move(self.text, -1,0)
        self.can.after(10, self.movement)
        
    def disContent(self,bt):
        self.con = pymysql.connect(host = "localhost", user = "root", password = "", database = "PyBank")
        self.cursor = self.con.cursor()
        query = "SELECT curr_bal from bank_accounts where acc_no = '%s'"%(getval2.h)
        
        
        self.lbShowData = Label(self.root)
        self.lbShowData.pack()
        """
        canvas = Canvas(self.root, width = 150, height = 10)
        canvas.place(x = 400,y = 90)
        line = canvas.create_line(1,5,10,5)
        xspeed = 5
        yspeed = 0
        while True:
            canvas.move(line, xspeed,yspeed)
            pos = canvas.coords(line)
            if  pos[2]>150:
                xspeed = 0
                break
            self.root.update()
            time.sleep(0.1)
        
        """
        
        self.cursor.execute(query)
        if bt == 1:
            for i in self.cursor:
                self.lbShowData.config(text = "Your Current Balance is : " + str(i[0]))
        elif bt == 2:
            for i in self.cursor:
                self.l = i[0]
            
    def dbtAmount(self):
        
        self.entDbtAmt = Entry(self.root, bd = 3)
        self.entDbtAmt.place(x = 240, y = 450)
        self.btnDbtAmt = Button(self.root,text = "Debit Amount", command = self.qwe, font = "Courier 12 bold", fg = "navy", width = 15)
        self.btnDbtAmt.place(x = 225, y = 490)
        
    
    def qwe(self):
        self.con = pymysql.connect(host = "localhost", user = "root", password = "", database = "PyBank")
        self.cursor = self.con.cursor()
        
        self.disContent(2)
        fileName = str(getval2.h) + ".log"
        amt = int(self.l) - int(self.entDbtAmt.get())
        
        query = "UPDATE bank_accounts set curr_bal = '%s' where acc_no = '%s'"%(amt, getval2.h)
        self.cursor.execute(query)
        logs(fileName, "\nAmount Debited : " + self.entDbtAmt.get() + " --- " + str(datetime.datetime.today()))
        self.con.commit()
        messagebox.showinfo("Information","Amount Debited Successfully")
        bankMoney(float(self.entDbtAmt.get()),'-')
        
    def credAmount(self):
        self.entCrdAmt= Entry(self.root, bd = 3)
        self.entCrdAmt.place(x = 240, y = 450)
        self.btnCred = Button(self.root, text = "Credit Amount",command = self.credAmtTrans, font = "Courier 12 bold", fg = "navy", width = 15)
        self.btnCred.place(x = 225, y = 490)
        
    def credAmtTrans(self):
        self.con = pymysql.connect(host = "localhost", user = "root", password = "", database = "PyBank")
        self.cursor = self.con.cursor()
        
        self.disContent(2)
        
        fileName = str(getval2.h) + ".log"
        
        amt = int(self.l) + int(self.entCrdAmt.get())
        if amt > 0:
            query = "UPDATE bank_accounts set curr_bal = '%s' where acc_no = '%s'"%(amt, getval2.h)
            self.cursor.execute(query)
            logs(fileName, "\nAmount CREDITED : " + self.entCrdAmt.get() + " --- " + str(datetime.datetime.today()))
            self.con.commit()
            messagebox.showinfo("Information","Amount credit successfully")
            bankMoney(float(self.entCrdAmt.get()),'+')
        else:
            logs(fileName ,"Tried CREDIT --- NOT SUFFICIENT BALANCE --- "  + str(datetime.datetime.today()))
            messagebox.showwarning("Information","Minimum Balance requirement is 500 Rs.")
            
    def regPIN(self):
        self.con = pymysql.connect(host = "localhost", user = "root", password = "", database = "PyBank")
        self.cursor = self.con.cursor()
        
        self.prevPIN = simpledialog.askinteger("Informaion", "Ask previous PIN")
        query = "SELECT PASSWORD FROM bank_accounts where acc_no = '%s'"%(getval2.h)
        k = 0
        
        fileName = str(getval2.h) + ".log"
        
        self.cursor.execute(query)
        for i in self.cursor:
            k = i[0]

        if int(k) == int(self.prevPIN):
            self.askNEWPIN = simpledialog.askinteger("Information","Enter New PIN")
            self.askNEWPINCNF = simpledialog.askinteger("Information","Enter New PIN again")
            if self.askNEWPIN == self.askNEWPINCNF:
                query = "UPDATE bank_accounts set Password = '%s' where acc_no = '%s'"%(self.askNEWPIN,getval2.h)
                self.cursor.execute(query)
                logs(fileName, "\nPIN REGENERATED --- " + str(datetime.datetime.today()))
                self.con.commit()
                messagebox.showinfo("Information","PIN Regenerated Successfully")
            else:
                logs(fileName, "\nTRYING PIN REGENERATION --- PASSWORD & CNFPASS NOT MATCH --- " + str(datetime.datetime.today()))
                messagebox.showerror("Information","Two Password fields does not match")
        else:
            logs(fileName, "\nTRIED PIN REGENERATION --- INVALID PREVIOUS PASSWORD --- "  + str(datetime.datetime.today()))
            messagebox.showerror("Information","Previous Password does not match")

    def transaction(self):
        try:
            self.askRECVACC = simpledialog.askinteger("Transaction","Enter the Account No:")
            self.con = pymysql.connect(host = "localhost", user = "root", password = "", database = "PyBank")
            self.cursor = self.con.cursor()
            try:
                self.query = "SELECT curr_bal FROM bank_accounts where ACC_NO='%s'"%(str(self.askRECVACC))
                self.cursor.execute(self.query)
                self.askTransAmount = simpledialog.askinteger("Amount","Enter Amount")
                for i in self.cursor:
                    self.a = i[0]
                
                
                self.disContent(2)
                if int(self.l) - self.askTransAmount > 100:
                    self.ans = int(self.l) - self.askTransAmount
                    self.ans2 = int(self.a) + int(self.askTransAmount)
                    self.cursor.execute("UPDATE bank_accounts set curr_bal = '%s' where ACC_NO='%s'"%(str(self.ans), getval2.h))
                    self.con.commit()
                    self.cursor.execute("UPDATE bank_accounts set curr_bal = '%s' where ACC_NO='%s'"%(str(self.ans2),str(self.askRECVACC)))
                    
                    self.con.commit()
                    print("done")    
                
            except Exception as e:
                #messagebox.showerror("Information","Could not find Bank Account")
                print(e)
            
        except:
            messagebox.showerror("connection","Can not connect to the served, Please Try again!")
            
            


def getval(h,f,g,choice):
    getval.f  = h
    getval.l = f
    getval.m = g
    getval.c = choice
    #print(getval.d)
    try1()


def getval2(a,b):
    getval2.h = a
    getval2.g = b
    checkData(getval2.h, getval2.g)
    
l= ["a","b"]

def try2():
    print(getval.d)

def try1():
    fp  = filedialog.askopenfilename( filetypes = (("JPG File",".jpg"),("PNG File",".png")))
    #print(fp)
#    l = []
    fp  = fp.replace("/",r"\\")
    #print(fp)
    
    con = pymysql.connect(host = "localhost", user = "root", password = "", database = "PyBank")
    cursor = con.cursor()
    query = "select Account_No from imp_values"
    cursor.execute(query)
    for i in cursor:
        a = i[0]
    
    fileName = a + ".jpg"
    
    
    #fileName = "" + getval.f + "" + getval.l + "" + getval.m + ".jpg"
    if getval.c == 0:
        directory= r"C:/wamp64/www/Banking_System/Aadhar_card/"
        l.insert(0,directory + fileName)
        print(l[0])
    elif getval.c == 1:
        directory= r"C:/wamp64/www/Banking_System/Personal_Photo/"
        l.insert(1,directory + fileName)
        print(l[1])
    print(fileName)
    """
    img = cv2.imread(fp)    
    cv2.imshow("Image",img)
    """
    #l = fp.split("/")
    #cv2.imwrite()
    #print(l[-1])
    
    os.chdir(directory)
    img = Image.open(fp)
    img = img.save(fileName)
    
    #shutil.copyfile(fp,path)
    os.listdir()
    
    
    #cv2.imwrite(fileName, img)
    """
    directory= r"C:/wamp64/www/Banking_System/Logs_Client"
    os.chdir(directory)
    fileName =a + ".log"
    
    with open(fileName, 'w') as f:
        f.write("Account Created On " + str(datetime.datetime.today())  + " --- ACCNO  = " + a)
    """
    
    #logging.basicConfig(filename = fileName)
    #logging.DEBUG("ACCOUNT CREATED ACCNO ")
    #logging.log(logging.DEBUG, "ACCOUNT CREATED", filename= fileName)



def checkData(accno,pin):
    count = 0
    try:
        con = pymysql.connect(host="localhost",user="root",passwd="", database="PyBank")
        cursor = con.cursor()
        cursor.execute("SELECT PASSWORD, ACC_NO FROM bank_accounts where ACC_NO = '%s'"%(accno))
        #global count
        
        fileName = str(accno) + ".log"
        for i in cursor:
            l = i[0]
        if str(l) == str(pin) and count < 2:
            
            logs(fileName, "\nAccount "+ accno +" --- logged  " + str(datetime.datetime.today()))
            window2()
        elif count > 2:
            window1()
        else:
            messagebox.showerror("Information","Password Does not match")                
            logs(fileName, "\nWrong Password Tried --- "  + str(datetime.datetime.today()))
            
            count = count + 1
            
            print(count)
    except Exception as e:
        print(e)

class Create7:
    def __init__(self):
        self.root = Tk(className = " Create New Bank Account")
        self.root.geometry("600x600")
        self.root.config(bg = "#FDFBF2")
        self.create_widgets()
        self.count = 0
        self.myFont = font.Font(family = 'Times', weight = 'bold')          
    def create_widgets(self):
        self.lbHeader = Label(self.root, text = "Login / Create New Account", font = "Times 30 bold",fg = "red2")
        #self.lbHeader.config(font = 30)
        self.lbHeader.place(x = 50, y = 20)
        
        ### Draw a rectangle over there and then show the buttons i.e. login form ###
        self.lbACCNODISP = Label(self.root, text = " Account No : ", font = "Courier 15 bold", fg = "navy")
        self.lbACCNODISP.place(x = 120,y = 120)
        self.entACCNO = Entry(self.root, bd = 3)
        self.entACCNO.place(x = 320, y = 120)
        self.lbPIN = Label(self.root, text = "        Pin : ", font = "Courier 15 bold", fg = "navy")
        self.lbPIN.place(x = 120, y= 160)
        self.entPIN = Entry(self.root, bd = 3)
        self.entPIN.place(x = 320, y = 160)
        
        self.btnSubmit = Button(self.root, text = "Submit", command = self.passval, font = "Times 10 bold", border = 5, width = 15, bg='dodger blue')
        #self.btnSubmit.config(command = checkData)
        self.btnSubmit.place(x = 230,y = 210)
        
        self.lbFooter = Label(self.root, text = "Don't have account? Create new Account", font = "Helventica 10 bold italic")
        self.lbFooter.place(x = 170,y = 280)
        self.btn = Button(self.root, text = "Create Account", command = window1, bg='dodger blue', font = "Times 10 bold", border = 5, width = 15 )
        self.btn.place(x = 230,y = 320)
        
    """
    def checkData(self):
        self.con = pymysql.connect(host="localhost",user="root",passwd="", database="PyBank")
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT PASSWORD, ACC_NO FROM bank_accounts where ACC_NO = '%s'"%(self.entACCNO.get()))
        
        for i in self.cursor:
            self.l = i[0]
        if str(self.l) == str(self.entPIN.get()) and self.count < 2:
            window2()
        else:
            messagebox.showerror("Information","Password Does not match")                
            window1()
            self.count = self.count + 1
            print(self.count)
    """
    def passval(self):
        a = self.entACCNO.get()
        b = self.entPIN.get()
        getval2(a,b)
        
    
    
class Create6:
    def __init__(self):
        self.root = Tk(className = " Create New Bank Account")
        self.root.config(bg = "#FDFBF2")
        self.root.geometry("600x700")
        self.create_widgets()
    def create_widgets(self):
        self.lbHead = Label(self.root,text = " Create New Account ", fg = "red2", font = "Times 30 bold")
        self.lbHead.place(x = 100,y = 20)
        self.lbFName  = Label(self.root, text = "First Name : ", font = "Courier 13 bold", fg = "navy")
        self.lbFName.place(x = 120, y = 100)
        self.lbMName = Label(self.root, text = "Middle Name : ", font = "Courier 13 bold", fg = "navy")
        self.lbMName.place(x = 120, y = 140)
        self.lbLName = Label(self.root, text = "Last Name : ", font = "Courier 13 bold", fg = "navy")
        self.lbLName.place(x = 120, y = 180)
        self.lbMobno = Label(self.root, text = "Mobile Number : ", font = "Courier 13 bold", fg = "navy")
        self.lbMobno.place(x = 120, y = 220)
        self.lbAdd = Label(self.root, text = "Address : ", font = "Courier 13 bold", fg = "navy")
        self.lbAdd.place(x = 120, y = 260)
        self.lbDOB = Label(self.root, text = "Date of Birth : ", font = "Courier 13 bold", fg = "navy")
        self.lbDOB.place(x = 120, y = 300)
        self.lbGender = Label(self.root, text = "Gender : ", font = "Courier 13 bold", fg = "navy")
        self.lbGender.place(x = 120, y = 340)
        self.lbEmail = Label(self.root, text = "Email Add. : ", font = "Courier 13 bold", fg = "navy")
        self.lbEmail.place(x = 120, y = 380)
        self.lbEmpStatus  = Label(self.root, text = "Employement Status : ", font = "Courier 13 bold", fg = "navy")
        self.lbEmpStatus.place(x = 120, y = 420)
        self.lbCurrBal1 = Label(self.root, text = "Current Balance : ", font = "Courier 13 bold", fg = "navy")
        self.lbCurrBal1.place(x = 120, y = 460)
        
        self.entFName = Entry(self.root, bd=3)
        self.entFName.place(x = 350, y = 100)
        self.entMName = Entry(self.root,bd=3)
        self.entMName.place(x = 350, y = 140)
        self.entLName = Entry(self.root,bd=3)
        self.entLName.place(x = 350, y = 180)
        self.entMobNo= Entry(self.root,bd=3)
        self.entMobNo.place(x = 350, y = 220)
        self.entAdd = Entry(self.root,bd=3)
        self.entAdd.place(x = 350, y = 260)
        self.entDOB = Entry(self.root,bd=3)
        self.entDOB.place(x = 350, y = 300)
        self.v = StringVar(self.root)
        self.rbg1 = Radiobutton(self.root, text = "Male", variable = self.v, value = "Male")
        self.rbg1.place(x = 350, y = 340)
        self.rbg2 = Radiobutton(self.root, text = "Female", variable = self.v, value = "Female")
        self.rbg2.place(x = 420, y = 340)
        self.entEmail = Entry(self.root,bd=3)
        self.entEmail.place(x = 350, y = 380)
        self.v1 = StringVar(self.root)
        self.cbEmpStatus = ttk.Combobox(self.root, values = ["Labourer", "Farming/ Fishing","Retail trading","Business", "Engineer","Medical","Teaching","Civil Servant","Student"])
        self.cbEmpStatus.place(x = 350, y = 420)
        self.cbEmpStatus.current(0)
        self.lbCurrBal = Entry(self.root, bd=3)
        self.lbCurrBal.place(x = 350, y = 460)
        
        self.btnAadharCard = Button(self.root, text = "Upload Aadhar Card",command  = self.take, font="Courier 12 bold", fg="white", activeforeground = "white",bg = "red2")
        #self.btnAadharCard.config(command = try1)
        self.btnAadharCard.place(x = 220, y = 500)
        self.btnPersonalPhoto = Button(self.root, text = "Upload Passpord Size Photo", command = self.take2, font="Courier 12 bold", fg="white", activeforeground = "white",bg = "red2")
        self.btnPersonalPhoto.place(x = 180, y = 550)
        #self.btnAadharCard.config(command = getval(self.entFName.get()))
        
        
        self.btnSubmit = Button(self.root, text = "Submit", command = self.submitData,width ="35", bg = "navy", fg = "white", activeforeground="navy", activebackground = "white", font = "Courier 14 bold")
        self.btnSubmit.place(x = 120, y = 600)
        
    def submitData(self):
        
        
        self.con = pymysql.connect(host="localhost",user="root",passwd="", database="PyBank")
        self.cursor = self.con.cursor()
        self.cursor.execute("select Account_No from imp_values")
        for i in self.cursor:
            self.ACC = int(i[0])
        
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        
        directory= r"C:/wamp64/www/Banking_System/Logs_Client"
        os.chdir(directory)
        fileName = str(self.ACC) + ".log"
    
        with open(fileName, 'w') as f:
             f.write("Account Created ---- " + str(datetime.datetime.today())  + " --- ACCNO  = " + str(self.ACC))
        
        
        
        if int(self.lbCurrBal.get())>500:
            if (re.search(regex, self.entEmail.get())):
                self.sm = simpledialog.askinteger("PIN","Enter a new security PIN", parent = self.root)
                query= "INSERT INTO bank_accounts VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.entFName.get(),\
                                                 self.entMName.get(),self.entLName.get(), self.entMobNo.get(), self.entAdd.get(),\
                                                 self.entDOB.get(), self.v.get(), self.entEmail.get(), self.cbEmpStatus.get(),l[0],l[1], self.ACC, self.sm, self.lbCurrBal.get())
                query2 ="INSERT INTO Log_Clients VALUES('%s','%s')"%(self.ACC, directory + fileName)
                connection("PyBank",query)
                connection("PyBank",query2)
                messagebox.showinfo("Information","Account Create Successfully!!")
                self.ACC = self.ACC + 2
                self.cursor.execute("UPDATE imp_values set Account_no = '%s'"%(self.ACC));
                self.con.commit()
                self.cursor.execute("select Account_Count from pybank_details")
                
                for i in self.cursor:
                    data = int(i[0])
                data = data + 1
                print("Data is : ",data)
                connection("PyBank","update pybank_details set Account_Count = '%s'"%(str(data)))
                bankMoney(float(self.lbCurrBal.get()),'+')
            else:
                messagebox.showwarning("Warning","Invalid Email Address")
        else:
            messagebox.showwarning("Information","Minimum balance should be 500 Rs.")
           
    def take(self):
        a = self.entFName.get()
        b = self.entLName.get()
        c = self.entMobNo.get()
        c = c[:5]
        #print(a)
        getval(a,b,c,0)
    
    def take2(self):
        a = self.entFName.get()
        b = self.entLName.get()
        c = self.entMobNo.get()
        c = c[:5]
        #print(a)
        getval(a,b,c,1)