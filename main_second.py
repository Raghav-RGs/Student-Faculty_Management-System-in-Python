
from tkinter import *
from std_login import *
from admin_login import *

from fac_login import *



def main():
    def S():
        mw.wm_withdraw()
        SDL_main()
        mw.wm_deiconify()
        mw.destroy()
    def A():
        mw.wm_withdraw()
        ADL_main()
        mw.wm_deiconify()
        mw.destroy()
    def F():
        mw.wm_withdraw()
        FCL_main()
        mw.wm_deiconify()
        mw.destroy()

    mw= Tk()
    mw.title("Login")
    mw.geometry("600x400+450+200")
    mw.minsize(600, 400)
    mw.maxsize(600, 400)

    heading = Label(mw, text=" Choose Login ", font=('Calibri', 36), border=1)
    heading.grid(row=0, column=0)
    heading.place(x=180, y=50)
    #st=PhotoImage(file="std.png")
    #std=st.subsample(1,1)
    btn = Button(mw,text="Student", command=S,font=('arial',13,'bold'),borderwidth=5)
    btn.grid(row=2, column=0, padx=50, pady=10)
    btn.place(x=100, y=250)
    #ad = PhotoImage(file="admin.png")
    #adm = ad.subsample(1,1)
    btn = Button(mw, text="Admin", command=A,font=('arial',13,'bold'),borderwidth=5)
    btn.grid(row=4, column=0, padx=50, pady=10)
    btn.place(x=250, y=250)
    #fac = PhotoImage(file="fac.png")
    #facty = fac.subsample(1,1)
    btn = Button(mw,text="Faculty", command=F,font=('arial',13,'bold'),borderwidth=5)
    btn.grid(row=6, column=0, padx=50, pady=10)
    btn.place(x=390, y=250)
    mw.mainloop()


