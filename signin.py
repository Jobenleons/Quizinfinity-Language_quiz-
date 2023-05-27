from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

mydb=mysql.connector.connect(host ='localhost',user = 'root',password = 'wasd1234',database = 'quizdatabase')

##from Functions import validate
def signup_page():
    login_window.destroy()

    import signup

def validate(usrentry,passentry):#,languageframe1,loginframe
    c = mydb.cursor()
    sql = "select * from login_details where username=%s and password=%s"
    global username
    username = usrentry.get()
    global password
    password = passentry.get()
    values = (username,password)
    c.execute(sql,values)
##    print(c.fetchall())
    results = c.fetchall()
##    print(results)
    if results:
        messagebox.showinfo("Success","Login success")
        login_window.destroy()
        import chooselanguage
        signin2cl = chooselanguage.Chooselang(username,password)
##        shownextframe(languageframe1,loginframe,x,y)
        #print("Login successful")
    else:
        sql = "select password from login_details where username=%s"
        values = (username,)
        c.execute(sql,values)
        result = c.fetchone()
##        print(result)
        if result==None:
            messagebox.showerror("Username does not exist","Please Register as a new user")
        else:
            messagebox.showerror("Login Failed (Wrong password)","Enter the correct Password")
    c.close()
    

            
#Functionality Part
def hide():
    openeye.config(file='Resources/closed eye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='Resources/open eye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

# GUI Part
############__________________
login_window = Tk()
login_window.geometry('1280x720+50+50')
login_window.resizable()
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='Resources/image1.png')
bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0,relwidth=1,relheight=1)       #grid(row=0,column=0)
###########___________________________________________ login frame
login_frame = Frame(login_window,highlightbackground="blue",highlightthickness=2)
login_frame.place(x=640,y=360)



###########__________________

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='#0000EE')
heading.place(x=620,y=120)
#######_______________________________

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=2,fg='firebrick1')
usernameEntry.place(x=605,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)
######______________________________

frame1=Frame(login_window,width=230,height=2,bg='firebrick1')
frame1.place(x=605,y=222)
###############___________________________

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=2,fg='firebrick1')
passwordEntry.place(x=605,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)
#################___________________________
frame2=Frame(login_window,width=230,height=2,bg='firebrick1')
frame2.place(x=605,y=282)
################_____________________________
# closeeye=PhotoImage(file='closed eye.png')
# eyeButton=Button(login_window,image=closeeye,bd=0,bg='white',activebackground='white',cursor='hand2')
# eyeButton.place(x=805,y=260)
#####________________________________
openeye=PhotoImage(file='Resources/open eye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',
                 command=hide)
eyeButton.place(x=808,y=260)
#########_____________________

forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',
                    cursor='hand2', font=('Microsoft Yahei UI Light',11,'bold'),fg='firebrick1',activeforeground='firebrick1')
forgetButton.place(x=690,y=288)
###############____________________________
loginButton=Button(login_window,text='Login',command = lambda :validate(usernameEntry,passwordEntry),font=('Open Sans',16,'bold'),
                   fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=17)
loginButton.place(x=600,y=350)
#######___________________________
orLabel=Label(login_window,text='.................OR...............',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=600,y=400)
#######___________________________________________ facebook,google, twitter
facebook_logo=PhotoImage(file='Resources/facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=650,y=440)

google_logo=PhotoImage(file='Resources/google.png')
googleLabel=Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=700,y=440)
twitter_logo=PhotoImage(file='Resources/twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=750,y=440)
###########______________________________
signupLabel=Label(login_window,text="Don't Have an Account?",font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=600,y=500)

newaccountButton=Button(login_window,text='Create New One',font=('Open Sans',9,'bold underline'),
                   fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=740,y=500)


login_window.mainloop()
