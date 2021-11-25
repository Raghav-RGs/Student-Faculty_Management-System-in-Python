from tkinter import *
from tkinter import messagebox
from tkinter import Menu
import mysql.connector
import faculty_add
import fac_update
import admin_delete
import admin_add
import fac_delete
import fac_search
import std_add
import std_update
import std_delete
import std_search

import help_site
import about_project

def main(ID):
    def help():
        help_site.main()
    def add_adm():
        admin_add.add_admin(pr_win)
    def del_adm():
        admin_delete.delete_ad(pr_win)


    def fac_add():
        faculty_add.faculty_add(pr_win)
    def fac_upd():
        fac_update.fac_upd(pr_win)
    def fac_del():
        fac_delete.delete_fac(pr_win)
    def fac_srh():
        fac_search.search_fac(pr_win)


    def st_add():
        std_add.add_std(pr_win)
    def st_upd():
        std_update.upd_std(pr_win)
    def st_del():
        std_delete.delete_std(pr_win)
    def st_srh():
        std_search.search_std(pr_win)



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


                qry = 'select * from admin'
                passw=ename.get()
                cur.execute(qry)

                Mrows = cur.fetchall()
                con.commit()

                cur.close()

                for rows in Mrows:
                    if rows[0] == ID:
                        print(rows)
                        data = list(rows)
                        break
                def set():
                    npass = epass.get()
                    cn = con.cursor(prepared=True)
                    qy = 'Update admin SET password=%s where Username=%s'
                    cn.execute(qy,(npass,ID))
                    con.commit()
                    if cn.rowcount!=0:
                        pw.wm_iconbitmap("conn.ico")
                        messagebox.showinfo("Update info", "Password Changed")
                        epass.delete(0, END)
                        pw.destroy()
                    else:
                        pw.wm_iconbitmap("error.ico")
                        messagebox.showinfo("Update info", "NO Change")
                        epass.delete(0,END)
                        pw.destroy()

                if data[1]==str(passw):
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

    def donothing():
        pass

    def about():
        about_project.main()




#-----------------------------------------------------------------------------------------------------------------------------------------
# Main Body
    pr_win =Tk()
    pr_win.title("Admin Profile")
    pr_win.geometry("600x400+450+200")
    pr_win.minsize(600, 400)
    pr_win.maxsize(800, 800)

#-----------------------------------------------------------------------------------------------
# Menu Body Starts

    menubar = Menu(pr_win)
    admenu=Menu(menubar,tearoff=0)
    admenu.add_command(label="Add Admin",command=add_adm)
    admenu.add_separator()
    admenu.add_command(label="Delete Admin", command=del_adm)
    admenu.add_separator()
    admenu.add_command(label="Close", command=pr_win.quit)
    menubar.add_cascade(label="Admin",menu=admenu)
#---------------------------------------------------------------------------------------
    msmenu = Menu(menubar, tearoff=0)
    msmenu.add_command(label="Add Faculty", command=fac_add)

    msmenu.add_separator()

    msmenu.add_command(label="Update Profile", command=fac_upd)
    msmenu.add_separator()
    msmenu.add_command(label="Delete Profile", command=fac_del)
    msmenu.add_separator()
    msmenu.add_command(label="Search Details", command=fac_srh)
    msmenu.add_separator()
    msmenu.add_command(label='Close', command=pr_win.quit)
    menubar.add_cascade(label="Faculty", menu=msmenu)

#--------------------------------------------------------------------------------------

    st_menu = Menu(menubar, tearoff=0)
    st_menu.add_command(label="Add Student", command=st_add)

    st_menu.add_separator()

    st_menu.add_command(label="Update Profile", command=st_upd)
    st_menu.add_separator()
    st_menu.add_command(label="Delete Profile", command=st_del)
    st_menu.add_separator()
    st_menu.add_command(label="Search Details", command=st_srh)
    st_menu.add_separator()
    st_menu.add_command(label='Close', command=pr_win.quit)
    menubar.add_cascade(label="Student", menu=st_menu)

#--------------------------------------------------------------------------------------------

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='Change Password', command=ch_pas)
    filemenu.add_command(label='Close', command=pr_win.quit)

    menubar.add_cascade(label='Setting', menu=filemenu)
    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label='Visit Site',command=help)
    menubar.add_cascade(label='Help',menu=helpmenu)

    aboutmenu=Menu(menubar,tearoff=0)
    aboutmenu.add_command(label='About Project',command=about)
    menubar.add_cascade(label='About',menu=aboutmenu)
    pr_win.config(menu=menubar)
    pr_win.configure(background='blue')

#Menu Body Ended
#------------------------------------------------------------------------------------------------
#Welcome Admin Body
    lbl=Label(pr_win,text='Welcome Admin',font=('arial',44,'bold'),background="Blue")

    lbl.grid(row=0,column=0)

    lbl.place(x=130,y=50)

    exp="""    This is a admin page from 
    where you can perform various 
    task related to student and 
    faculty.
     
    To add or delete new
    admin the superadmin password is 
    required. 
    
    The Superadmin Username is Raghav
    
    For Further help ,click on Help.
    To know about project ,click on About
    """
    lbl2 = Label(pr_win, text=exp,anchor=CENTER ,justify=LEFT,font=('arial',24, 'bold'), background="Blue")
    lbl2.grid(row=0,column=0,padx=10,pady=10)
    lbl2.place(x=5,y=150)

    pr_win.mainloop()

