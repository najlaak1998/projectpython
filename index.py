from tkinter import *
Window=Tk()
Window.title("Registraation Form")
Window.geometry("300x200+10+20")

labl_0 =Label(text="Registration form", width=20, font=("bold", 20),fg="blue")
labl_0.place(x=90, y=53)

labl_1 =Label(text=" Name", width=20, font=("bold", 10))
labl_1.place(x=80, y=130)

entry_1 = Entry(Window,text="Enter Name:")
entry_1.place(x=240, y=130)

labl_2 = Label(text="phone", width=20, font=("bold", 10))
labl_2.place(x=68, y=180)

entry_02 = Entry(Window,text="Enter phone:")
entry_02.place(x=240, y=180)

labl_3 = Label(text="Gender", width=20, font=("bold", 10))
labl_3.place(x=70, y=230)

Radiobutton(text="Male",  value=1).place(x=235, y=230)
Radiobutton(text="Female",value=2).place(x=290, y=230)

labl_4 = Label(text="Emergency", width=20, font=("bold", 10))
labl_4.place(x=70, y=280)

entry_04 = Entry(Window,text="Enter Emergency:")
entry_04.place(x=240, y=280)

labl_5 = Label(text="Payment mood", width=20, font=("bold", 10))
labl_5.place(x=70, y=320)
entry_05 = Entry(Window,text="Enter Payment mood:")
entry_05.place(x=243, y=320)

Checkbutton(text="remember me?").place(x=200, y=350)

Button(text='Submit',width=20,bg='blue',fg='white').place(x=200,y=400)

Window.mainloop()


