from tkinter import *
from tkinter import messagebox
import mysql.connector

def upd_std(pr_win):
    def clearall():

        Roll.delete(0,END)
        name.delete(0, END)
        passd.delete(0, END)
        Br.delete(0, END)
        Sem.delete(0, END)
        Sec.delete(0, END)
        Add.delete(0, END)
        City.delete(0, END)
        Fees.delete(0, END)
        Email.delete(0, END)
        Att.delete(0, END)

    def insert_std():
        iD=Roll.get()
        Name=(name.get()).split()
        Passd=passd.get()
        br=Br.get()
        sem=Sem.get()
        sec=Sec.get()
        add=Add.get()
        city=City.get()
        fees=Fees.get()
        mail=Email.get()
        att=Att.get()

        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="",
                                      database="studentdb")

        if (con):

            # pw.wm_iconbitmap("conn.ico")
            # messagebox.showinfo("MYSQL", message="Connection Done!")

            try:
                cur = con.cursor(prepared=True);
                pre_qry = "update student set ID=%s,password=%s,F_name=%s,L_name=%s,Branch=%s,semester=%s,Section=%s,address=%s,city=%s,fees=%s,Email=%s,Attendance=%s where ID=%s"
                cur.execute(pre_qry, (iD,Passd,Name[0],Name[1],br,sem,sec,add,city,fees,mail,att,iD))
                con.commit()


                if cur.rowcount != 0:

                        pw.wm_iconbitmap("conn.ico")
                        messagebox.showinfo("Update info", "Profile Updated")
                        clearall()
                        pw.destroy()
                else:
                    pw.wm_iconbitmap("error.ico")
                    messagebox.showinfo("Update info", "ID not found")
                    clearall()
                    pw.destroy()
            except:
                    pw.wm_iconbitmap("error.ico")
                    messagebox.showinfo("Update info", "Cannot insert these values")
                    clearall()
                    pw.destroy()




        else:
            pw.wm_iconbitmap("error.ico")
            messagebox.showinfo("Mysql", messagebox="Connection Failed!")

    pw = Toplevel(pr_win)
    pw.title('Add Faculty')
    pw.geometry("600x400+450+200")
    heading = Label(pw, text=" ADD NEW STUDENT", font=('Calibri', 36))
    heading.grid(row=0, column=0)
    heading.place(x=150, y=10)
    lbRoll = Label(pw, text="Enrollment No : ", font=18)
    Roll = Entry(pw, width=25,border=3)
    lbname = Label(pw, text="Name : ", font=18)
    name = Entry(pw, width=25,border=3)
    lblpass = Label(pw, text="Password : ", font=18)
    passd = Entry(pw, width=25,border=3)
    lbBr = Label(pw, text="Branch : ", font=18)
    Br= Entry(pw, width=25,border=3)
    lbSem = Label(pw, text="Semester : ", font=18)
    Sem=Entry(pw,  width=25,border=3)
    lbSec = Label(pw, text="Section : ", font=18)
    Sec = Entry(pw,  width=25,border=3)
    lbAdd = Label(pw, text="Address : ", font=18)
    Add = Entry(pw,  width=25,border=3)
    lbCity = Label(pw, text="City : ", font=18)
    City = Entry(pw, width=25,border=3)
    lbFees = Label(pw, text="Fees Status : ", font=18)
    Fees = Entry(pw, width=25,border=3)
    lbEmail = Label(pw, text="Email ID : ", font=18)
    Email = Entry(pw, width=25,border=3)
    lbAtt = Label(pw, text="Attendance : ", font=18)
    Att = Entry(pw, width=25,border=3)

    #--------- Grid Placement ------------------------------------------------------------------------

    lbRoll.grid(row=0, column=0, padx=10, pady=10)
    Roll.grid(row=0, column=1, padx=10, pady=10)
    lbname.grid(row=1, column=0, padx=10, pady=15)
    name.grid(row=1, column=1, padx=10, pady=15)
    lblpass.grid(row=2, column=0, padx=10, pady=15)
    passd.grid(row=2, column=1, padx=10, pady=15)
    lbBr.grid(row=3, column=0, padx=10, pady=15)
    Br.grid(row=3, column=1, padx=10, pady=15)
    lbSem.grid(row=4, column=0, padx=10, pady=15)
    Sem.grid(row=4, column=1, padx=10, pady=15)
    lbSec.grid(row=5, column=0, padx=10, pady=15)
    Sec.grid(row=5, column=1, padx=10, pady=15)
    lbAdd.grid(row=6, column=0, padx=10, pady=15)
    Add.grid(row=6, column=1, padx=10, pady=15)
    lbCity.grid(row=7, column=0, padx=10, pady=15)
    City.grid(row=7, column=1, padx=10, pady=15)
    lbFees.grid(row=8, column=0, padx=10, pady=15)
    Fees.grid(row=8, column=1, padx=10, pady=15)
    lbEmail.grid(row=9, column=0, padx=10, pady=15)
    Email.grid(row=9, column=1, padx=10, pady=15)
    lbAtt.grid(row=10, column=0, padx=10, pady=15)
    Att.grid(row=10, column=1, padx=10, pady=15)

    #----------Place--------------------------------------------------------------------
    lbRoll.place(x=30,y=80)
    Roll.place(x=160, y=80)
    lbname.place(x=30, y=105)
    name.place(x=160, y=105)
    lblpass.place(x=30, y=130)
    passd.place(x=160, y=130)
    lbBr.place(x=30, y=155)
    Br.place(x=160, y=155)
    lbSem.place(x=30, y=180)
    Sem.place(x=160, y=180)
    lbSec.place(x=30, y=205)
    Sec.place(x=160, y=205)
    lbAdd.place(x=30, y=230)
    Add.place(x=160, y=230)
    lbCity.place(x=30, y=255)
    City.place(x=160, y=255)
    lbFees.place(x=30,y=280)
    Fees.place(x=160, y=280)
    lbEmail.place(x=30, y=305)
    Email.place(x=160, y=305)
    lbAtt.place(x=30, y=330)
    Att.place(x=160, y=330)
    btn=Button(pw,text='Close',command=pw.destroy,font=('arial',13,'bold'),border=5)
    btn.grid(row=10,column=4,padx=10,pady=15)
    btn.place(x=460,y=330)
    btn = Button(pw, text='Add', command=insert_std, font=('arial', 13, 'bold'), border=5)
    btn.grid(row=10, column=3, padx=10, pady=15)
    btn.place(x=360, y=330)

