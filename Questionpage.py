from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector

mydb=mysql.connector.connect(host ='localhost',user = 'root',password = 'wasd1234',database = 'quizdatabase')


##german stage displaying page 

class questionpage:
    
    
    def __init__(self,username,password,stageid,topic):#,username,password,topic
        self.stageid = stageid
        self.username = username
        self.password = password
        self.topic = topic
        self.firstquestionid = self.firstqidfinder(self.stageid,self.topic)
        self.qid = self.firstquestionid
        self.pagescore = 0
        self.page()

    def firstqidfinder(self,stage,topic):
        if topic=="german":
            if stage == 1:
                return 1
            elif stage ==2:
                return 6
            elif stage==3:
                return 11
            
        else:
            if stage == 1:
                return 16
            elif stage ==2:
                return 21
            elif stage==3:
                return 26
            
    
    def questupdate(self,questionid,questionlabel, opt1, opt2, opt3, opt4):
        c = mydb.cursor()
        sql  = "select ques, opt1, opt2, opt3, opt4, ans from questions where ques_id = " + str(questionid)
        c.execute(sql)
        details  = c.fetchall()
        quesdet = details[0]
        questionval = quesdet[0]
        opt1val = quesdet[1]
        opt2val = quesdet[2]
        opt3val = quesdet[3]
        opt4val = quesdet[4]
        questionlabel.config(text = questionval)
        opt1.config(text = opt1val)
        opt2.config(text = opt2val)
        opt3.config(text = opt3val)
        opt4.config(text = opt4val)
        c.close()

    def scoreupdate(self,button,qid,stage):
        c = mydb.cursor()
        select_opt = button.cget("text")
        sql = "select ans from questions where ques_id = "+str(qid)
        c.execute(sql)
        temp = c.fetchall()
        answer=temp[0][0]
        
        if answer == select_opt:
            self.pagescore = self.pagescore+1
        
##        if select_opt == answer:

    def clickoption(self,button,questionlabel, opt1, opt2, opt3, opt4,window):
        c = mydb.cursor()
        print(self.qid)
        self.scoreupdate(button,self.qid,self.stageid)
        if self.firstquestionid+4 == self.qid:
            print(self.pagescore)
            window.destroy()
            if self.topic == "german":
                messagebox.showinfo("Here is your Score","Score "+str(self.pagescore))
                sql1 = "select G"+str(self.stageid)+"_score from quiz_scores where username = %s and password =%s"
                val1 =(self.username,self.password)
                c.execute(sql1,val1)
                result1 = c.fetchone()
                print(result1)
                lastscore = result1[0]
                print(lastscore)
                if self.pagescore>lastscore:
                    sql2 = "UPDATE quiz_scores SET G"+str(self.stageid)+"_score = %s WHERE username = %s AND password = %s"
                    val2 = (str(self.pagescore),self.username,self.password)
                    c.execute(sql2,val2)
                    mydb.commit()
                import Germanstagedisplay
                question2german = Germanstagedisplay.germanstagedisp(self.username,self.password)
            elif self.topic == "french":
                messagebox.showinfo("Here is your Score","Score "+str(self.pagescore))
                sql1 = "select F"+str(self.stageid)+"_score from quiz_scores where username = %s and password =%s"
                val1 =(self.username,self.password)
                c.execute(sql1,val1)
                result1 = c.fetchone()
                lastscore = result1[0]
                if self.pagescore>lastscore:
                    sql2 = "UPDATE quiz_scores SET F"+str(self.stageid)+"_score = %s WHERE username = %s AND password = %s"
                    val2 = (self.pagescore,self.username,self.password)
                    c.execute(sql2,val2)
                import Frenchstagedisplay
                question2french = Frenchstagedisplay.frenchstagedisp(self.username,self.password)
        self.qid = self.qid + 1
        self.questupdate(self.qid,questionlabel,opt1, opt2, opt3, opt4)

    def page(self):
        root=Tk()
        root.geometry("1058x720+0+0")
        root.title("Language quiz")
        root.config(bg="navy")
        root.columnconfigure(1,weight=2)
##        qid = self.stageid*5-4
        
        questionframe=Frame(root, height=720, width=1058, bg="white",relief="ridge",bd=10)
        questionframe.propagate(0)
        questionframe.pack()
        img1=ImageTk.PhotoImage(file='Resources/questpageimg.jpg')
        image=Label(questionframe, image=img1).place(x=0,y=0,relwidth=1,relheight=1)

        question=Label(questionframe, text="question", bg="azure",
                                      font=("Helvetica", 20, "bold"))
        opt1=Button(questionframe, text="STAGE 1", command = lambda : self.clickoption(opt1,question,opt1,opt2,opt3,opt4,root), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        opt2=Button(questionframe, text="STAGE 2", command = lambda : self.clickoption(opt2,question,opt1,opt2,opt3,opt4,root), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        opt3=Button(questionframe, text="STAGE 3", command = lambda : self.clickoption(opt3,question,opt1,opt2,opt3,opt4,root), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        opt4=Button(questionframe, text="STAGE 3", command = lambda : self.clickoption(opt4,question,opt1,opt2,opt3,opt4,root), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        self.questupdate(self.firstquestionid,question, opt1, opt2, opt3, opt4)
        question.place(x=230, y=240)
        opt1.place(x=180,y=385)
        opt2.place(x=610,y=385)
        opt3.place(x=180,y=510)
        opt4.place(x=610,y=510)
        root.mainloop()
