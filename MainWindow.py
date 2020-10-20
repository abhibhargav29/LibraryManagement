from tkinter import Tk,Label,Frame,Canvas,Button
import pymysql as sql
from PIL import Image,ImageTk
from tkinter import messagebox
import sys
import time

password = input("Enter password: ")

#Establish Connection
try:
    con = sql.connect(host="localhost", user="root", password=password, database="library")   
    print("Connection Sucessful")
    print("Open GUI window")
except:
    print("Connection failed")
    time.sleep(2)
    sys.exit()

#GUI window
window = Tk()

#Window basics
window.title("Library")
window.geometry("600x600")

#Background
bgImg = Image.open("lib.png")

bgHeight,bgWidth = bgImg.size 
bgHeight = int(bgHeight/7.16); bgWidth = int(bgWidth/7.72)
bgImg = bgImg.resize((bgWidth,bgHeight),Image.ANTIALIAS)

Img = ImageTk.PhotoImage(bgImg)
Background = Canvas(window)
Background.create_image(300,340,image=Img)
Background.configure(bg="white",width=bgWidth,height=bgHeight)
Background.pack(expand=True)

#Heading
headingFrame = Frame(window,bg="grey",bd=5)
headingFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame, text="Library Management", bg='black', fg='white', font=('Cailibri',20))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Buttons
btn1 = Button(window,text="Add Book Details",bg='black', fg='white') #command=addBook)
btn1.place(relx=0.275,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(window,text="Delete Book",bg='black', fg='white') #command=delete)
btn2.place(relx=0.275,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(window,text="View Book List",bg='black', fg='white') #command=View)
btn3.place(relx=0.275,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(window,text="Issue Book to Student",bg='black', fg='white') #command = issueBook)
btn4.place(relx=0.275,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(window,text="Return Book",bg='black', fg='white') #command = returnBook)
btn5.place(relx=0.275,rely=0.8, relwidth=0.45,relheight=0.1)

#main loop
window.mainloop()
