from tkinter import*
from tkinter import messagebox
import mysql.connector

def delete_std(pr_win):

    def check():
        name = (ename.get(),)
        passw = epass.get()

        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="",
                                      database="studentdb")
        if (con):
            # pr_win.wm_iconbitmap("conn.ico")
            # messagebox.showinfo("MYSQL", message="Connection Done!")
            #print(name)
            if 'Raghav@123' == passw:
                cur = con.cursor(prepared=True)
                try:
                    qry = 'delete from student where ID=%s'

                    cur.execute(qry,name)
                    con.commit()
                    cur.close()
                    pw.wm_iconbitmap("conn.ico")
                    messagebox.showinfo("Update info", message="Deletion Done")
                    pw.destroy()
                except:
                    pw.wm_iconbitmap("error.ico")
                    messagebox.showinfo("Update info", message="Invalid Deletion")
                    pw.destroy()

            else:
                pw.wm_iconbitmap("error.ico")
                messagebox.showinfo("Update info", message="SuperAdmin Password is incorrect ")
                pw.destroy()

    pw = Toplevel(pr_win)
    pw.title('Delete Profile')
    pw.geometry("600x400+450+200")
    heading = Label(pw, text='Delete Student Profile', font=('Calibri', 36), border=1)
    heading.grid(row=0, column=0)
    heading.place(x=100, y=50)
    lbname = Label(pw, text="User ID : ", font=18, fg='black')
    ename = Entry(pw, border=3, width=25)
    btn = Button(pw, text='Delete', border=5, font=('arial', 13, 'bold'), command=check)
    lbname.grid(row=0, column=0, padx=10, pady=10)
    ename.grid(row=0, column=1, padx=10, pady=10)
    lbpass = Label(pw, text="SuperAdmin Password : ", font=18, fg='black')
    epass = Entry(pw, show="*", border=3, width=25)

    lbpass.grid(row=1, column=0, padx=100, pady=20)
    epass.grid(row=1, column=1, padx=10, pady=20)
    btn.grid(row=2, column=1, padx=10, pady=20)
    lbpass.place(x=100, y=250)
    epass.place(x=300, y=254)
    btn.place(x=200, y=310)

    lbname.place(x=120, y=150)
    ename.place(x=285, y=150)


