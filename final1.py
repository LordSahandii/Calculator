##Sahand's Final project for CS50

#Importing the tkinter library to design our calculator
from tkinter import *
#Opening the window
win = Tk()
win.title("Calculator")
win.geometry("320x300")
win.configure(background="blue")
E = Entry(win)
E.pack()
E.place(in_ = win , x = 150 , y = 20)


#defining functions to insert the numbers
def B1():
        E.insert(END, "1")
def B2():
        E.insert(END, "2")
def B3():
        E.insert(END, "3")
def B4():
        E.insert(END, "4")
def B5():
        E.insert(END, "5")
def B6():
        E.insert(END, "6")
def B7():
        E.insert(END, "7")
def B8():
        E.insert(END, "8")
def B9():
        E.insert(END, "9")
def B0():
        E.insert(END, "0")
def B00():
        E.insert(END, "00")

#functions for making the operations work
def turn_into_negative():
        s = E.get()
        E.delete(0, END)
        E.insert(END, str(-1 * int(s)))
def inputplus(x):

        x = list(x)
        b2=[]
        b3=x + list("+")
        i=0
        w=""
        while i<len(x):
            if b3[i]!="+":
                w=w+str(b3[i])
                while b3[i+1]!="+":
                    w=w+str(x[i+1])
                    i=i+1
                b2.append (w)
            w=""
            i=i+1
        return b2
def inputnegative(x):

        x = list(x)
        b2=[]
        b3=x + list("-")
        i=0
        w=""
        while i<len(x):
            if b3[i]!="-":
                w=w+str(b3[i])
                while b3[i+1]!="-":
                    w=w+str(x[i+1])
                    i=i+1
                b2.append (w)
            w=""
            i=i+1
        return b2

def inputdivider(x):

        x = list(x)
        b2=[]
        b3=x + list("/")
        i=0
        w=""
        while i<len(x):
            if b3[i]!="/":
                w=w+str(b3[i])
                while b3[i+1]!="/":
                    w=w+str(x[i+1])
                    i=i+1
                b2.append (w)
            w=""
            i=i+1
        return b2
def inputtimes(x):

        x = list(x)
        b2=[]
        b3=x + list("*")
        i=0
        w=""
        while i<len(x):
            if b3[i]!="*":
                w=w+str(b3[i])
                while b3[i+1]!="*":
                    w=w+str(x[i+1])
                    i=i+1
                b2.append (w)
            w=""
            i=i+1
        return b2
def inputpower(x):

        x = list(x)
        b2=[]
        b3=x + list("^")
        i=0
        w=""
        while i<len(x):
            if b3[i]!="^":
                w=w+str(b3[i])
                while b3[i+1]!="^":
                    w=w+str(x[i+1])
                    i=i+1
                b2.append (w)
            w=""
            i=i+1
        return b2
def inputradical(x):

        x = list(x)
        b2=[]
        b3=x + list("√")
        i=0
        w=""
        while i<len(x):
            if b3[i]!="√":
                w=w+str(b3[i])
                while b3[i+1]!="√":
                    w=w+str(x[i+1])
                    i=i+1
                b2.append (w)
            w=""
            i=i+1
        return b2
def remainder(x):

        x = list(x)
        b2=[]
        b3=x + list("b")
        i=0
        w=""
        while i<len(x):
            if b3[i]!="b":
                w=w+str(b3[i])
                while b3[i+1]!="b":
                    w=w+str(x[i+1])
                    i=i+1
                b2.append (w)
            w=""
            i=i+1
        return b2
def quotient(x):

        x = list(x)
        b2=[]
        b3=x + list("k")
        i=0
        w=""
        while i<len(x):
            if b3[i]!="k":
                w=w+str(b3[i])
                while b3[i+1]!="k":
                    w=w+str(x[i+1])
                    i=i+1
                b2.append (w)
            w=""
            i=i+1
        return b2




#defining functions to insert the operations
def plus():
        E.insert(END, "+")
def negative():
        E.insert(END, "-")
def times():
        E.insert(END, "*")
def divide():
        E.insert(END, "/")
def power():
        E.insert(END, "^")
def radical():
        E.insert(END, "√")
def remain():
        E.insert(END, "b")
def qu():
        E.insert(END, "k")
def clear():
        E.delete(0,END)
def clearg():
        x=E.get()
        x=list(x)
        m=len(x)
        E.delete(m-1,END)

#this function shows the operations in the header
def mosa():
        if "+" in list(E.get()):
                s = inputplus(list(E.get()))
                E.delete(0, END)
                E.insert(END,str(float(s[0]) + float(s[1])))
        if "-" in list(E.get()):
                s = inputnegative(list(E.get()))
                E.delete(0, END)
                E.insert(END,str(float(s[0]) - float(s[1])))
        if "*" in list(E.get()):
                s = inputtimes(list(E.get()))
                E.delete(0, END)
                E.insert(END,str(float(s[0]) * float(s[1])))
        if "/" in list(E.get()):
                s = inputdivider(list(E.get()))
                E.delete(0, END)
                E.insert(END,str(float(s[0]) / float(s[1])))
        if "^" in list(E.get()):
                s = inputpower(list(E.get()))
                E.delete(0, END)
                E.insert(END,str(float(s[0]) ** float(s[1])))
        if "√" in list(E.get()):
                s = inputradical(list(E.get()))
                E.delete(0, END)
                E.insert(END,str(float(s[1]) ** (1/float(s[0]))))
        if "b" in list(E.get()):
                s = remainder(list(E.get()))
                E.delete(0, END)
                E.insert(END,str(float(s[0]) % float(s[1])))
        if "k" in list(E.get()):
                s = quotient(list(E.get()))
                E.delete(0, END)
                E.insert(END,str(float(s[0]) // float(s[1])))










#function for showing a different window for Sum of Vectors

def vectors():
        win2 = Tk()
        win2.geometry("500x600")
        win2.title("Vectors")
        canvas_width = 500
        canvas_height = 600

        w = Canvas(win2,
                        width=canvas_width,
                        height=canvas_height)

        w.pack()


        w.create_line(0, 250, 500, 250, fill="red",width = 5)
        w.create_line(250, 0, 250, 500, fill="red",width = 5)



        for x in range(10,500,10):

                w.create_line(x, 0, x, 500, fill="#476042")






        for y in range(10,500,10):

                w.create_line(0, y, 500, y, fill="#476042")



        i1 = 0
        i2 = 0
        i3 = 0
              # does the sum of the vectors
        def plusv():






                a = E_x1.get()
                b = E_y1.get()
                c = E_x2.get()
                d = E_y2.get()
                sx = int(a)+int(c)
                sy = int(d)+int(b)





                i1 = w.create_line(250, 250, 250+int(b)*10, 250-int(a)*10, width = 3)
                i2 = w.create_line(250, 250, 250+int(d)*10, 250-int(c)*10, width = 3)
                i3 = w.create_line(250, 250, 250+sy*10, 250-sx*10, width = 3,fill='red')


        E_x1 = Entry(win2)
        E_x1.pack()
        E_x1.place(in_ = win , x = 80 , y = 530)

        x1 = Label(win2, text="Y")
        x1.pack()
        x1.place( x = 60 , y = 530)


        E_y1 = Entry(win2)
        E_y1.pack()
        E_y1.place(in_ = win , x = 80 , y = 510)

        x2 = Label(win2, text="X")
        x2.pack()
        x2.place( x = 60 , y = 510)


        E_x2 = Entry(win2)
        E_x2.pack()
        E_x2.place(in_ = win , x = 250 , y = 530)

        x3 = Label(win2, text="Y")
        x3.pack()
        x3.place( x = 230 , y = 530)

        E_y2 = Entry(win2)
        E_y2.pack()
        E_y2.place(in_ = win , x = 250 , y = 510)

        x4 = Label(win2, text="X")
        x4.pack()
        x4.place( x = 230 , y = 510)

        B_jambordar = Button(win2, text = "Sum", width=10,height=2, command = plusv,bg="yellow")
        B_jambordar.pack()
        B_jambordar.place(in_ = win2, x =400 , y = 520)





























## Defining all the buttons for all the numbers and operations

B1= Button(win , text = " 1 " , width = 4 , height = 2 , command  = B1,bg="yellow")
B1.pack()
B1.place(in_ = win ,x = 20 , y = 20)
B2= Button(win , text = " 2 " , width = 4 , height = 2  , command  = B2,bg="yellow")
B2.pack()
B2.place(in_ = win ,x = 60 , y = 20)
B3= Button(win , text = " 3 " , width = 4 , height = 2  , command  = B3,bg="yellow")
B3.pack()
B3.place(in_ = win ,x = 100 , y = 20)
B4= Button(win , text = " 4 " , width = 4 , height = 2 , command  = B4,bg="yellow" )
B4.pack()
B4.place(in_ = win ,x = 20 , y = 60)
B5= Button(win , text = " 5 " , width = 4 , height = 2 , command  = B5,bg="yellow" )
B5.pack()
B5.place(in_ = win ,x = 60, y = 60)
B6= Button(win , text = " 6 " , width = 4 , height = 2 , command  = B6,bg="yellow" )
B6.pack()
B6.place(in_ = win ,x = 100 , y = 60)
B7= Button(win , text = " 7 " , width = 4 , height = 2 , command  = B7,bg="yellow")
B7.pack()
B7.place(in_ = win ,x = 20 , y = 100)
B8= Button(win , text = " 8 " , width = 4 , height = 2  , command  = B8,bg="yellow")
B8.pack()
B8.place(in_ = win ,x = 60 , y = 100)
B9= Button(win , text = " 9 " , width = 4 , height = 2  , command  = B9,bg="yellow")
B9.pack()
B9.place(in_ = win ,x = 100 , y = 100)
B0= Button(win , text = " 0 " , width = 4 , height = 2  , command  = B0,bg="yellow")
B0.pack()
B0.place(in_ = win ,x = 60 , y = 140)
B00= Button(win , text = " 00 " , width = 4 , height = 2  , command  = B00,bg="yellow")
B00.pack()
B00.place(in_ = win ,x = 100 , y = 140)

B_manfi1= Button(win , text = " ± " , width = 4 , height = 2 ,command = turn_into_negative,bg="yellow")
B_manfi1.pack()
B_manfi1.place(in_ = win ,x = 20 , y = 140)

B_plus = Button(win, text = " + ", width = 4 , height = 2 ,command=plus,bg="violetred" )
B_plus.pack()
B_plus.place(in_ = win, x = 20 , y = 240)

B_plus = Button(win, text = " - ", width = 4 , height = 2 ,command=negative ,bg="violetred")
B_plus.pack()
B_plus.place(in_ = win, x = 20 , y = 200)

B_plus = Button(win, text = " × ", width = 4 , height = 2 ,command=times,bg="violetred" )
B_plus.pack()
B_plus.place(in_ = win, x = 60 , y = 240)

B_plus = Button(win, text = " ÷ ", width = 4 , height = 2 ,command=divide,bg="violetred" )
B_plus.pack()
B_plus.place(in_ = win, x = 60 , y = 200)

B_plus = Button(win, text = " ^", width = 4 , height = 2 ,command=power,bg="violetred")
B_plus.pack()
B_plus.place(in_ = win, x = 100 , y = 240)

B_plus = Button(win, text = " √ ", width = 4 , height = 2 ,command=radical,bg="violetred" )
B_plus.pack()
B_plus.place(in_ = win, x = 100 , y = 200)
B_plus = Button(win, text = " Remainder ", width = 10 , height = 2 ,command=remain,bg="black",fg="white")
B_plus.pack()
B_plus.place(in_ = win, x = 150 , y = 100)
B_plus = Button(win, text = " quotient ", width = 10 , height = 2 ,command=qu,bg="black",fg="white")
B_plus.pack()
B_plus.place(in_ = win, x = 230 , y = 100)



B_mosa = Button(win, text = " = ", width = 21 , height = 5 , command=mosa,bg="green")
B_mosa.pack()
B_mosa.place(in_ = win, x =150  , y = 200)
B_clear = Button(win, text = "C", width = 4 , height = 2 ,command=clear,bg="red" )
B_clear.pack()
B_clear.place(in_ = win, x = 150 , y = 50)
B_clearg= Button(win, text = "CE", width = 4 , height = 2 ,command=clearg,bg="red" )
B_clearg.pack()
B_clearg.place(in_ = win, x = 190 , y = 50)

B_mokhtasat = Button(win, text = " Vectors ", width = 21 , height = 2 ,command=vectors,bg="orange" )
B_mokhtasat.pack()
B_mokhtasat.place(in_ = win, x = 150 , y = 150)



mainloop()








