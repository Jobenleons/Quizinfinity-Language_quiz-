from tkinter import *
from tkinter import messagebox
from functools import partial
import mysql.connector

mydb=mysql.connector.connect(host ='localhost',user = 'root',password = 'wasd1234',database = 'quizdatabase')
c = mydb.cursor()
import time

#######Login Newuser functions######


def validate(usrentry,passentry,languageframe1,loginframe):#,languageframe1,loginframe
    sql = "select * from login_details where username=%s and password=%s"
    global username
    username = usrentry.get()
    global password
    password = passentry.get()
    values = (username,password)
    c.execute(sql,values)

    results = c.fetchall()
##    print(results)
    if results:
        messagebox.showinfo("Success","Login success")
##        shownextframe(languageframe1,loginframe,x,y)
        #print("Login successful")
    else:
        sql = "select psd from login_details where usr=%s"
        values = (username.get(),)
        c.execute(sql,values)
        result = c.fetchone()
##        print(result)
        if result==None:
            messagebox.showerror("Username does not exist","Please Register as a new user")
        else:
            messagebox.showerror("Login Failed (Wrong password)","Enter the correct Password")
            
        #print("Login unsuccessful")

##print(username)
def newuser(usrentry,passentry,cnfpassword):
    sql= "insert into login_details(username,password) values(%s,%s)"
    sql1 = "insert into quiz_scores(username,password) values(%s,%s)"
    s1 = usrentry.get()
    s2 = passentry.get()
    s3 = cnfpassword.get()
    if s1=="" or s2=="" or s3 =="":
        messagebox.showwarning("Warning!!","Fields canot be empty")
    elif s2!=s3:
        messagebox.showwarning("Warning!!","Passwords do not match")
    else:
        val = (s1,s2)
        c.execute(sql,val)
        c.execute(sql1,val)
        mydb.commit()
        messagebox.showinfo("Success", "Welcome "+str(s1))


def shownextframe(nextframe,currentframe,x,y):
    currentframe.place_forget()
    nextframe.place(x=x,y=y)

def questupdate(questionid,questionlabel, opt1, opt2, opt3, opt4):
    sql  = "select ques, opt1, opt2, opt3, opt4, ans from questions where ques_id = " + str(questionid)
    c.execute(sql)
    details  = c.fetchall()
    quesdet = details[0]
    questionlabel.config(text = questdet[0])
    opt1.config(text = questdet[1])
    opt2.config(text = questdet[2])
    opt3.config(text = questdet[3])
    opt4.config(text = questdet[4])

def scoreupdateG(usrentry,psdentry,button,questionid,stage):
    select_opt = button.cget("text")
    sql = "select ans from questions where ques_id = "+str(questionid)
    c.execute(sql)
    temp = c.fetchall()
    answer=temp[0][0]
    username = usrentry.get()
    password = psdentry.get()
    if select_opt == answer:
        sql = "UPDATE quiz_scores SET G" + str(stage) + "_score = G" + str(stage) + "_score+1 WHERE username = " +str(username)+" AND password =" + str(password)
        c.execute(sql)
        c.commit()

def scoreupdateF(usrentry,psdentry,button,questionid,stage):
    select_opt = button.cget("text")
    sql = "select ans from questions where ques_id = "+str(questionid)
    c.execute(sql)
    temp = c.fetchall()
    answer=temp[0][0]
    username = usrentry.get()
    password = psdentry.get()
    if select_opt == answer:
##        sql = "UPDATE quiz_scores SET F" + str(stage) + "_score = F" + str(stage) + "_score+1 WHERE username = " +str(username)+" AND password =" + str(password)
##        c.execute(sql)
##        c.commit()
    
def g1question(questionid,questionframe,stageframe, questionlabel, opt1, opt2, opt3, opt4):
    if questionid ==5:
        shownextframe(stageframe,questionframe)
    questupdate(questionid,questionlabel, opt1, opt2, opt3, opt4)
    shownextframe(questionframe,stageframe)
    scoreupdateG(usrentry,psdentry,button,questionid,1)
    
    else:
        g1question(questionid+1,questionframe,questionframe,questionlabel,opt1,opt2,opt3,opt4)

def g2question(questionid,questionframe,stageframe, questionlabel, opt1, opt2, opt3, opt4):
    if questionid ==10:
        shownextframe(stageframe,questionframe)
        
    questupdate(questionid,questionlabel, opt1, opt2, opt3, opt4)
    shownextframe(questionframe,stageframe)
    scoreupdateG(usrentry,psdentry,button,questionid,2)
    else:
        g2question(questionid+1,questionframe,questionframe,questionlabel,opt1,opt2,opt3,opt4)

def g3question(questionid,questionframe,stageframe, questionlabel, opt1, opt2, opt3, opt4):
    if questionid ==15:
        shownextframe(stageframe,questionframe)
    questupdate(questionid,questionlabel, opt1, opt2, opt3, opt4)
    shownextframe(questionframe,stageframe)
    scoreupdateG(usrentry,psdentry,button,questionid,1)
    else:
        g3question(questionid+1,questionframe,questionframe,questionlabel,opt1,opt2,opt3,opt4)

def f1question(questionid,questionframe,stageframe, questionlabel, opt1, opt2, opt3, opt4):
    if questionid ==5:
        shownextframe(stageframe,questionframe)
        
    questupdate(questionid,questionlabel, opt1, opt2, opt3, opt4)
    shownextframe(questionframe,stageframe)
    scoreupdateF(usrentry,psdentry,button,questionid,1)
    
    else:
        f1question(questionid+1,questionframe,questionframe,questionlabel,opt1,opt2,opt3,opt4)

def f2question(questionid,questionframe,stageframe, questionlabel, opt1, opt2, opt3, opt4):
    if questionid ==10:
        shownextframe(stageframe,questionframe)
    questupdateF(questionid,questionlabel, opt1, opt2, opt3, opt4)
    shownextframe(questionframe,stageframe)
    scoreupdate(usrentry,psdentry,button,questionid,1)
    else:
        f2question(questionid+1,questionframe,questionframe,questionlabel,opt1,opt2,opt3,opt4)

def f3question(questionid,questionframe,stageframe, questionlabel, opt1, opt2, opt3, opt4):
    if questionid ==15:
        shownextframe(stageframe,questionframe)
    questupdateF(questionid,questionlabel, opt1, opt2, opt3, opt4)
    shownextframe(questionframe,stageframe)
    scoreupdate(usrentry,psdentry,button,questionid,1)
    else:
        f3question(questionid+1,questionframe,questionframe,questionlabel,opt1,opt2,opt3,opt4)



            
        
    

   
w = Tk()
w.geometry("600x400")

login_frame = Frame (w,highlightbackground ="blue",highlightthickness = 2)
login_frame.place(x=150,y=150)
l1=Label(login_frame,text="Enter Username")
l2=Label(login_frame,text="Enter Password")
usr = Entry(login_frame)
psd = Entry(login_frame,show="*")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
usr.grid(row=0,column=1)
psd.grid(row=1,column=1)
v=IntVar(value=0)
##c1=Checkbutton(login_frame,text = "Show password",variable=v,onvalue=1 , offvalue = 0,command = psdshow)
##c1.grid(row = 1 ,column = 2)
b1 =Button(login_frame,text = "Login",command=lambda :validate(usr,psd))
b1.grid(row=2,column=1)
b2 =Button(login_frame,text = "New User? Register now" ,command = lambda :shownextframe(reg_frame,login_frame,150,150))
b2.grid(row=3,column=1)

reg_frame=Frame(w)
l3 = Label(reg_frame,text = "Enter UserName").grid(row=0,column=0)
l4 = Label(reg_frame,text = "Enter Password").grid(row=1,column=0)
l5 = Label(reg_frame,text = "Confirm Password").grid(row=2,column=0)
e1 = Entry(reg_frame)
e1.grid(row=0,column=1)

e2 = Entry(reg_frame,show = "*")
e2.grid(row=1,column=1)
e3 = Entry(reg_frame,show = "*")
e3.grid(row=2,column=1)
b3 = Button(reg_frame,text = "Submit", command = lambda :scoreupdate(usr,psd)).grid(row=3,column=1)
b4 = Button(reg_frame,text = "Login", command = lambda :shownextframe(login_frame,reg_frame,150,150)).grid(row=3,column=0)
##print(b1.cget("text"))



w.mainloop()
