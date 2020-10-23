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
    
    #Labels
    labelFrame = Frame(viewWindow, bg="white")
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    #Buttons
    Deletebtn = Button(viewWindow, text="Delete All", command=lambda: deleteAll(con))
    Deletebtn.configure(font=("Calibri",14), bg='white', fg='black')
    Deletebtn.place(relx=0.300, rely=0.9, relwidth=0.20,relheight=0.08)
    
    Exitbtn = Button(viewWindow, text="Cancel", font=("Calibri",14), bg='white', fg='black', command=viewWindow.destroy)
    Exitbtn.place(relx=0.500, rely=0.9, relwidth=0.20,relheight=0.08)

    #Main Text
    query1 = "SELECT * FROM books LIMIT 9"
    try:
        cur=con.cursor() 
        n = cur.execute(query1)
        rows = cur.fetchall()
        for i in range(0,10):
            for j in range(0,4):
                if(i==0):
                    e = Entry(labelFrame, font=("Calibri",12,"bold"))
                else:
                    e = Entry(labelFrame, font=("Calibri",12))    
                if(j==0):
                    e.configure(width=7)
                elif(j==1):
                    e.configure(width=24)
                elif(j==2):
                    e.configure(width=20)
                else:
                    e.configure(width=7)
                e.grid(row=i, column=j)
                if(i==0 and j==0):
                    e.insert(END, "BookId")
                elif(i==0 and j==1):
                    e.insert(END, "Title")
                elif(i==0 and j==2):
                    e.insert(END, "Author")
                elif(i==0 and j==3):
                    e.insert(END, "Status")
                elif(i<=n):
                    e.insert(END, rows[i-1][j])
                e.configure(state=DISABLED)
    except:
        messagebox.showinfo("Failed","Unable to fetch book details")
        viewWindow.destroy()
        return

    #main loop
    viewWindow.mainloop()
