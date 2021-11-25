from tkinter import *
from tkinter import messagebox
import mysql.connector
def add_admin(pr_win):
    def insert_Ad():

        name = ename.get()
        passw = epass.get()

        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="",
                                      database="studentdb")

        if (con):

            # pw.wm_iconbitmap("conn.ico")
            # messagebox.showinfo("MYSQL", message="Connection Done!")
            try:
                cur = con.cursor(prepared=True);
                pre_qry = "insert into admin values(%s,%s)"
                cur.execute(pre_qry, (name, passw))
                con.commit()
                if cur.rowcount != 0:

                        pw.wm_iconbitmap("conn.ico")
                        messagebox.showinfo("Update info", "Insertion Done")
                        epass.delete(0, END)
                        pw.destroy()
                else:
                    pw.wm_iconbitmap("error.ico")
                    messagebox.showinfo("Update info", "NO Insertion")
                    epass.delete(0, END)
                    pw.destroy()
            except:
                    pw.wm_iconbitmap("error.ico")
                    messagebox.showinfo("Update info", "NO Insertion")
                    epass.delete(0, END)
                    pw.destroy()




        else:
            pw.wm_iconbitmap("error.ico")
            messagebox.showinfo("Mysql", messagebox="Connection Failed!")

    pw = Toplevel(pr_win)
    pw.title('Add Admin')
    pw.geometry("600x400+450+200")
    heading = Label(pw, text="ADD NEW ADMIN", font=('Calibri', 36), border=1)
    heading.grid(row=0, column=0)
    heading.place(x=180, y=50)
    lbname = Label(pw, text="Username : ", font=18, fg='black')
    ename = Entry(pw, border=3, width=25)
    lbpass = Label(pw, text="Password : ", font=18, fg='black')
    epass = Entry(pw, show="*", border=3, width=25)
    lbname.grid(row=0, column=0, padx=10, pady=100)
    ename.grid(row=0, column=1, padx=100, pady=100)
    lbpass.grid(row=1, column=0, padx=100, pady=20)
    epass.grid(row=1, column=1, padx=10, pady=20)
    lbname.place(x=180, y=150)
    ename.place(x=285, y=154)
    lbpass.place(x=180, y=200)
    epass.place(x=285, y=204)
    btn = Button(pw, text="ADD", command=insert_Ad, font=('arial', 13, 'bold'), borderwidth=5)
    btn.grid(row=2, column=0, padx=50, pady=10)
    btn.place(x=280, y=250)
