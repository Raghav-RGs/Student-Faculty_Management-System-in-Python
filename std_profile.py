from tkinter import *
from tkinter import messagebox
from tkinter import Menu
import mysql.connector
import help_site
import about_project

def main(ID):
    def profile(pr_win,ID):
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="",
                                      database="studentdb")
        if (con):
            #pr_win.wm_iconbitmap("conn.ico")
            #messagebox.showinfo("MYSQL", message="Connection Done!")
            cur = con.cursor()
            #print(ID)
            ID=str(ID)
            qry = 'select * from student'
            cur.execute(qry)
            Mrows = cur.fetchall()
            con.commit()

            for rows in Mrows:
                if rows[0]==ID:
                    #print(rows)
                    data=list(rows)
                    break

            heading = Label(pr_win, text=" Student Profile ", font=('Calibri', 36),bg='blue')
            heading.grid(row=0, column=0)
            heading.place(x=150, y=10)

            lbRoll = Label(pr_win, text="Enrollment No : ", font=18, fg='black',bg='blue')
            Roll = Label(pr_win, text=data[0], font=18, fg='black',bg='blue')
            lbname = Label(pr_win, text="Name : ", font=18, fg='black',bg='blue')
            name = Label(pr_win, text=data[2] +' '+data[3], font=18, fg='black',bg='blue')
            lbBr = Label(pr_win, text="Branch : ", font=18, fg='black',bg='blue')
            Br= Label(pr_win, text=data[4], font=18, fg='black',bg='blue')
            lbSem = Label(pr_win, text="Semester : ", font=18, fg='black',bg='blue')
            Sem=Label(pr_win, text=data[5]+' th', font=18, fg='black',bg='blue')
            lbSec = Label(pr_win, text="Section : ", font=18, fg='black',bg='blue')
            Sec = Label(pr_win, text=data[6], font=18, fg='black',bg='blue')
            lbAdd = Label(pr_win, text="Address : ", font=18, fg='black',bg='blue')
            Add = Label(pr_win, text=data[7], font=18, fg='black',bg='blue')
            lbCity = Label(pr_win, text="City : ", font=18, fg='black',bg='blue')
            City = Label(pr_win, text=data[8], font=18, fg='black',bg='blue')
            lbFees = Label(pr_win, text="Fees Status : ", font=18, fg='black',bg='blue')
            Fees = Label(pr_win, text=data[9], font=18, fg='black',bg='blue')
            lbEmail = Label(pr_win, text="Email ID : ", font=18, fg='black',bg='blue')
            Email = Label(pr_win, text=data[10], font=18, fg='black',bg='blue')
            lbAtt = Label(pr_win, text="Attendance : ", font=18, fg='black',bg='blue')
            Att = Label(pr_win, text=str(data[11])+'%', font=18, fg='black',bg='blue')

#--------- Grid Placement ------------------------------------------------------------------------

            lbRoll.grid(row=0, column=0, padx=10, pady=10)
            Roll.grid(row=0, column=1, padx=10, pady=10)
            lbname.grid(row=1, column=0, padx=10, pady=15)
            name.grid(row=1, column=1, padx=10, pady=15)
            lbBr.grid(row=2, column=0, padx=10, pady=15)
            Br.grid(row=2, column=1, padx=10, pady=15)
            lbSem.grid(row=3, column=0, padx=10, pady=15)
            Sem.grid(row=3, column=1, padx=10, pady=15)
            lbSec.grid(row=4, column=0, padx=10, pady=15)
            Sec.grid(row=4, column=1, padx=10, pady=15)
            lbAdd.grid(row=5, column=0, padx=10, pady=15)
            Add.grid(row=5, column=1, padx=10, pady=15)
            lbCity.grid(row=6, column=0, padx=10, pady=15)
            City.grid(row=6, column=1, padx=10, pady=15)
            lbFees.grid(row=7, column=0, padx=10, pady=15)
            Fees.grid(row=7, column=1, padx=10, pady=15)
            lbEmail.grid(row=8, column=0, padx=10, pady=15)
            Email.grid(row=8, column=1, padx=10, pady=15)
            lbAtt.grid(row=9, column=0, padx=10, pady=15)
            Att.grid(row=9, column=1, padx=10, pady=15)

#----------Place--------------------------------------------------------------------
            lbRoll.place(x=30,y=80)
            Roll.place(x=160, y=80)

            lbname.place(x=30, y=105)
            name.place(x=160, y=105)
            lbBr.place(x=30, y=130)
            Br.place(x=160, y=130)
            lbSem.place(x=30, y=155)
            Sem.place(x=160, y=155)
            lbSec.place(x=30, y=180)
            Sec.place(x=160, y=180)
            lbAdd.place(x=30, y=205)
            Add.place(x=160, y=205)
            lbCity.place(x=30, y=230)
            City.place(x=160, y=230)
            lbFees.place(x=30,y=255)
            Fees.place(x=160, y=255)
            lbEmail.place(x=30, y=280)
            Email.place(x=160, y=280)
            lbAtt.place(x=30, y=305)
            Att.place(x=160, y=305)
            btn=Button(pr_win,text='LogOut',command=pr_win.destroy,font=('arial',13,'bold'),border=5)
            btn.grid(row=10,column=2,padx=10,pady=15)
            btn.place(x=260,y=330)
#------------------------------------------------------------------------------------

        else:
            pr_win.wm_iconbitmap("error.ico")
            messagebox.showinfo("MYSQL", message="Connection Failed!")

    def ch_pas():

        def check():

            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="",
                                          database="studentdb")
            if (con):
                # pr_win.wm_iconbitmap("conn.ico")
                # messagebox.showinfo("MYSQL", message="Connection Done!")
                cur = con.cursor()


                qry = 'select * from student'
                passw=ename.get()
                cur.execute(qry)
                print(passw)
                Mrows = cur.fetchall()
                con.commit()

                cur.close()

                for rows in Mrows:
                    if rows[0] == ID:
                        #print(rows)
                        data = list(rows)
                        break
                def set():
                    npass = epass.get()
                    cn = con.cursor(prepared=True)
                    qy = 'Update student SET Password=%s where ID=%s'
                    cn.execute(qy,(npass,ID))
                    con.commit()
                    if cn.rowcount!=0:
                        pw.wm_iconbitmap("conn.ico")
                        messagebox.showinfo("Update info", "Password Changed")
                        epass.delete(0,END)
                        pw.destroy()
                    else:
                        pw.wm_iconbitmap("conn.ico")
                        messagebox.showinfo("Update info", "NO Change")
                        epass.delete(0, END)
                        pw.destroy()

                if data[1]==passw:
                    lbpass = Label(pw, text="New Password : ", font=18, fg='black')
                    epass = Entry(pw, show="*", border=3, width=25)
                    btn1=Button(pw,text='Change',font=('arial',13,'bold'),border=5,command=set)
                    lbpass.grid(row=1, column=0, padx=100, pady=20)
                    epass.grid(row=1, column=1, padx=10, pady=20)
                    btn1.grid(row=2, column=1, padx=10, pady=20)
                    lbpass.place(x=100, y=250)
                    epass.place(x=250, y=254)
                    btn1.place(x=200, y=310)
                else:
                    pw.wm_iconbitmap("error.ico")
                    messagebox.showinfo("Update info", message="Wrong Password")
                    ename.delete(0,END)


        pw=Toplevel(pr_win)
        pw.title('Change password')
        pw.geometry("600x400+450+200")
        heading = Label(pw, text=" Change Password ", font=('Calibri', 36), border=1)
        heading.grid(row=0, column=0)
        heading.place(x=180, y=50)
        lbname = Label(pw, text="Current Password : ", font=18, fg='black')
        ename = Entry(pw,show='*' ,border=3, width=25)
        btn=Button(pw,text='Check',border=5,font=('arial',13,'bold'),command=check)
        lbname.grid(row=0, column=0, padx=10, pady=10)
        ename.grid(row=0, column=1, padx=10, pady=10)
        btn.grid(row=1,column=1,padx=10,pady=10)
        lbname.place(x=120, y=150)
        ename.place(x=285, y=150)
        btn.place(x=285, y=180)



    def about():
        about_project.main()
    def help():
        help_site.main()

    pr_win =Tk()
    pr_win.title("Student Profile")
    pr_win.geometry("600x400+450+200")
    pr_win.minsize(600, 400)
    pr_win.maxsize(600, 800)

    menubar = Menu(pr_win)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='Change Password', command=ch_pas)
    filemenu.add_command(label='Close', command=pr_win.quit)

    menubar.add_cascade(label='Student', menu=filemenu)
    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label='visit site',command=help)
    menubar.add_cascade(label='Help',menu=helpmenu)

    aboutmenu=Menu(menubar,tearoff=0)
    aboutmenu.add_command(label='About Project',command=about)
    menubar.add_cascade(label='About',menu=aboutmenu)
    pr_win.config(menu=menubar)

    pr_win.configure(background='blue')
    profile(pr_win,ID)
    pr_win.mainloop()

