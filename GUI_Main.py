

from tkinter import * 
import tkinter as tk

from PIL import Image , ImageTk     


##############################################+=============================================================

root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")
import sqlite3
my_conn = sqlite3.connect('face.db')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Face Attendance System")


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('face1.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
###################################################################
def display():
    
    from subprocess import call
    call(["python", "GUI_master.py"])
    
    
def window():
    root.destroy()    
#####################################################################






lbl = tk.Label(root, text="Attendance Using Face Detection", bd=5,font=('times', 40,' bold '), height=1, width=30,bg="Black",fg="indian red")
lbl.place(x=330, y=5)




button1 = tk.Button(text="Face Attendance System",bd=5,command=display,width=20, height=1, font=('times', 15, ' bold '),bg="purple",fg="white")
button1.place(x=650, y=400)

button1 = tk.Button(text="Exit",command=window,width=20, bd=5,height=1, font=('times', 15, ' bold '),bg="red",fg="white")
button1.place(x=650, y=470)



root.mainloop()