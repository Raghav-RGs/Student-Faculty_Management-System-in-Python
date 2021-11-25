from tkinter import *
from tkinter import messagebox
import mysql.connector


def fac_upd(pr_win):
    def clearall():
        Roll.delete(0, END)
        fname.delete(0, END)
        lname.delete(0, END)
        Br.delete(0, END)
        Sem.delete(0, END)
        Sec.delete(0, END)
        Sub.delete(0, END)
        City.delete(0, END)
        passw.delete(0, END)
    def insert_fa():

        id = Roll.get()
        Fname = fname.get()
        Lname = lname.get()
        br = Br.get()
        sem = Sem.get()
        sec = Sec.get()
        sub = Sub.get()
        city = City.get()
        passwd = passw.get()



        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="",
                                      database="studentdb")

        if (con):

            # pw.wm_iconbitmap("conn.ico")
            # messagebox.showinfo("MYSQL", message="Connection Done!")
            cur = con.cursor(prepared=True);
            pre_qry = "update faculty set ID=%s,F_name=%s,L_name=%s,Branch=%s,Section=%s,Subject=%s,password=%s,Semester=%s,City=%s where ID=%s"
            cur.execute(pre_qry, (id, Fname, Lname, br, sec, sub, passwd, sem, city,id))
            con.commit()
            if cur.rowcount != 0:
                try:

                    pw.wm_iconbitmap("conn.ico")
                    messagebox.showinfo("Update info", "Profile Updated")
                    clearall()
                    pw.destroy()
                except:
                    pw.wm_iconbitmap("error.ico")
                    messagebox.showinfo("Update info", "Cannot insert these values")
                    clearall()
                    pw.destroy()
            else:
                pw.wm_iconbitmap("error.ico")
                messagebox.showinfo("Update info", "ID not found")
                clearall()
                pw.destroy()



        else:
            pw.wm_iconbitmap("error.ico")
            messagebox.showinfo("Mysql", messagebox="Connection Failed!")

    pw = Toplevel(pr_win)
    pw.title('Update Faculty Profiles')
    pw.geometry("600x400+450+200")
    heading = Label(pw, text=" UPDATE FACULTY PROFILE", font=('Calibri', 36))
    heading.grid(row=0, column=0)
    heading.place(x=150, y=10)

    lbRoll = Label(pw, text="User ID : ", font=18)
    Roll = Entry(pw, border=3, width=25)
    lbname = Label(pw, text="First Name : ", font=18)
    fname = Entry(pw, border=3, width=25)
    lblname = Label(pw, text="Last Name : ", font=18)
    lname = Entry(pw, border=3, width=25)
    lbBr = Label(pw, text="Branch : ", font=18)
    Br = Entry(pw, border=3, width=25)
    lbSem = Label(pw, text="Semester : ", font=18)
    Sem = Entry(pw, border=3, width=25)
    lbSec = Label(pw, text="Section : ", font=18)
    Sec = Entry(pw, border=3, width=25)
    lbSub = Label(pw, text="Subject : ", font=18)
    Sub = Entry(pw, border=3, width=25)
    lbCity = Label(pw, text="City : ", font=18)
    City = Entry(pw, border=3, width=25)
    lbpassw = Label(pw, text="Password : ", font=18)
    passw = Entry(pw, border=3, width=25)

    # --------- Grid Placement ------------------------------------------------------------------------

    lbRoll.grid(row=0, column=0, padx=10, pady=10)
    Roll.grid(row=0, column=1, padx=10, pady=10)
    lbname.grid(row=1, column=0, padx=10, pady=15)
    fname.grid(row=1, column=1, padx=10, pady=15)
    lblname.grid(row=2, column=0, padx=10, pady=15)
    lname.grid(row=2, column=1, padx=10, pady=15)
    lbBr.grid(row=3, column=0, padx=10, pady=15)
    Br.grid(row=3, column=1, padx=10, pady=15)
    lbSem.grid(row=4, column=0, padx=10, pady=15)
    Sem.grid(row=4, column=1, padx=10, pady=15)
    lbSec.grid(row=5, column=0, padx=10, pady=15)
    Sec.grid(row=5, column=1, padx=10, pady=15)
    lbSub.grid(row=6, column=0, padx=10, pady=15)
    Sub.grid(row=6, column=1, padx=10, pady=15)
    lbCity.grid(row=7, column=0, padx=10, pady=15)
    City.grid(row=7, column=1, padx=10, pady=15)
    lbpassw.grid(row=8, column=0, padx=10, pady=15)
    passw.grid(row=8, column=1, padx=10, pady=15)

    # ----------Place--------------------------------------------------------------------
    lbRoll.place(x=30, y=80)
    Roll.place(x=160, y=80)

    lbname.place(x=30, y=105)
    fname.place(x=160, y=105)
    lblname.place(x=30, y=130)
    lname.place(x=160, y=130)
    lbBr.place(x=30, y=155)
    Br.place(x=160, y=155)
    lbSem.place(x=30, y=180)
    Sem.place(x=160, y=180)
    lbSec.place(x=30, y=205)
    Sec.place(x=160, y=205)
    lbSub.place(x=30, y=230)
    Sub.place(x=160, y=230)
    lbCity.place(x=30, y=255)
    City.place(x=160, y=255)
    lbpassw.place(x=30, y=280)
    passw.place(x=160, y=280)
    btn = Button(pw, text='ADD', command=insert_fa, font=('arial', 13, 'bold'), border=5)
    btn.grid(row=10, column=2, padx=10, pady=15)
    btn.place(x=260, y=330)
    btn1 = Button(pw, text='Clear all', command=clearall, font=('arial', 13, 'bold'), border=5)
    btn1.grid(row=10, column=4, padx=10, pady=15)
    btn1.place(x=360, y=330)
