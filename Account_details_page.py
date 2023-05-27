from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
from tkinter import filedialog
##from matplotlib.figure import Figure
##from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
##NavigationToolbar2Tk)
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from functions import *

# db connection
mydb=mysql.connector.connect(host ='localhost',user = 'root',password = 'wasd1234',database = 'quizdatabase')

# c = mydb.cursor()

class Accountdetails:
    def __init__(self,username,password,prevfile):
        self.username = username
        self.password = password
        self.prevfile = prevfile
        self.getdetails()
        self.page()

    def changeframe(self,nextframe,prevframe):
        prevframe.place_forget()
        nextframe.place(x=50, y=50)

    def deletedetails(self,window):
        c = mydb.cursor()
        sql = "DELETE FROM login_details WHERE username=%s and password= %s"
        sql1 = "DELETE FROM quiz_scores WHERE username=%s and password= %s"
        val = (self.username,self.password)
        c.execute(sql,val)
        c.execute(sql1,val)
        mydb.commit()
        mydb.close()
        window.destroy()
        import signin
    
    def dispprevpage(self,window):
        window.destroy()
        u = self.username
        p = self.password
        if self.prevfile=="chooselanguage":
            mydb.close()
            import chooselanguage
            ad2cl = chooselanguage.Chooselang(u,p)
        if self.prevfile=="Germanstagedisplay":
            mydb.close()
            import Germanstagedisplay
            ad2german = Germanstagedisplay.germanstagedisp(u,p)
        if self.prevfile=="FrenchStagedisplay":
            mydb.close()
            import FrenchStagedisplay
            ad2french = FrenchStagedisplay.frenchstagedisp(u,p)

    def getscores(self,language):
        c = mydb.cursor()
        if language =="g":
            sql = "select G1_score, G2_score, G3_score from quiz_scores where username = %s and password = %s"
            values =(self.username,self.password)
            c.execute(sql,values)
            results = c.fetchone()
            g1 = results[0]
            g2 = results[1]
            g3 = results[2]
            return g1,g2,g3
        if language =="f":
            sql = "select F1_score,F2_score,F3_score from quiz_scores where username = %s and password = %s"
            values =(self.username,self.password)
            c.execute(sql,values)
            results = c.fetchone()
            f1 = results[0]
            f2 = results[1]
            f3 = results[2]
            return f1,f2,f3

    
    def getdetails(self):
        c = mydb.cursor()
        sql = "select email,phone,address from login_details where username= %s and password= %s"
        values = (self.username,self.password)
        c.execute(sql,values)
        results = c.fetchone()
        self.email = results[0]
        self.phone = results[1]
        self.address = results[2]
        

    def changedetails(self,newusername,email,address,phone,user_name,user_email,user_phone,user_address):
        try:
            l = ["username","email","phone","address"]
            l1 = [newusername,email,phone,address]
            c = mydb.cursor()
            for i,j in zip(l,l1):
                if j != "":
                    print(i,str(j))
                    
                    sql= "UPDATE login_details SET "+i+" = %s WHERE username = %s AND password = %s"
                    sql1= "UPDATE quiz_scores SET "+i+" = %s WHERE username = %s AND password = %s"
                    val = (j,self.username,self.password)
                    
                    if i=="username":
                        c.execute(sql,val)
                        c.execute(sql1,val)
                        mydb.commit()
                        self.username = newusername
                        user_name.config(text = "Hi "+self.username+"!")
                    if i=="email":
                        c.execute(sql,val)
                        mydb.commit()
                        user_email.config(text = email)
                    if i=="phone":
                        c.execute(sql,val)
                        mydb.commit()
                        user_phone.config(text = phone)
                    if i=="address":
                        c.execute(sql,val)
                        mydb.commit()
                        user_address.config(text = address)
            
        except:
            messagebox.showwarning("Username aldready taken!!","Choose a diffrent username")
                
    def page(self):
        window = Tk()
        window.geometry("800x500")
        window.title("Account Details")
        # Window 1
        disp_frame1 = Frame(window, width=800, height=100)
        disp_frame1.config(background='#0081C9')
        disp_frame1.pack()

        disp_frame2 = Frame(window, width=800, height=100)
        disp_frame2.config(background="#FFC93C", relief='groove')
        disp_frame2.place(x=0, y=400)

        user_detail_frame = Frame(window, width=700, height=400)
        user_detail_frame.place(x=50, y=50)
        
        account_label = Label(user_detail_frame, text="Account Details", font=("Times New Roman", 15), border=0)
        account_label.place(x=300, y=10)

        btn1 = Button(user_detail_frame, text="Back", border=5, width=8, command=lambda : self.dispprevpage(window))
        btn1.place(x=50, y=320)

        btn2 = Button(user_detail_frame, text="Edit Details", border=5, width=12, command=lambda : self.changeframe(edit_details_frame,user_detail_frame))
        btn2.place(x=300, y=320)

        btn3 = Button(user_detail_frame, text="Delete Account", border=5, width=14, command=lambda : self.changeframe(delete_frame,user_detail_frame))
        btn3.place(x=550, y=320)
        
        ##img_frame = Frame(user_detail_frame, width=200, height=200, background='grey')
        ##img_frame.place(x=30, y=100)
        
        btn4 = Button(user_detail_frame, text="Score", border=5, width=8, command=lambda : self.changeframe(score_frame,user_detail_frame))
        btn4.place(x=550, y=180)
          
        user_name = Label(user_detail_frame, text="Hi "+self.username+"!", font=("Times New Roman", 35))
        user_name.place(x=50, y=90)
        
        user_email = Label(user_detail_frame, text=self.email, font=("Arial Bold", 15))
        user_email.place(x=50, y=150)
        
        user_phone = Label(user_detail_frame, text=self.phone, font=("Times New Roman", 15))
        user_phone.place(x=50, y=180)

        user_address = Label(user_detail_frame, text=self.address, font=("Times New Roman", 15))
        user_address.place(x=50, y=210)
        
        # edit window

        edit_details_frame = Frame(window, width=700, height=400)

        edit_label = Label(edit_details_frame, text="Edit Details", font=("Times New Roman", 15), border=0)
        edit_label.place(x=300, y=10)

        Label(edit_details_frame, text="Enter your New User Name  ", font=("Times New Roman", 15)).place(x=50, y=100)
        e1 = Entry(edit_details_frame, width=25, font=("Times New Roman", 15))
        e1.place(x=350, y=100)
        
        Label(edit_details_frame, text="Enter your Email-Id  ", font=("Times New Roman", 15)).place(x=50, y=150)
        e2 = Entry(edit_details_frame, width=25, font=("Times New Roman", 15))
        e2.place(x=350, y=150)
        Label(edit_details_frame, text="Enter your Address  ", font=("Times New Roman", 15)).place(x=50, y=200)
        e3 = Entry(edit_details_frame, width=25, font=("Times New Roman", 15))
        e3.place(x=350, y=200)
        Label(edit_details_frame, text="Enter your phone number ", font=("Times New Roman", 15)).place(x=50, y=250)
        e4 = Entry(edit_details_frame, width=25, font=("Times New Roman", 15))
        e4.place(x=350, y=250)

        btn1 = Button(edit_details_frame, width=8, text="Back", border=5, command=lambda : self.changeframe(user_detail_frame,edit_details_frame))
        btn1.place(x=450, y=300)

        btn2 = Button(edit_details_frame,width=10, text="Save Details", border=5,command = lambda : self.changedetails(e1.get(),e2.get(),e3.get(),e4.get(),user_name,user_email,user_phone,user_address))
        btn2.place(x=600, y=300)
        # window 2

        delete_frame = Frame(window, width=700, height=400)

        delete_label = Label(delete_frame, text="Delete Account", font=("Times New Roman", 15), border=0)
        delete_label.place(x=300, y=10)

        Label(delete_frame, text="Enter your email  ", font=("Times New Roman", 15)).place(x=100, y=100)
        d1 = Entry(delete_frame, width=25, font=("Times New Roman", 15)).place(x=300, y=100)
        Label(delete_frame, text="Enter your password  ", font=("Times New Roman", 15)).place(x=100, y=150)
        d2 = Entry(delete_frame, width=25, font=("Times New Roman", 15)).place(x=300, y=150)
        Label(delete_frame, text="Confirm your password  ", font=("Times New Roman", 15)).place(x=100, y=200)
        d3 = Entry(delete_frame, width=25, font=("Times New Roman", 15)).place(x=300, y=200)

        btn1 = Button(delete_frame, width=10, text="Cancel", border=5, command=lambda : self.changeframe(user_detail_frame,delete_frame))
        btn1.place(x=200, y=330)

        btn2 = Button(delete_frame, width=10, text="Confirm", border=5, command=lambda : self.deletedetails(window))
        btn2.place(x=450, y=330)

        ## Score frame

        score_frame = Frame(window, width=700, height=400)
        
        score_label = Label(score_frame, text="Score", font=("Times New Roman", 15), border=0)
        score_label.place(x=300, y=10)

        btn1 = Button(score_frame, text="Back", border=5, width=8, command=lambda : self.changeframe(user_detail_frame,score_frame))
        btn1.place(x=50, y=320)

        image_german = Image.open('Resources/German.jpeg')
        imgg= ImageTk.PhotoImage(image_german)

        image_french = Image.open('Resources/French.jpeg')
        imgf= ImageTk.PhotoImage(image_french)
##        image_german = image_german.resize((150,150), Image.ANTIALIAS)
        
        
        myButton1 = Button(score_frame, text="Results - German",command = lambda : self.changeframe(germanframe,score_frame),padx=50,pady=50,fg="green",bg="white",borderwidth=10,font=("Helvetica", 10, "bold"),image = imgg)
        myButton2 = Button(score_frame, text="Results - French",command = lambda : self.changeframe(frenchframe,score_frame),padx=53,pady=50,fg="green",bg="white",borderwidth=10,font=("Helvetica", 10, "bold"),image = imgf)

        myButton1.place(x=50, y=70)
        myButton2.place(x=350, y=70)

        ## German score

        germanframe = Frame(window, width=700, height=400)
        
        image_french1 = image_french.resize((100,50), Image.LANCZOS)
        imgf1= ImageTk.PhotoImage(image_french1)
        
        german_label = Label(germanframe, text="Score", font=("Times New Roman", 15), border=0)
        german_label.place(x=300, y=10)

##        image_german = Image.open('Resources/German.jpeg')
##        imgg= ImageTk.PhotoImage(image_german)
##
##        image_french = Image.open('Resources/French.jpeg')
##        imgf= ImageTk.PhotoImage(image_french)
        
        myButton1 = Button(germanframe, text="Back",command = lambda : self.changeframe(score_frame,germanframe),padx=30,fg="green",bg="white",borderwidth=10,font=("Helvetica", 10, "bold"))
        myButton2 = Button(germanframe, text="Results - French",command = lambda : self.changeframe(frenchframe,germanframe),padx=53,pady=50,fg="green",bg="white",borderwidth=10,font=("Helvetica", 10, "bold"),image = imgf1)

        myButton1.place(x=50, y=70)##grid(row =0,column = 1)
        myButton2.place(x=50, y=140)##grid(row=1,column=1)

        g1,g2,g3 = self.getscores("g")
        totg = g1+g2+g3

        datag = {'Stages': ['G1', 'G2', 'G3', 'Total'],
                 'Score': [g1,g2,g3, totg]
                 }
        dfg = pd.DataFrame(datag)
        
        figure1 = plt.Figure(figsize=(7, 6), dpi=55)
        axg = figure1.add_subplot(111)
        barg = FigureCanvasTkAgg(figure1, germanframe)
        barg.get_tk_widget().place(x=250, y=40)#pack(side=tk.RIGHT, fill=tk.BOTH)
        dfg = dfg[['Stages', 'Score']].groupby('Stages').sum()
        dfg.plot(kind='bar', legend=True, ax=axg)
        axg.set_title('Stages Vs. Score')

        ## French score

        frenchframe = Frame(window, width=700, height=400)
        
        image_german1 = image_german.resize((100,50), Image.LANCZOS)
        imgg1= ImageTk.PhotoImage(image_german1)
        
        french_label = Label(frenchframe, text="Score", font=("Times New Roman", 15), border=0)
        french_label.place(x=300, y=10)

##        image_german = Image.open('Resources/German.jpeg')
##        imgg= ImageTk.PhotoImage(image_german)
##
##        image_french = Image.open('Resources/French.jpeg')
##        imgf= ImageTk.PhotoImage(image_french)
        
        myButton1 = Button(frenchframe, text="Back",command = lambda : self.changeframe(score_frame,frenchframe),padx=30,fg="green",bg="white",borderwidth=10,font=("Helvetica", 10, "bold"))
        myButton2 = Button(frenchframe, text="Results - German",command = lambda : self.changeframe(germanframe,frenchframe),padx=53,pady=50,fg="green",bg="white",borderwidth=10,font=("Helvetica", 10, "bold"),image = imgg1)

        myButton1.place(x=50, y=70)##grid(row =0,column = 1)
        myButton2.place(x=50, y=140)##grid(row=1,column=1)

        f1,f2,f3 = self.getscores("f")
        totf = f1+f2+f3

        dataf = {'Stages': ['F1', 'F2', 'F3', 'Total'],
                 'Score': [f1,f2,f3, totf]
                 }
        dff = pd.DataFrame(dataf)
        

        figuref = plt.Figure(figsize=(7, 6), dpi=55)
        axf = figuref.add_subplot(111)
        barf = FigureCanvasTkAgg(figuref, frenchframe)
        barf.get_tk_widget().place(x=250, y=40)#pack(side=tk.RIGHT, fill=tk.BOTH)
        dff = dff[['Stages', 'Score']].groupby('Stages').sum()
        dff.plot(kind='bar', legend=True, ax=axf)
        axf.set_title('Stages Vs. Score')

        window.mainloop()



##a = Accountdetails('admin','password','Germanstagedisplay')

##        fig = Figure()##figsize = (3, 3),dpi = 90
##  
##        # list of squares
##        y = [5,5,5,5]
##      
##        # adding the subplot
##        plot1 = fig.add_subplot(111)
##      
##        # plotting the graph
##        plot1.plot(y)
##      
##        # creating the Tkinter canvas
##        # containing the Matplotlib figure
##        canvas = FigureCanvasTkAgg(fig,
##                                   master = germanframe)  
##        canvas.draw()
##      
##        # placing the canvas on the Tkinter window
##        canvas.get_tk_widget().place(x=50, y=50)
##      
####        # creating the Matplotlib toolbar
####        toolbar = NavigationToolbar2Tk(canvas,
####                                       germanframe)
####        toolbar.update()
####      
####        # placing the toolbar on the Tkinter window
####        canvas.get_tk_widget().pack()
##       
        

        
        ##img_frame = Frame(user_detail_frame, width=200, height=200, background='grey')
        ##img_frame.place(x=30, y=100)
        
##        btn4 = Button(score_frame, text="Score", border=5, width=8, command=window.destroy)
##        btn4.place(x=550, y=180)
          
##        user_name = Label(score_frame, text="Hi "+self.username+"!", font=("Times New Roman", 35))
##        user_name.place(x=50, y=90)
##        
##        user_email = Label(score_frame, text=self.email, font=("Arial Bold", 15))
##        user_email.place(x=50, y=150)
##        
##        user_phone = Label(score_frame, text=self.phone, font=("Times New Roman", 15))
##        user_phone.place(x=50, y=180)
##
##        user_address = Label(score_frame, text=self.address, font=("Times New Roman", 15))
##        user_address.place(x=50, y=210)

        
        
        



##def openImage():
##
##    global op_img
##    window.filename = filedialog.askopenfilename(initialdir="\Downloads\sbv", title="Select File",
##                                                 filetypes=(("jpg files", "*.jpg"), ("All files", "*.*")))
##    op_img = ImageTk.PhotoImage(Image.open(window.filename).resize((180, 180)))
##    Label(image=op_img).place(x=80, y=150)


# menubar = Menu(window, background="blue")
# file = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Home', menu=file)
# menubar.add_command(label="X", command=window.destroy, )

# window.config(menu=menubar)
# file.add_command(label="New File", command=None)
# file.add_separator()
# file.add_command(label="Exit")
#
#     s1 = d1.get()
#     s2 = d2.get()
#     s3 = d3.get()
#
#     if s1 == "" or s2 == "" or s3 == "":
#         messagebox.showwarning("Warning!!", "Field cannot be blank")
#     elif s2 != s3:
#         messagebox.showerror("Error", "Password don't match")
#     else:
#         try:
#             value = (s1, s2)



# def delete():
#     # sql = "delete from login_details (usr,psd) values (%s %s)"
#
#             messagebox.showinfo("Success", "Deleted Successfully")
#         except Exception as e:
#             messagebox.showerror("Duplicate user", "Invalid User!")


# def saveDetails():
#     sql = "update log_details set usernam"


# def insert():
#     sql = "insert into user_details (usr,psd) values (%s,%s)"
#     s1 = e1.get()
#     s2 = e2.get()
#     s3 = e3.get()
#     s4 = e4.get()
#     if s1 == "" or s2 == "" or s3 == "" or s4 == "":
#         messagebox.showwarning("Warning!!", "Fields cannot be left blank")
#     elif s2 != s3:
#         messagebox.showerror("Error", "Passwords do not match")
#     else:
#         try:
#             val = (s1, s2)
#             c.execute(sql, val)
#             mydb.commit()
#             messagebox.showinfo("Success", "Registration Successfull")
#         except Exception as e:
#             messagebox.showerror("Duplicate user ", "Username already exist")
#






##canvas = Canvas(img_frame, width=180, height=180, bg="gray16")
##user_image = Image.open("C:\\Users\\anshe\\Downloads\sbv\\background_img_car.jpg")
##resize_img = user_image.resize((180, 180))
##user_img = ImageTk.PhotoImage(resize_img)
##canvas.create_image(0, 0, anchor=NW, image=user_img)
##canvas.pack()


##edit_img_frame = Frame(edit_details_frame, width=180, height=180)
##edit_img_frame.place(x=30, y=100)

##canvas = Canvas(edit_img_frame, width=180, height=180)
##edit_image = Image.open("C:\\Users\\anshe\\Downloads\sbv\\background_img_car.jpg")
##resize_img = edit_image.resize((180, 180))
##edited_img = ImageTk.PhotoImage(resize_img)
##canvas.create_image(0, 0, anchor=NW, image=edited_img)
##canvas.pack()



##btn3 = Button(edit_details_frame, text="Change Image", border=5, command=openImage)
##btn3.place(x=70, y=300)


