from tkinter import Tk,Label,PhotoImage,Canvas
import pymysql as sql
from tkinter import messagebox
import sys
import time

try:
    con = sql.connect(host="localhost", user="root", password="4647", database="library")   
    print("Connection Sucessful")
except:
    print("Connection failed")
    time.sleep(3)
    sys.exit()

window = Tk()
window.title("Library")
#window.geometry("700x600")

C= Canvas(window, bg="blue", height=600, width=500)
bgImg = PhotoImage(file = "lib.png")
background = Label(window, image=PhotoImage)
background.place(x=0,y=0,relwidth=1,relheight=1)


window.mainloop()