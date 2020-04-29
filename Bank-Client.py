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
