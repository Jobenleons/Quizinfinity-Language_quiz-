from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

import mysql.connector

mydb=mysql.connector.connect(host ='localhost',user = 'root',password = 'wasd1234',database = 'quizdatabase')
c = mydb.cursor()

def login_page():
    signup_window.destroy()

    import signin


#Functionality Part
def hide():
    openeye.config(file='Resources/closed eye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='Resources/open eye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

# def hide():
#     openeye.config(file='closed eye.png')
#     passwordEntry.config(show='*')
#     eyeButton.config(command=show)
#
# def show():
#     openeye.config(file='open eye.png')
#     passwordEntry.config(show='')
#     eyeButton.config(command=hide)


def newuser(usrentry,passentry,cnfpassword,emailentry,window):
    try:
        sql= "insert into login_details(username,password,email) values(%s,%s,%s)"
        sql1 = "insert into quiz_scores(username,password) values(%s,%s)"
        s1 = usrentry.get()
        s2 = passentry.get()
        s3 = cnfpassword.get()
        s4 = emailentry.get()
        if s1=="" or s2=="" or s3 =="" or s4 == "":
            messagebox.showwarning("Warning!!","Fields canot be empty")
        elif s2!=s3:
            messagebox.showwarning("Warning!!","Passwords do not match")
        else:
            val1 = (s1,s2)
            val = (s1,s2,s4)
            c.execute(sql,val)
            c.execute(sql1,val1)
            mydb.commit()
            messagebox.showinfo("Success", "Welcome "+str(s1))
            window.destroy()
            import chooselanguage
            signup2cl = chooselanguage.Chooselang(s1,s2)
    except:
        messagebox.showwarning("Username aldready taken!!","Choose a diffrent username")
                



#####################_________________
signup_window=Tk()
signup_window.geometry('1280x720+50+50')
signup_window.title("Signup Page")
signup_window.resizable()

background=ImageTk.PhotoImage(file='Resources/sign up.jpg')
bgLabel=Label(signup_window,image=background)
bgLabel.place(x=0,y=0,relwidth=1,relheight=1)
###################_____________________________________
frame = Frame(signup_window)
frame.place(x=460,y=210)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='#0000EE')
heading.grid(row=0,column=0,padx=10,pady=10)
##########______________________________________________

emailLabel=Label(frame,text='Email Address',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg="firebrick1")
emailLabel.grid(row=1,column=0,sticky="w",padx=25,pady=(10,0))

emailEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',15,'bold'),bg="#000fff000",fg='black')
emailEntry.grid(row=2,column=0)
############__________________________

usernameLabel=Label(frame,text='UserName',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg="firebrick1")
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',15,'bold'),bg="#000fff000",fg='black')
usernameEntry.grid(row=4,column=0,padx=25)


###########_____________________________
passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg="firebrick1")
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',15,'bold'),bg="#000fff000",fg='black')
passwordEntry.grid(row=6,column=0,padx=25)
##########################______________________________________  # eye function
openeye=PhotoImage(file='Resources/open eye.png')
eyeButton=Button(frame,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',
                 command=hide)
eyeButton.place(x=340,y=260)

###############_________________
confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg="firebrick1")
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmpasswordEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',15,'bold'),bg="#000fff000",fg='black')
confirmpasswordEntry.grid(row=8,column=0,padx=25)

# openeye=PhotoImage(file='closed eye (1).png')
# eyeButton=Button(frame,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',
#                  command=hide)
# eyeButton.pack(x=340,y=300)

###############_________________________________


termsandconditions=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',12,'bold'),fg='firebrick1',bg='white',
                               activebackground='white',activeforeground='firebrick1',cursor='hand2')
termsandconditions.grid(row=9,column=0)

signupButton=Button(frame,text='SIGN UP',command = lambda : newuser(usernameEntry,passwordEntry,confirmpasswordEntry,emailEntry,signup_window),font=('Open Sans',16,'bold'),
                   fg='black',bg='blue',activeforeground='white',activebackground='blue',cursor='hand2',bd=0,width=23)
signupButton.grid(row=10,column=0,pady=10)

######################__________________________

alreadyaccount=Label(frame,text="Don't have an account?", font=('Open Sans','9','bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=10)
loginButton=Button(frame, text='Login',font=('Open Sans',9,'bold underline'),
                   fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=login_page)
loginButton.place(x=150,y=450)







signup_window.mainloop()

