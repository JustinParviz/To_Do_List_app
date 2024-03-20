import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list = []

#icon
Image_icon = PhotoImage(file="images/task.png")
root.iconphoto(False,Image_icon)

#top bar
TopImage = PhotoImage(file="images/topbar.png")
Label(root,image = TopImage).pack()

dockImage = PhotoImage(file="images/dock.png")
Label(root,image=dockImage,bg="#32405b").place(x=30,y=25)

noteImage = PhotoImage(file="images/task.png")
Label(root,image=noteImage,bg="#32405b").place(x=340,y=25)

heading = Label(root,text="ALL TASKS",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=20)

#main
frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task = StringVar()
task_entry = Entry(frame,width=18,font="ariel 20",bd=0)
task_entry.place(x=10,y=7)


button = Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0)
button.place(x=300,y=0)





root.mainloop()

