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

    cr8 = Create8()
    


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

class Create8():
    def __init__(self):
        self.root = Tk(className = " Update Account Information ")
        self.root.geometry("600x800")
        self.root.config(bg = "#FDFBF2")
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
        self.lbACC = Label(self.root, text = "Account Number : ", font = "Courier 13 bold", fg = "navy")
        self.lbACC.place(x = 120, y = 500)
        self.lbAnsFName = Label(self.root, text = self.l[0], font = "Courier 13 bold", fg = "navy")
        self.lbAnsFName.place(x = 350, y = 100)
        self.lbAnsMName = Label(self.root, text = self.l[1], font = "Courier 13 bold", fg = "navy")
        self.lbAnsMName.place(x = 350, y = 140)
        
        self.entLName = Entry(self.root,bd=3)
        self.entLName.insert(0, self.l[2])
        self.entLName.place(x = 350, y = 180)
        self.entMobNo= Label(self.root, text = self.l[3], font = "Courier 13 bold", fg = "navy")
        self.entMobNo.place(x = 350, y = 220)
        self.entAdd = Entry(self.root,bd=3)
        self.entAdd.insert(0, self.l[4])
        self.entAdd.place(x = 350, y = 260)
        self.entDOB = Label(self.root, text = self.l[5], font = "Courier 13 bold", fg = "navy")
        self.entDOB.place(x = 350, y = 300)
        self.v = StringVar(self.root)
        self.entGend = Label(self.root, text = self.l[6], font = "Courier 13 bold", fg = "navy")
        self.entGend.place(x = 350, y = 340)
        self.entEmail = Label(self.root, text = self.l[7], font = "Courier 13 bold", fg = "navy")
        self.entEmail.place(x = 350, y = 380)
        self.v1 = StringVar(self.root)
        self.cbEmpStatus = ttk.Combobox(self.root, values = ["Labourer", "Farming/ Fishing","Retail trading","Business", "Engineer","Medical","Teaching","Civil Servant","Student"])
        self.cbEmpStatus.place(x = 350, y = 420)
        self.cbEmpStatus.current(0)
        self.lbCurrBal = Label(self.root, text = self.l[13], font = "Courier 13 bold", fg = "navy")
        self.lbCurrBal.place(x = 350, y = 460)
        
        self.lbANSAcc = Label(self.root, text = self.l[11], font = "Courier 13 bold", fg = "navy")
        self.lbANSAcc.place(x = 350, y = 500)
        
        self.btnSubmit = Button(self.root, text = "Update",command = self.updateInfo ,font = "Times 10 bold", border = 5, width = 15, bg='red2')
        self.btnSubmit.place(x = 250,y = 540)
        
    def updateInfo(self):
        self.query = "update bank_accounts set Last_Name = '%s', Address = '%s' , EmpStatus = '%s' where ACC_NO='%s'"%(self.entLName.get(), self.entAdd.get(), self.cbEmpStatus.get(), self.l[11])
        connection("PyBank", self.query)
        messagebox.showinfo("Information", "Details Updated...")
        

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
        
        self.prevPIN = simpledialog.askinteger("Informaion", "Ask previous PIN", show="*")
        query = "SELECT PASSWORD FROM bank_accounts where acc_no = '%s'"%(getval2.h)
        k = 0
        
        fileName = str(getval2.h) + ".log"
        
        self.cursor.execute(query)
        for i in self.cursor:
            k = i[0]

        if int(k) == int(self.prevPIN):
            self.askNEWPIN = simpledialog.askinteger("Information","Enter New PIN", show="*")
            self.askNEWPINCNF = simpledialog.askinteger("Information","Enter New PIN again", show="*")
            if int(self.askNEWPIN) == int(self.askNEWPINCNF):
                query = "UPDATE bank_accounts set Password = '%s' where acc_no = '%s'"%(self.askNEWPIN,getval2.h)
                self.cursor.execute(query)
                logs(fileName, "\nPIN REGENERATED --- " + str(datetime.datetime.today()))
                self.con.commit()
                messagebox.showinfo("Information","PIN Regenerated Successfully")
            else:
                logs(fileName, "\nTRYING PIN REGENERATION --- PASSWORD & CNFPASS NOT MATCH --- " + str(datetime.datetime.today()))
                messagebox.showerror("Information","Two Password fields does not match AND Only Numbers accepted!")
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
 
    
    os.chdir(directory)
    img = Image.open(fp)
    img = img.save(fileName)
    
    
    os.listdir()
    


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
        self.entPIN = Entry(self.root, bd = 3, show="*")
        self.entPIN.place(x = 320, y = 160)
        
        self.btnSubmit = Button(self.root, text = "Submit", command = self.passval, font = "Times 10 bold", border = 5, width = 15, bg='dodger blue')
        #self.btnSubmit.config(command = checkData)
        self.btnSubmit.place(x = 230,y = 210)
        
        self.lbFooter = Label(self.root, text = "Don't have account? Create new Account", font = "Helventica 10 bold italic")
        self.lbFooter.place(x = 170,y = 280)
        self.btn = Button(self.root, text = "Create Account", command = window1, bg='dodger blue', font = "Times 10 bold", border = 5, width = 15 )
        self.btn.place(x = 230,y = 320)
        
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
                self.sm = simpledialog.askinteger("PIN","Enter a new security PIN", parent = self.root, show="*")
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