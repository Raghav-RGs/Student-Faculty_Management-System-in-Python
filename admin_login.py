from tkinter import *
from tkinter import messagebox
import mysql.connector
import admin_page

def ADL_main():

        def std_login():
            check = False
            name = ename.get()
            passw = epass.get()

            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="",
                                          database="studentdb")

            if (con):

                #sw.wm_iconbitmap("conn.ico")
                #messagebox.showinfo("MYSQL", message="Connection Done!")
                cur = con.cursor()
                qry = "select *from admin"
                cur.execute(qry)
                Mrows = cur.fetchall()
                con.commit()
                check=False
                empty=False
                if name == '' or passw == '':
                    sw.wm_iconbitmap("conn.ico")
                    messagebox.showinfo("Login", message="Field is Empty")
                    empty=True
                for rows in Mrows:

                    #print("username:", rows[0])
                    #print("passw:", rows[1])



                    if name == rows[0] and passw == rows[1] and empty==False:
                        print("valid user and password")
                        sw.wm_iconbitmap("conn.ico")
                        messagebox.showinfo("Login", message="Login Successfull")
                        ename.delete(0, END)
                        epass.delete(0, END)
                        check=True
                        sw.wm_withdraw()
                        admin_page.main(rows[0])
                        sw.wm_deiconify()



                if check==False and empty==False:
                        sw.wm_iconbitmap("error.ico")
                        print('invalid user',rows[0],rows[1])
                        messagebox.showinfo("Login", message="Login Failed")
                        ename.delete(0, END)
                        epass.delete(0, END)

                        con.close()

            else:
                sw.wm_iconbitmap("error.ico")
                messagebox.showinfo("Mysql", messagebox="Connection Failed!")


        sw = Tk()

        sw.title("Admin Login")
        sw.geometry("600x400+450+200")
        sw.minsize(600, 400)
        sw.maxsize(600, 400)

        heading = Label(sw,text=" Admin Login ",font=('Calibri',36),border=1)
        heading.grid(row=0,column=0)
        heading.place(x=180,y=50)
        lbname = Label(sw, text="Username : ", font=18, fg='black')
        ename = Entry(sw,border=3,width=25)
        lbpass = Label(sw, text="Password : ", font=18, fg='black')
        epass = Entry(sw, show="*",border=3,width=25)
        lbname.grid(row=0, column=0, padx=10, pady=100)
        ename.grid(row=0, column=1, padx=100, pady=100)
        lbpass.grid(row=1, column=0, padx=100, pady=20)
        epass.grid(row=1, column=1, padx=10, pady=20)
        lbname.place(x=180, y=150)
        ename.place(x=285, y=154)
        lbpass.place(x=180, y=200)
        epass.place(x=285, y=204)
        btn = Button(sw, text="Log in", command=std_login,font=('arial',13,'bold'),borderwidth=5)
        btn.grid(row=2, column=0, padx=50, pady=10)
        btn.place(x=280, y=250)
        sw.mainloop()

