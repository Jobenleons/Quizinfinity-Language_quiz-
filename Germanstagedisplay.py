from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector
mydb=mysql.connector.connect(host ='localhost',user = 'root',password = 'wasd1234',database = 'quizdatabase')

##c = mydb.cursor()
class germanstagedisp:
    topic = "german"
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.disppage()

    def dispaccountpage(self,window):
        window.destroy()
        u = self.username
        p = self.password
        import Account_details_page
        german2ad = Account_details_page.Accountdetails(u,p,"Germanstagedisplay")
        
    def getstagescores(self):
        sql = "select G1_score,G2_score,G3_score from quiz_scores where username = %s and password =%s"
        values = (self.username,self.password)
        c = mydb.cursor()
        c.execute(sql,values)
        results = c.fetchone()
        g1 = results[0]
        g2 = results[1]
        g3 = results[2]
        return g1,g2,g3

    def dispmessage(self):
        messagebox.showinfo("Locked","Complete all levels before this stage.")
        
    def disppage(self):
##        print("Hey")
        root=Tk()
        root.geometry("1080x1920+0+0")
        root.title("Language quiz")
        root.config(bg="navy")
        root.columnconfigure(1,weight=2)
        german_stage=Frame(root, height=1080, width=1920, bg="white",relief="ridge",bd=10)
        german_stage.propagate(0)
        german_stage.pack()
        img1=ImageTk.PhotoImage(file='Resources/stage pic.png')
        image=Label(german_stage, image=img1).place(x=0,y=0,relwidth=1,relheight=1)

        gstage_title=Label(root, text="select the stage", bg="azure",
                                      font=("Helvetica", 30, "bold")).place(x=400, y=50)
        g1,g2,g3 = self.getstagescores()
        print(g1,g2,g3)
        stg1=Button(root, text="STAGE 1", command = lambda : self.showquestionpage(root,1), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        if g1 > 3:
            stg2=Button(root, text="STAGE 2", command = lambda : self.showquestionpage(root,2), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        else:
            stg2=Button(root, text="STAGE 2", command = lambda :self.dispmessage(), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        if g2 > 3:
            stg3=Button(root, text="STAGE 3", command = lambda : self.showquestionpage(root,3), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        else:
            stg3=Button(root, text="STAGE 3", command = lambda :self.dispmessage(), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        back=Button(root, text="Back", command = lambda : self.showlanguagepage(root), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        acc_det = Button(root, text="Account Details", command = lambda :self.dispaccountpage(root), width=20, height=3, fg="royalblue4", bg="lavender",
                                     font=("Helvetica", 10, "bold italic"))
        acc_det.place(x=800,y=100)
        stg1.place(x=200,y=100)
        stg2.place(x=450,y=250)
        stg3.place(x=700,y=450)
        back.place(x=800,y=50)
        root.mainloop()

##german stage displaying page

    
    def showquestionpage(self,window,stage):
        window.destroy()
        import Questionpage
        german2qp = Questionpage.questionpage(self.username,self.password,stage,germanstagedisp.topic)

    def showlanguagepage(self,window):
        messagebox.showinfo("Thank you for learning!","Visit us soon!")
        window.destroy()
        import chooselanguage
        german2cl = chooselanguage.Chooselang(self.username,self.password)

##obj = germanstagedisp("admin","password")

