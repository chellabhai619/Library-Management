from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from ReturnBook import *
mypass = "850222Ass"
mydatabase="mydatabase"

con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)
cur = con.cursor()
extractBid = "select bid from books"

cur.execute(extractBid)
con.commit()
for i in cur:
    allBid.append(i[0])
a=123
if a in allBid:
    print("TRUE")