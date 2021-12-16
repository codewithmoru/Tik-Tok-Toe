from io import StringIO
from tkinter import*
from tkinter import messagebox


player = 1
bx1 = '1'
bx2 = '2'
bx3 = '3'
bx4 = '4'
bx5 = '5'
bx6 = '6'
bx7 = '7'
bx8 = '8'
bx9 = '9'

root = Tk()

root.geometry('1250x650+50+20')
root.resizable(width=FALSE, height=FALSE)

root.title('Tik Tak Toe')
root['bg']='pink'
operator = ""
text_input = StringVar()
text_input1 = StringVar()

class footer():
    def __init__(self, root=None):
        self.l = Label(root, text='Tik__Tak__Toe', bg='deepskyblue', width='50')
        self.l.pack()
        self.f0 = Frame(root, bg='orange', height='5', bd='5px').pack(fill=X)
        self.l1 = Label(root, text='1st Player :', bg='gold', fg='black', width='15', bd='3px')
        self.l1.place(x='100', y='50')
        self.e1 = Entry(root, width='30', bg='violet', bd='3px', textvariable = text_input)
        self.e1.place(x='230', y='50')
        self.l0 = Label(root, text='Vs', bg='gold', fg='black',  bd='3px', width='10')
        self.l0.place(x='450', y='50')
        self.l2 = Label(root, text='2nd Player :', bg='gold', fg='black', width='15', bd='3px')
        self.l2.place(x='570', y='50')
        self.e2 = Entry(root, width='30',bg='violet', bd='3px', textvariable = text_input1)
        self.e2.place(x='700', y='50')
        
footer()

class dashbord():
    def __init__(self, f1=None):
        self.f1 = Frame(root, width='490', height='500', bg='burlywood', relief=RAISED)
        self.f1.place(x='50', y='100')
        self.l3 = Label(f1, text='Dashbord', bg='orangered', width='50')
        self.l3.place(x='120', y='100')
        self.f2 = Frame(root, width='450', height='80', bg='burlywood', relief=RAISED)
        self.f2.place(x='650', y='150')       
        self.f3 = Frame(root,  width='450', height='80', bg='burlywood', relief=RAISED)
        self.f3.place(x='650', y='250')       
        self.f4 = Frame(root,  width='450', height='80', bg='burlywood', relief=RAISED)
        self.f4.place(x='650', y='350')       
        self.f5 = Frame(root,  width='450', height='80', bg='burlywood', relief=RAISED)
        self.f5.place(x='650', y='450')       
         

# Buttons of dashbord...!
            
        b1 = Button(root, text=" ",  width='15', height='7', font='20', bd='3px', activebackground='orange' ,command=lambda : activate(1))
        b1.place(x='60', y='150')       
        b2 = Button(root, text=" ",  width='15', height='7', font='20', bd='3px', bg='black', fg='red',activebackground='orange', command=lambda : activate(2))
        b2.place(x='60', y='300')       
        b3 = Button(root, text=" ",  width='15', height='7', font='20', bd='3px', activebackground='orange', command=lambda : activate(3))
        b3.place(x='60', y='450')       
        b4 = Button(root, text=" ",  width='15', height='7', font='20', bd='3px', bg='black',fg='red', activebackground='orange', command=lambda : activate(4))
        b4.place(x='220', y='150')       
        b5 = Button(root, text=" ",  width='15', height='7', font='15', bd='3px', activebackground='orange',command=lambda : activate(5))
        b5.place(x='220', y='300')       
        b6 = Button(root, text=" ",  width='15', height='7', font='15', bd='3px', bg='black',fg='red', activebackground='orange', command=lambda : activate(6))
        b6.place(x='220', y='450')       
        b7 = Button(root, text=" ",  width='15', height='7', font='15', bd='3px', activebackground='orange',command=lambda : activate(7))
        b7.place(x='380', y='150')       
        b8 = Button(root, text=" ",  width='15', height='7', font='15', bd='3px', bg='black',fg='red', activebackground='orange', command=lambda : activate(8))
        b8.place(x='380', y='300')       
        b9 = Button(root, text=" ",  width='15', height='7', font='15', bd='3px', command=lambda : activate(9))
        b9.place(x='380', y='450')       

        def maker():
            messagebox.showinfo('Creator :',  "Eng. Moreshwar Mahale")

        b10 = Button(root, text='Creator', font='Times 10 bold', bg='slategrey', activebackground='orange' ,width='50' , height='2' ,command= maker)
        b10.place(x='700', y='370')
                        
        def NewGame():
             global operator
             operator = ""
             text_input.set('')
             text_input1.set('')
             
        b11 = Button(root, text='Start New Game', font='Times 10 bold', bg='slategrey', activebackground='orange' ,width='50' , height='2' ,command= NewGame)
        b11.place(x='700', y='170')
    
        def ClearDash():
             global operator
             operator = ""
             text_input.set('')
             text_input1.set('')
            

        b12 = Button(root, text='Clear', font='Times 10 bold' , bg='slategrey', activebackground='orange', width='50' , height='2' ,command= ClearDash)
        b12.place(x='700', y='270')      

        b13 = Button(root, text='Exit', font='Times 10 bold' , bg='slategrey', activebackground='orange',width='50' , height='2' ,command= root.quit)
        b13.place(x='700', y='470')


        player = 1
        
        def activate (box):
            global player
            global bx1
            global bx2
            global bx3
            global bx4
            global bx5
            global bx6
            global bx7
            global bx8
            global bx9
            
            
            if box == 1 and player == 1:  
               b1.config(text='O')
               player = 2
               bx1 = 'O'  

            elif box == 1 and player == 2:
                 b1.config(text='X')
                 player = 1
                 bx1 = 'X'

            elif box == 2 and player == 1:
                 b2.config(text='O')
                 player = 2
                 bx2 = 'O'

            elif box == 2 and player == 2:
                 b2.config(text='X')
                 player = 1
                 bx2 = 'X'

            elif box == 3 and player == 1:
                 b3.config(text='O') 
                 player = 2
                 bx3 = 'O'   
            
            elif box == 3 and player == 2:
                 b3.config(text='X')
                 player = 1
                 bx3 = 'X'

            elif box == 4 and player == 1:
                 b4.config(text='O') 
                 player = 2
                 bx4 = 'O'

            elif box == 4 and player == 2:
                  b4.config(text='X')
                  player = 1
                  bx4 = 'X'

            elif box == 5 and player == 1:
                  b5.config(text='O')
                  player = 2
                  bx5 = 'O'
             
            elif box == 5 and player == 2:
                  b5.config(text='X')
                  player = 1
                  bx5 = 'X'

            elif box == 6 and player == 1:
                  b6.config(text='O')
                  player = 2
                  bx6 = 'O'
             
            elif box == 6 and player == 2:
                  b6.config(text='X')
                  player = 1
                  bx6 = 'X'

            elif box == 7 and player == 1:
                  b7.config(text='O')
                  player = 2
                  bx7 = 'O'

            elif box == 7 and player == 2:
                  b7.config(text='X')
                  player = 1
                  bx7 = 'X'

            elif box == 8 and player == 1:
                  b8.config(text='O')
                  player = 2
                  bx8 = 'O'

            elif box == 8 and player == 2:
                  b8.config(text='X')
                  player = 1
                  bx4 = 'X'

            elif box == 9 and player == 1:
                  b9.config(text='O')
                  player = 2
                  bx9 = 'O'

            elif box == 9 and player == 2:
                  b9.config(text='X')
                  player = 1
                  bx9 = 'X'

                     
dashbord()  


root.mainloop()

#you have to set new gane button by lambda ok.....!