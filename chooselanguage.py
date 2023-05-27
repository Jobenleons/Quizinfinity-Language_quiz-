from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector

mydb=mysql.connector.connect(host ='localhost',user = 'root',password = 'wasd1234',database = 'quizdatabase')


class Chooselang:
    def __init__(self,username,password):
        self.username = username
        self.password = password
##        print(self.username,self.password)
        self.displaypage()
 
    def dispgermanstage(self,window):
        window.destroy()
##        print("Hey")
        u = self.username
        p = self.password
        import Germanstagedisplay
        cl2german = Germanstagedisplay.germanstagedisp(u,p)

    def dispfrenchstage(self,window):
        window.destroy()
        u = self.username
        p = self.password
        import Frenchstagedisplay
        cl2french = Frenchstagedisplay.frenchstagedisp(u,p)

    def dispaccountpage(self,window):
        window.destroy()
        u = self.username
        p = self.password
        import Account_details_page
        cl2ad = Account_details_page.Accountdetails(u,p,"chooselanguage")

    def numberoflearners(self):
        c= mydb.cursor()
        sqlg = "select * from quiz_scores where G1_score>3"
        c.execute(sqlg)
        resg = c.fetchall()
        lg = len(resg)
        sqlf = "select * from quiz_scores where F1_score>3"
        c.execute(sqlf)
        resf = c.fetchall()
        lf = len(resf)
        return lg,lf 
        
    def displaypage(self):
        root=Tk()
        root.geometry("1080x1920+0+0")
        root.title("Language quiz")
        root.config(bg="navy")
        root.columnconfigure(1,weight=2)
        lang_page=Frame(root, height=1080, width=1920, bg="black",relief="ridge",bd=10)
        lang_page.propagate(0)
        lang_page.pack()
        lg, lf = self.numberoflearners() 
        img1=ImageTk.PhotoImage(file='Resources/book1.png')
        image=Label(lang_page, image=img1).place(x=0,y=0,relwidth=1,relheight=1)
        lang_title=Label(root, text="Choose the language", bg="azure",
                                    font=("Helvetica", 30, "bold italic underline"))
        acc_det = Button(root, text="Account Details", command = lambda :self.dispaccountpage(root), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        german=Button(root, text="German", command = lambda :self.dispgermanstage(root), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        german_users = Label(root, text=str(lg)+" learners", bg="azure",
                                    font=("Helvetica", 30, "bold italic underline")).place(x=700,y=200)
        french=Button(root, text="french", command = lambda :self.dispfrenchstage(root), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        french_users = Label(root, text=str(lf)+" learners", bg="azure",
                                    font=("Helvetica", 30, "bold italic underline")).place(x=700,y=350)
        lang_title.place(x=350,y=100)
        acc_det.place(x=800,y=100)
        german.place(x=450,y=200)
        french.place(x=450,y=350)
        root.mainloop()
    
##obj = Chooselang('admin','password')

# a=ttk.notbook()
