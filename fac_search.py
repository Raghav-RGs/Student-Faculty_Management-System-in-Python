from tkinter import *
from tkinter import messagebox
import mysql.connector

def search_fac(pr_win):

    def search():
        check=False

        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="",
                                      database="studentdb")
        if (con):
            #pr_win.wm_iconbitmap("conn.ico")
            #messagebox.showinfo("MYSQL", message="Connection Done!")
            cur = con.cursor()
            #print(ID)
            ID=ename.get()
            qry = 'select * from faculty'
            cur.execute(qry)
            Mrows = cur.fetchall()
            con.commit()

            for rows in Mrows:
                if rows[0]==ID:
                    #print(rows)
                    #pw.wm_iconbitmap("conn.ico")
                    #messagebox.showinfo("MYSQL", message="ID Found")
                    data=list(rows)
                    check=True
                    break
            if check==True:


                lbRoll = Label(pw, text="User ID : ", font=18, fg='black')
                Roll = Label(pw, text=data[0], font=18, fg='black')
                lbname = Label(pw, text="Name : ", font=18, fg='black')
                name = Label(pw, text=data[1] +' '+data[2], font=18, fg='black')
                lbBr = Label(pw, text="Branch : ", font=18, fg='black')
                Br= Label(pw, text=data[3], font=18, fg='black')
                lbSem = Label(pw, text="Semester : ", font=18, fg='black')
                Sem=Label(pw, text=data[7]+' th', font=18, fg='black')
                lbSec = Label(pw, text="Section : ", font=18, fg='black')
                Sec = Label(pw, text=data[4], font=18, fg='black')
                lbSub = Label(pw, text="Subject : ", font=18, fg='black')
                Sub = Label(pw, text=data[5], font=18, fg='black')
                lbCity = Label(pw, text="City : ", font=18, fg='black')
                City = Label(pw, text=data[8], font=18, fg='black')

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
                lbSub.grid(row=5, column=0, padx=10, pady=15)
                Sub.grid(row=5, column=1, padx=10, pady=15)
                lbCity.grid(row=6, column=0, padx=10, pady=15)
                City.grid(row=6, column=1, padx=10, pady=15)


    #----------Place--------------------------------------------------------------------
                lbRoll.place(x=30,y=150)
                Roll.place(x=160, y=150)

                lbname.place(x=30, y=175)
                name.place(x=160, y=175)
                lbBr.place(x=30, y=200)
                Br.place(x=160, y=200)
                lbSem.place(x=30, y=225)
                Sem.place(x=160, y=225)
                lbSec.place(x=30, y=250)
                Sec.place(x=160, y=250)
                lbSub.place(x=30, y=275)
                Sub.place(x=160, y=275)
                lbCity.place(x=30, y=300)
                City.place(x=160, y=300)
                btn=Button(pw,text='Close',command=pw.destroy,font=('arial',13,'bold'),border=5)
                btn.grid(row=10,column=2,padx=10,pady=15)
                btn.place(x=360,y=330)
            else:
                pw.wm_iconbitmap("error.ico")
                messagebox.showinfo("MYSQL", message="ID does't exist")
#----------------------------------------------------------------------------------------------------
        else:
            pw.wm_iconbitmap("error.ico")
            messagebox.showinfo("MYSQL", message="Connection Failed!")
    pw = Toplevel(pr_win)
    pw.title('Search')
    pw.geometry("600x400+450+200")
    heading = Label(pw, text=" Search Details", font=('Calibri', 36), border=1)
    heading.grid(row=0, column=0)
    heading.place(x=180, y=20)
    lbname = Label(pw, text="Faculty ID : ", font=18, fg='black')
    ename = Entry(pw, border=3, width=25)
    btn = Button(pw, text='Search',border=5, font=('arial', 13, 'bold'), command=search)
    lbname.grid(row=0, column=0, padx=10, pady=10)
    ename.grid(row=0, column=1, padx=10, pady=10)
    btn.grid(row=0, column=1, padx=10, pady=10)
    lbname.place(x=120, y=100)
    ename.place(x=235, y=100)
    btn.place(x=405, y=90)