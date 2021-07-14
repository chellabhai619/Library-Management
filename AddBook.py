from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import pymysql

def searchBook():
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)
    y = 0.25
    sea=search1.get()

    Label(labelFrame, text="%-10s%-40s%-30s%-30s%-20s" % ('BID', 'Title', 'Author', 'Status','Rate'), bg='black', fg='white').place(
        relx=0.07, rely=0.1)
    Label(labelFrame, text="------------------------------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    seaBooks = "select * from "+ bookTable +" where bid= "+sea

    try:
        cur.execute(seaBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-30s%-30s%-30s%-20s" % (i[0], i[1], i[2], i[3], i[4]), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")


def search():
    global search1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root


    bookTable='books'
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="SEARCH BOOKS", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame, text="ENTER BOOK ID \n TO BE SEARCHED : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5)

    search1 = Entry(labelFrame)
    search1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(labelFrame, text="SUBMIT", bg='white', fg='black', width=10, height=2, command=searchBook)
    SubmitBtn.place(x=300, y=200)


def updatebook():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    rate=bookInfo5.get()

    updateBooks = "update " + bookTable + " set title='" + title + "', author='" + author + "', rate='" + rate + "'where bid ='"+bid+"'"

    try:
        cur.execute(updateBooks)
        con.commit()
        messagebox.showinfo('Success', "Book updated successfully")
    except:
        messagebox.showinfo("Error", "Can't update data into Database")



    root.destroy()


def update():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, bookInfo5, Canvas1, con, cur, bookTable, root

    bookTable="books"

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="UPDATE BOOKS", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="ENTER BOOK ID \n TO BE UPDATED : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.1)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(labelFrame, text="TITLE OF THE BOOK : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame, text="AUTHOR : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    lb5 = Label(labelFrame, text="RATE : ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.650, relheight=0.08)

    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3, rely=0.650, relwidth=0.62, relheight=0.08)

    SubmitBtnr = Button(labelFrame, text="OK", bg='white', fg='black', width=10, height=1, command=updatebook)
    SubmitBtnr.place(x=300, y=220)





def deleteBook():
    issueTable="books_issued"
    bid = bookInfo1.get()
    allBid=[]
    extractBid = "select bid from books"
    cur.execute(extractBid)
    con.commit()
    for i in cur:
        allBid.append(str(i[0]))

    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(str(i[0]))

        if bid in allBid:
            deleteSql = "delete from " + bookTable + " where bid = '" + bid + "'"
            deleteIssue = "delete from " + issueTable + " where bid = '" + bid + "'"
            try:
                cur.execute(deleteSql)
                con.commit()
                cur.execute(deleteIssue)
                con.commit()
                messagebox.showinfo('Success', "Book Record Deleted Successfully")
            except:
                messagebox.showinfo("Please check Book ID")
            print(bid)

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root



    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="DELETE BOOKS", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(labelFrame, text="SUBMIT", bg='white', fg='black', width=10, height=2, command=deleteBook)
    SubmitBtn.place(x=300, y=200)


def View():


    ids = []
    cur.execute("SELECT * FROM books")
    i = 0
    root = Tk()
    e = Label(root, width=10, text='BookID', borderwidth=1, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = Label(root, width=10, text='Title', borderwidth=1, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = Label(root, width=10, text='Author', borderwidth=1, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = Label(root, width=10, text='Status', borderwidth=1, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=3)
    e = Label(root, width=10, text='Rate', borderwidth=1, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=4)
    i = 1
    for name in cur:
        for j in range(len(name)):
            e = Entry(root, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, name[j])
        i = i + 1
    root.mainloop()


def bookRegister1():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    rate =bookInfo5.get()

    insertBooks = "insert into " + bookTable + " values('" + bid + "','" + title + "','" + author + "','available','" + rate + "')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")





def bookRegister():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4,bookInfo5, Canvas1, con, cur, bookTable, root



    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="ADD BOOKS", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="BOOK ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(labelFrame, text="TITLE OF THE BOOK : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame, text="AUTHOR : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)


    lb5 = Label(labelFrame, text="RATE : ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.65, relheight=0.08)

    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    SubmitBtnr = Button(labelFrame, text="OK", bg='white', fg='black', width=10, height=2, command=bookRegister1)
    SubmitBtnr.place(x=300, y=200)





def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("1000x500")

    # Add your own database name and password here to reflect in the code
    mypass = "850222Ass"
    mydatabase = "db"
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)

    '''mydatabase = "mydatabase"
    con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)
    cur = con.cursor()'''

    # Enter Table Names here
    bookTable = "books"  # Book Table

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="BOOKS", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    # Submit Button
    SubmitBtn = Button(root, text="ADD", bg='white', fg='black', width=10, height=2, command=bookRegister)
    # SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    SubmitBtn.place(x=20, y=150)

    SubmitBtn1 = Button(root, text="DELETE", bg='white', fg='black', width=10, height=2, command=delete)
    # SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    SubmitBtn1.place(x=20, y=200)

    SubmitBtn1 = Button(root, text="SEARCH", bg='white', fg='black', width=10, height=2, command=search)
    # SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    SubmitBtn1.place(x=20, y=250)

    SubmitBtn1 = Button(root, text="UPDATE", bg='white', fg='black', width=10, height=2, command=update)
    # SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    SubmitBtn1.place(x=20, y=300)

    SubmitBtn2 = Button(root, text="VIEW", bg='white', fg='black', width=10, height=2, command=View)
    # SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    SubmitBtn2.place(x=20, y=350)

    quitBtn = Button(root, text="Quit", bg='white', fg='black', width=10, height=2, command=root.destroy)
    quitBtn.place(x=450, y=430)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)


    root.mainloop()
