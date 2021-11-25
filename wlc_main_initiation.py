import turtle
import tkinter
import main_second



def welcome():

    root=tkinter.Tk()
    root.title("Welcome")
    root.geometry("600x600+450+200")
    root.maxsize(600,600)
    root.minsize(600,600)

    Canvas=tkinter.Canvas(root,bg='Black',width=600 , height=600)

    Canvas.pack()


    colors = ['purple', 'Red', 'orange', 'blue', 'green', 'yellow']
    t =turtle.RawTurtle(Canvas)
    p =turtle.RawTurtle(Canvas)
    #title('Welcome')
    #screensize(600,400)
    #bgcolor('black')
    p.pencolor(colors[3])
    p.up()
    t.penup()
    t.goto(0,-100)
    p.goto(-250,150)
    p.down()


    count = 0
    t.speed(20)
    p.hideturtle()
    t.speed(20)
    t.pendown()
    t.hideturtle()
    for x in range(200):
        t.pencolor(colors[x % 5])
        t.pensize(x / 100 + 1)
        t.forward(x)
        t.left(59)

    p.speed(-10)
    for x in range(20):
        p.color(colors[x % 6])

        p.write(" WELCOME ", False, font=('Arial', 68, 'normal'))

    root.wm_withdraw()
    main_second.main()
    root.wm_deiconify()
    root.destroy()
welcome()




