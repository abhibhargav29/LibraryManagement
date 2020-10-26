from tkinter import Tk,Label,Frame,Canvas,Button,Toplevel,Entry,StringVar,ttk
import pymysql as sql
from PIL import Image,ImageTk 
from tkinter import messagebox
from datetime import datetime

#*******************************************************************************************************************************
#For adding book

def registerBook(con, BookId, BookName, BookAuthor):
    cur = con.cursor()
    status = "A"
    query = f"INSERT INTO books VALUES('{BookId.get()}','{BookName.get()}','{BookAuthor.get()}','{status}')"
    try:
        cur.execute(query)
        con.commit()
        messagebox.showinfo("Sucess","Book Added Sucessfully")
    except(sql.err.IntegrityError):
        messagebox.showinfo("Failed","Book Id can not be null or duplicated")
    except(sql.err.DataError):
        messagebox.showinfo("Failed","Please enter attributes within limits")
    except Exception:
        messagebox.showinfo("Failed","Something went wrong")
    addWindow.destroy()

def addBook(con):
    global addWindow

    #GUI window
    addWindow = Toplevel()

    #Window basics 
    addWindow.title("Add Book")
    addWindow.geometry("600x600")
    addWindow.configure(bg="white")     

    #Background
    bgImg = Image.open("lib.png")

    bgHeight,bgWidth = bgImg.size 
    bgHeight = int(bgHeight/7.16); bgWidth = int(bgWidth/7.72)
    bgImg = bgImg.resize((bgWidth,bgHeight),Image.ANTIALIAS)

    Img = ImageTk.PhotoImage(bgImg)
    Background = Canvas(addWindow)
    Background.create_image(300,340,image=Img)
    Background.configure(bg="white",width=bgWidth,height=bgHeight)
    Background.pack(expand=True)
    
    #Heading
    headingFrame = Frame(addWindow,bg="grey",bd=5)
    headingFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame, text="Add Book", bg='black', fg='white', font=('Cailibri',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    #Labels
    labelFrame = Frame(addWindow, bg="black")
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.3)
    
    idLabel = Label(labelFrame, bg="black", fg="white", text="Book Id:", anchor="w", font=("Calibri",13))
    idLabel.place(relx=0.01,rely=0.1,relwidth=0.3,relheight=0.12)

    nameLabel = Label(labelFrame, bg="black", fg="white", text="Book Title:", anchor="w", font=("Calibri",13))
    nameLabel.place(relx=0.01,rely=0.45,relwidth=0.3,relheight=0.12)
    
    authorLabel = Label(labelFrame, bg="black", fg="white", text="Book Author:", anchor="w", font=("Calibri",13))
    authorLabel.place(relx=0.01,rely=0.80,relwidth=0.3,relheight=0.12)

    
    #Info Variables
    BookId = StringVar()
    BookName = StringVar()
    BookAuthor = StringVar()

    #Input Feilds
    idEntry = Entry(labelFrame, textvariable=BookId, font=("Calibri",13))
    idEntry.place(relx=0.32,rely=0.1,relwidth=0.6,relheight=0.12)
    
    nameEntry = Entry(labelFrame, textvariable=BookName, font=("Calibri",13))
    nameEntry.place(relx=0.32,rely=0.45,relwidth=0.6,relheight=0.12)
    
    authorEntry = Entry(labelFrame, textvariable=BookAuthor, font=("Calibri",13))
    authorEntry.place(relx=0.32,rely=0.80,relwidth=0.6,relheight=0.12)

    #Buttons
    Submitbtn = Button(addWindow, text="Submit", command=lambda: registerBook(con,BookId,BookName,BookAuthor))
    Submitbtn.configure(font=("Calibri",14), bg='white', fg='black')
    Submitbtn.place(relx=0.300, rely=0.9, relwidth=0.20,relheight=0.08)
    
    Exitbtn = Button(addWindow, text="Cancel", font=("Calibri",14), bg='white', fg='black', command=addWindow.destroy)
    Exitbtn.place(relx=0.500, rely=0.9, relwidth=0.20,relheight=0.08)

    #main loop
    addWindow.mainloop()


#*******************************************************************************************************************************
#For deleting book

def deleteRecord(con,bookid):
    cur = con.cursor()
    query1 = f"DELETE FROM issued_books WHERE book_id = '{bookid.get()}'"
    query2 = f"DELETE FROM books WHERE book_id ='{bookid.get()}'"
    try:
        cur.execute(query1)
        con.commit()
        cur.execute(query2)
        con.commit()
        messagebox.showinfo("Success","Delete Complete")
    except:
        messagebox.showinfo("Failed","Something went wrong")
    deleteWindow.destroy()

def deleteBook(con):
    global deleteWindow

    #GUI window
    deleteWindow = Toplevel()

    #Window basics 
    deleteWindow.title("Delete Book")
    deleteWindow.geometry("600x600")
    deleteWindow.configure(bg="white")     

    #Background
    bgImg = Image.open("lib.png")

    bgHeight,bgWidth = bgImg.size 
    bgHeight = int(bgHeight/7.16); bgWidth = int(bgWidth/7.72)
    bgImg = bgImg.resize((bgWidth,bgHeight),Image.ANTIALIAS)

    Img = ImageTk.PhotoImage(bgImg)
    Background = Canvas(deleteWindow)
    Background.create_image(300,340,image=Img)
    Background.configure(bg="white",width=bgWidth,height=bgHeight)
    Background.pack(expand=True)
    
    #Heading
    headingFrame = Frame(deleteWindow,bg="grey",bd=5)
    headingFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame, text="Delete Book", bg='black', fg='white', font=('Cailibri',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    #Labels
    labelFrame = Frame(deleteWindow, bg="black")
    labelFrame.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.2)
    
    idLabel = Label(labelFrame, bg="black", fg="white", text="Book Id:", anchor="w", font=("Calibri",15))
    idLabel.place(relx=0.01,rely=0.45,relwidth=0.3,relheight=0.2)
    
    #Info Variables
    BookId = StringVar()

    #Input Feilds
    idEntry = Entry(labelFrame, textvariable=BookId, font=("Calibri",15))
    idEntry.place(relx=0.32,rely=0.45,relwidth=0.6,relheight=0.2)

    #Buttons
    Submitbtn = Button(deleteWindow, text="Submit", command=lambda: deleteRecord(con,BookId))
    Submitbtn.configure(font=("Calibri",14), bg='white', fg='black')
    Submitbtn.place(relx=0.300, rely=0.9, relwidth=0.20,relheight=0.08)
    
    Exitbtn = Button(deleteWindow, text="Cancel", font=("Calibri",14), bg='white', fg='black', command=deleteWindow.destroy)
    Exitbtn.place(relx=0.500, rely=0.9, relwidth=0.20,relheight=0.08)

    #main loop
    deleteWindow.mainloop()


#*******************************************************************************************************************************
#For Viewing List

def deleteAll(con):
    confirmation = messagebox.askquestion("Delete All","Are you sure you want to delete all records?")
    if(confirmation=="yes"):
        query1 = "DELETE FROM issued_books"
        query2 = "DELETE FROM books"
        try:
            cur = con.cursor()
            cur.execute(query1)
            con.commit()
            cur.execute(query2)
            con.commit()
            messagebox.showinfo("Success","All records deleted")
            viewWindow.destroy()
        except:
            messagebox.showinfo("Failed","Something went wrong")
    else:
        pass

def ShowList(con):
    global viewWindow

    #GUI window
    viewWindow = Toplevel()

    #Window basics 
    viewWindow.title("View Books")
    viewWindow.geometry("600x600")
    viewWindow.configure(bg="white")     

    #Background
    bgImg = Image.open("lib.png")

    bgHeight,bgWidth = bgImg.size 
    bgHeight = int(bgHeight/7.16); bgWidth = int(bgWidth/7.72)
    bgImg = bgImg.resize((bgWidth,bgHeight),Image.ANTIALIAS)

    Img = ImageTk.PhotoImage(bgImg)
    Background = Canvas(viewWindow)
    Background.create_image(300,340,image=Img)
    Background.configure(bg="white",width=bgWidth,height=bgHeight)
    Background.pack(expand=True)
    
    #Heading
    headingFrame = Frame(viewWindow,bg="grey",bd=5)
    headingFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame, text="View Books", bg='black', fg='white', font=('Cailibri',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    #Book Tree
    TreeFrame = ttk.Treeview(viewWindow, columns=(1,2,3,4), show="headings")
    TreeFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    TreeFrame.column(1, width = 4) 
    TreeFrame.column(2, width = 75) 
    TreeFrame.column(3, width = 50)
    TreeFrame.column(4, width = 1) 
    TreeFrame.heading(1, text="BookId")
    TreeFrame.heading(2, text="Title")
    TreeFrame.heading(3, text="Author")
    TreeFrame.heading(4, text="Status")

    #Buttons
    Deletebtn = Button(viewWindow, text="Delete All", command=lambda: deleteAll(con))
    Deletebtn.configure(font=("Calibri",14), bg='white', fg='black')
    Deletebtn.place(relx=0.300, rely=0.9, relwidth=0.20,relheight=0.08)
    
    Exitbtn = Button(viewWindow, text="Cancel", font=("Calibri",14), bg='white', fg='black', command=viewWindow.destroy)
    Exitbtn.place(relx=0.500, rely=0.9, relwidth=0.20,relheight=0.08)

    #Main Text
    query1 = "SELECT * FROM books"
    try:
        cur=con.cursor() 
        cur.execute(query1)
        rows = cur.fetchall()
        for row in rows:
            TreeFrame.insert("","end",values=row)
    except:
        messagebox.showinfo("Failed","Unable to fetch book details")
        viewWindow.destroy()
        return
    
    #main loop
    viewWindow.mainloop()


#*******************************************************************************************************************************
#For issuing book

def registerIssue(con,bookid,studentid):
    cur = con.cursor()
    now = datetime.now().date()
    date = str(now)
    query1 = f"INSERT INTO issued_books VALUES('{bookid.get()}','{studentid.get()}','{date}')"
    query2 = f"UPDATE books SET status='NA' WHERE book_id = '{bookid.get()}'"
    try:
        cur.execute(query1)
        con.commit()
        cur.execute(query2)
        con.commit()
        messagebox.showinfo("Success","Book Issued")
    except sql.err.IntegrityError:
        messagebox.showinfo("Failed","Enter an available bookid")
    except sql.err.DataError:
        messagebox.showinfo("Failed","Enter valid bookid and studentid")
    except:
        messagebox.showinfo("Failed","Something went wrong")
    issueWindow.destroy()

def issueBook(con):
    global issueWindow

    #GUI window
    issueWindow = Toplevel()

    #Window basics 
    issueWindow.title("Issue Book")
    issueWindow.geometry("600x600")
    issueWindow.configure(bg="white")     

    #Background
    bgImg = Image.open("lib.png")

    bgHeight,bgWidth = bgImg.size 
    bgHeight = int(bgHeight/7.16); bgWidth = int(bgWidth/7.72)
    bgImg = bgImg.resize((bgWidth,bgHeight),Image.ANTIALIAS)

    Img = ImageTk.PhotoImage(bgImg)
    Background = Canvas(issueWindow)
    Background.create_image(300,340,image=Img)
    Background.configure(bg="white",width=bgWidth,height=bgHeight)
    Background.pack(expand=True)
    
    #Heading
    headingFrame = Frame(issueWindow,bg="grey",bd=5)
    headingFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame, text="Issue Book", bg='black', fg='white', font=('Cailibri',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    #Labels
    labelFrame = Frame(issueWindow, bg="black")
    labelFrame.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.2)
    
    idLabel = Label(labelFrame, bg="black", fg="white", text="Book Id:", anchor="w", font=("Calibri",15))
    idLabel.place(relx=0.01,rely=0.25,relwidth=0.3,relheight=0.2)

    sidLabel = Label(labelFrame, bg="black", fg="white", text="Student Id:", anchor="w", font=("Calibri",15))
    sidLabel.place(relx=0.01,rely=0.65,relwidth=0.3,relheight=0.2)
    
    #Info Variables
    BookId = StringVar()
    StudentId = StringVar()

    #Input Feilds
    idEntry = Entry(labelFrame, textvariable=BookId, font=("Calibri",15))
    idEntry.place(relx=0.32,rely=0.25,relwidth=0.6,relheight=0.2)

    sidEntry = Entry(labelFrame, textvariable=StudentId, font=("Calibri",15))
    sidEntry.place(relx=0.32,rely=0.65,relwidth=0.6,relheight=0.2)

    #Buttons
    Submitbtn = Button(issueWindow, text="Issue", command=lambda: registerIssue(con,BookId,StudentId))
    Submitbtn.configure(font=("Calibri",14), bg='white', fg='black')
    Submitbtn.place(relx=0.300, rely=0.9, relwidth=0.20,relheight=0.08)
    
    Exitbtn = Button(issueWindow, text="Cancel", font=("Calibri",14), bg='white', fg='black', command=issueWindow.destroy)
    Exitbtn.place(relx=0.500, rely=0.9, relwidth=0.20,relheight=0.08)

    #main loop
    issueWindow.mainloop()


#*******************************************************************************************************************************
#For returning book

def deleteIssue(con,bookid):
    cur = con.cursor()
    try:
        query0 = f"SELECT CURDATE()-issue_date FROM issued_books WHERE book_id='{bookid.get()}'"
        cur.execute(query0)
        days = cur.fetchall()
        fine=0
        if(int(days[0][0])>15):
            fine+= (int(days[0][0])-15)*2
        else:
            fine=0
    except:
        fine=0
    query1 = f"DELETE FROM issued_books WHERE book_id = '{bookid.get()}'"
    query2 = f"UPDATE books SET status='A' WHERE book_id = '{bookid.get()}'"
    try:
        cur.execute(query1)
        con.commit()
        cur.execute(query2)
        con.commit()
        messagebox.showinfo("Success",f"Book Returned, Fine Amount:{fine}")
    except:
        messagebox.showinfo("Failed","Something went wrong")
    returnWindow.destroy()

def returnBook(con):
    global returnWindow

    #GUI window
    returnWindow = Toplevel()

    #Window basics 
    returnWindow.title("Return Book")
    returnWindow.geometry("600x600")
    returnWindow.configure(bg="white")     

    #Background
    bgImg = Image.open("lib.png")

    bgHeight,bgWidth = bgImg.size 
    bgHeight = int(bgHeight/7.16); bgWidth = int(bgWidth/7.72)
    bgImg = bgImg.resize((bgWidth,bgHeight),Image.ANTIALIAS)

    Img = ImageTk.PhotoImage(bgImg)
    Background = Canvas(returnWindow)
    Background.create_image(300,340,image=Img)
    Background.configure(bg="white",width=bgWidth,height=bgHeight)
    Background.pack(expand=True)
    
    #Heading
    headingFrame = Frame(returnWindow,bg="grey",bd=5)
    headingFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame, text="Return Book", bg='black', fg='white', font=('Cailibri',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    #Labels
    labelFrame = Frame(returnWindow, bg="black")
    labelFrame.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.2)
    
    idLabel = Label(labelFrame, bg="black", fg="white", text="Book Id:", anchor="w", font=("Calibri",15))
    idLabel.place(relx=0.01,rely=0.45,relwidth=0.3,relheight=0.2)
    
    #Info Variables
    BookId = StringVar()

    #Input Feilds
    idEntry = Entry(labelFrame, textvariable=BookId, font=("Calibri",15))
    idEntry.place(relx=0.32,rely=0.45,relwidth=0.6,relheight=0.2)

    #Buttons
    Submitbtn = Button(returnWindow, text="Return", command=lambda: deleteIssue(con,BookId))
    Submitbtn.configure(font=("Calibri",14), bg='white', fg='black')
    Submitbtn.place(relx=0.300, rely=0.9, relwidth=0.20,relheight=0.08)
    
    Exitbtn = Button(returnWindow, text="Cancel", font=("Calibri",14), bg='white', fg='black', command=returnWindow.destroy)
    Exitbtn.place(relx=0.500, rely=0.9, relwidth=0.20,relheight=0.08)

    #main loop
    returnWindow.mainloop()
