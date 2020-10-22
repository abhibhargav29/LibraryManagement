from tkinter import Tk,Label,Frame,Canvas,Button,Toplevel,Entry,StringVar
import pymysql as sql
from PIL import Image,ImageTk 
from tkinter import messagebox

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
    except:
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