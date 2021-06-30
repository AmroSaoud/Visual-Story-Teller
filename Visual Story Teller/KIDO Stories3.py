"""
Calling The liberaries
"""

from Tkinter import*


"""
First Window => 
"""

root=Tk()
root.title('KIDO Stories')
scrn_W=root.winfo_screenwidth()
scrn_H=root.winfo_screenheight()
x=int(((scrn_W/2)-(scrn_W/2)))-9
y=int((scrn_H/2)-(scrn_H/2))
root.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
photo=PhotoImage(file='i13.gif')
labl=Label(root,image=photo)
labl.place(x=0,y=0)

x1=int(scrn_W/5)-10
y1=int(scrn_H/3)-40
img1=PhotoImage(file='i1.gif')
btn1=Button(width=x1,height=y1,image=img1)
btn1.place(x=x1*0+5,y=y1*0+5)

img2=PhotoImage(file='i2.gif')
btn2=Button(width=x1,height=y1,image=img2)
btn2.place(x=x1+15,y=y1*0+5)

img3=PhotoImage(file='i3.gif')
btn3=Button(width=x1,height=y1,image=img3)
btn3.place(x=x1*2+25,y=y1*0+5)

img4=PhotoImage(file='i4.gif')
btn4=Button(width=x1,height=y1,image=img4)
btn4.place(x=x1*3+35,y=y1*0+5)

img5=PhotoImage(file='i5.gif')
btn5=Button(width=x1,height=y1,image=img5)
btn5.place(x=x1*4+45,y=y1*0+5)

img6=PhotoImage(file='i6.gif')
btn6=Button(width=x1,height=y1,image=img6)
btn6.place(x=x1*0+5,y=y1+15)

img7=PhotoImage(file='i7.gif')
btn7=Button(width=x1,height=y1,image=img7)
btn7.place(x=x1*0+5,y=y1*2+25)

img8=PhotoImage(file='i8.gif')
btn8=Button(width=x1,height=y1,image=img8)
btn8.place(x=x1+15,y=y1*2+25)

img9=PhotoImage(file='i9.gif')
btn9=Button(width=x1,height=y1,image=img9)
btn9.place(x=x1*2+25,y=y1*2+25)

img10=PhotoImage(file='i10.gif')
btn10=Button(width=x1,height=y1,image=img10)
btn10.place(x=x1*3+35,y=y1*2+25)

img11=PhotoImage(file='i11.gif')
btn11=Button(width=x1,height=y1,image=img11)
btn11.place(x=x1*4+45,y=y1*2+25)

img12=PhotoImage(file='i12.gif')
btn12=Button(width=x1,height=y1,image=img12)
btn12.place(x=x1*4+45,y=y1+15)

lbl=Label(root,text="KIDO STORIES",font='Tahoma 86',bg='#ffff00')
lbl.place(x=(scrn_W/4),y=(scrn_H/2.75))
def vid1():
    os.system("\\Users\\macbook\\Documents\\Media\\Music\\7UOGuU8nMBA.mp4")
btn1=Button(root,text='Read',width=10,height=5)
btn1.place(x=0,y=700)
btn1.config(command=vid1)
#Second Window => Stories(Goldillock's and The Three Bears Story).

#(cindrella).
def window2():
    root2=Tk()
    scrn_W=root2.winfo_screenwidth()
    scrn_H=root2.winfo_screenheight()
    root2.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
    root2.title("cindrella")
    root2.configure(background='white')
    btn2=Button(root2,text='Read',width=10,height=5)
    btn2.place(x=0,y=700) 
    btnw2=Button(root2,text='Listen',width=10,height=5)
    btnw2.place(x=100,y=700)
    lblw2=Label(root2,text="cindrella",font='Times 46',fg='black',bg='white')
    lblw2.pack()
    by=Button(root2,text='close',width=10,height=5)
    by.place(x=200,y=700)
    
    def close_window2 (): 
        root2.destroy()        
            
    def two():       
        with open('Stories\\Gold 3 Beers.txt', "r") as f:
            Label(root2, text= f.read().strip(),fg='black',bg='white').pack()
                
    btn2.config(command=two)

    def twoo():
        winsound.PlaySound('Audio\\Cinderella.wav', winsound.SND_ASYNC) 
    btnw2.config(command=twoo)
    
    def O1():
        
        winsound.PlaySound(None, winsound.SND_ASYNC) 
    by.config(command=O1)
    button = Button (root2, text = "Another Story ",width=10,height=5,command = close_window2).place(x=300,y=700)    
btn2.config(command=window2)


#(bunny loves to read).
def window3():
    root3=Tk()
    scrn_W=root3.winfo_screenwidth()
    scrn_H=root3.winfo_screenheight()
    root3.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
    root3.title("Bunny Loves To Read")
    root3.configure(background='white')
    btn3=Button(root3,text='Read',width=10,height=5)
    btn3.place(x=0,y=700)
    by=Button(root3,text='Close',width=10,height=5)
    by.place(x=200,y=700)    
    btnw3=Button(root3,text='Listen',width=10,height=5)
    btnw3.place(x=100,y=700)
    lblw3=Label(root3,text="Bunny Loves To Read",font='Times 46',fg='black',bg='white')
    lblw3.pack()
    by=Button(root3,text='close',width=10,height=5)
    by.place(x=200,y=700)    
            
    def three():       
        with open('Stories\\Gold 3 Beers.txt', "r") as f:
            Label(root3, text= f.read().strip(),fg='black',bg='white').pack()                
    btn3.config(command=three)

    def threee():
        winsound.PlaySound('Audio\\Bunny Loves to Write.wav', winsound.SND_ASYNC) 
    btnw3.config(command=threee)
    
    def close_window1 (): 
        root3.destroy()

    def O():
        winsound.PlaySound(None, winsound.SND_ASYNC) 
    by.config(command=O)
    button = Button (root3, text = "Another Story ",width=10,height=5,command = close_window1).place(x=300,y=700)
btn3.config(command=window3)


#(The Gingerbread Man).
def window4():
    root4=Tk()
    scrn_W=root4.winfo_screenwidth()
    scrn_H=root4.winfo_screenheight()
    root4.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
    root4.title("The Gingerbread Man")
    root4.configure(background='white')
    btn4=Button(root4,text='Read',width=10,height=5)
    btn4.place(x=0,y=700)
    btnw4=Button(root4,text='Listen',width=10,height=5)
    btnw4.place(x=100,y=700)
    lblw4=Label(root4,text="The Gingerbread Man",font='Times 46',fg='black',bg='white')
    lblw4.pack()         
    by=Button(root4,text='close',width=10,height=5)
    by.place(x=200,y=700)
    
    def four():       
        with open('Stories\\Gold 3 Beers.txt', "r") as f:
                Label(root4, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn4.config(command=four)

    def fourr():
        winsound.PlaySound('Audio\\The Gingerbread Man.wav', winsound.SND_ASYNC)
    btnw4.config(command=fourr)
    
    def close_window1 (): 
        root4.destroy()

    def O():
        winsound.PlaySound(None, winsound.SND_ASYNC) 
    by.config(command=O)
    button = Button (root4, text = "Another Story ",width=10,height=5,command = close_window1).place(x=300,y=700)    
btn4.config(command=window4)


#(The Three Billy Goat Gruff).
def window5():
    root5=Tk()
    scrn_W=root5.winfo_screenwidth()
    scrn_H=root5.winfo_screenheight()
    root5.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
    root5.title("The Three Billy Goat Gruff")
    root5.configure(background='white')
    btn5=Button(root5,text='Read',width=10,height=5)
    btn5.place(x=0,y=700)
    btnw5=Button(root5,text='Listen',width=10,height=5)
    btnw5.place(x=100,y=700)
    lblw5=Label(root5,text="The Three Billy Goat Gruff",font='Times 46',fg='black',bg='white')
    lblw5.pack()
    by=Button(root5,text='close',width=10,height=5)
    by.place(x=200,y=700)    
                    
    def five():       
        with open('Stories\\Gold 3 Beers.txt', "r") as f:
                Label(root5, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn5.config(command=five)

    def fivee():
        winsound.PlaySound('Audio\\The Three Billy Goats Gruff.wav', winsound.SND_ASYNC)
    btnw5.config(command=fivee)
    
    def close_window1 (): 
        root5.destroy()

    def O():
        winsound.PlaySound(None, winsound.SND_ASYNC) 
    by.config(command=O)
    button = Button (root5, text = "Another Story ",width=10,height=5,command = close_window1).place(x=300,y=700)    
btn5.config(command=window5)


#(The Littel Mermaid).
def window6():
    root6=Tk()
    scrn_W=root6.winfo_screenwidth()
    scrn_H=root6.winfo_screenheight()
    root6.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
    root6.title("The Littel Mermaid")
    root6.configure(background='white')
    btn6=Button(root6,text='Read',width=10,height=5)
    btn6.place(x=0,y=700)
    btnw6=Button(root6,text='Listen',width=10,height=5)
    btnw6.place(x=100,y=700)
    lblw6=Label(root6,text="The Littel Mermaid",font='Times 46',fg='black',bg='white')
    lblw6.pack()
    by=Button(root6,text='close',width=10,height=5)
    by.place(x=200,y=700)    
            
    def six():
        with open('Stories\\Mermaid.txt', "r") as f:
            Label(root6, text= f.read().strip(),fg='black',bg='white').pack()
    btn6.config(command=six)

    def sixx():
        winsound.PlaySound('Audio\\Little Mermaid.wav', winsound.SND_ASYNC)
    btnw6.config(command=sixx)
    
    def close_window1 (): 
        root6.destroy()

    def O():
        winsound.PlaySound(None, winsound.SND_ASYNC) 
    by.config(command=O)
    button = Button (root6, text = "Another Story ",width=10,height=5,command = close_window1).place(x=300,y=700)    
btn6.config(command=window6)


#(The Princess And The Pea).
def window7():
    root7=Tk()
    scrn_W=root7.winfo_screenwidth()
    scrn_H=root7.winfo_screenheight()
    root7.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
    root7.title("The Princess And The Pea")
    root7.configure(background='white')
    btn7=Button(root7,text='Read',width=10,height=5)
    btn7.place(x=0,y=700)
    btnw7=Button(root7,text='Listen',width=10,height=5)
    btnw7.place(x=100,y=700)
    lblw7=Label(root7,text="The Princess And The Pea",font='Times 46',fg='black',bg='white')
    lblw7.pack()
    by=Button(root7,text='close',width=10,height=5)
    by.place(x=200,y=700)    
                            
    def seven():       
        with open('Stories\\Gold 3 Beers.txt', "r") as f:
            Label(root7, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn7.config(command=seven)

    def sevenn():
        winsound.PlaySound('Audio\\The Princess And The Pea.wav', winsound.SND_ASYNC)
    btnw7.config(command=sevenn)
    
    def close_window1 (): 
        root7.destroy()

    def O():
        winsound.PlaySound(None, winsound.SND_ASYNC) 
    by.config(command=O)
    button = Button (root7, text = "Another Story ",width=10,height=5,command = close_window1).place(x=300,y=700)    
btn7.config(command=window7)


#(Little Red Riding Hood).
def window8():
    root8=Tk()
    scrn_W=root8.winfo_screenwidth()
    scrn_H=root8.winfo_screenheight()
    root8.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
    root8.title("Little Red Riding Hood")
    root8.configure(background='white')
    btn8=Button(root8,text='Read',width=10,height=5)
    btn8.place(x=0,y=700)
    btnw8=Button(root8,text='Listen',width=10,height=5)
    btnw8.place(x=100,y=700)
    lblw8=Label(root8,text="Little Red Riding Hood",font='Times 46',fg='black',bg='white')
    lblw8.pack()
    by=Button(root8,text='close',width=10,height=5)
    by.place(x=200,y=700)    
                                
    def eight():       
        with open('Stories\\Gold 3 Beers.txt', "r") as f:
            Label(root8, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn8.config(command=eight)

    def eightt():
        winsound.PlaySound('Audio\\Little Red Riding Hood.wav', winsound.SND_ASYNC)
    btnw8.config(command=eightt)
    
    def close_window1 (): 
        root8.destroy()

    def O():
        winsound.PlaySound(None, winsound.SND_ASYNC) 
    by.config(command=O)
    button = Button (root8, text = "Another Story ",width=10,height=5,command = close_window1).place(x=300,y=700)    
btn8.config(command=window8)


#(One Bear Lost).
def window9():
    root9=Tk()
    scrn_W=root9.winfo_screenwidth()
    scrn_H=root9.winfo_screenheight()
    root9.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
    root9.title("One Bear Lost")
    root9.configure(background='white')
    btn9=Button(root9,text='Read',width=10,height=5)
    btn9.place(x=0,y=700)
    btnw9=Button(root9,text='Listen',width=10,height=5)
    btnw9.place(x=100,y=700)
    lblw9=Label(root9,text="One Bear Lost",font='Times 46',fg='black',bg='white')
    lblw9.pack()
    by=Button(root9,text='close',width=10,height=5)
    by.place(x=200,y=700)    
                                
    def nine():       
        with open('Stories\\Gold 3 Beers.txt', "r") as f:
            Label(root9, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn9.config(command=nine)

    def ninee():
        winsound.PlaySound('Audio\\One Bear Lost.wav', winsound.SND_ASYNC)
    btnw9.config(command=ninee)
    
    def close_window1 (): 
        root9.destroy()

    def O():
        winsound.PlaySound(None, winsound.SND_ASYNC) 
    by.config(command=O)
    button = Button (root9, text = "Another Story ",width=10,height=5,command = close_window1).place(x=300,y=700)    
btn9.config(command=window9)


#(Jack And The Bean Stalk).
def window10():
    root10=Tk()
    scrn_W=root10.winfo_screenwidth()
    scrn_H=root10.winfo_screenheight()
    root10.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
    root10.title("Jack And The Bean Stalk")
    root10.configure(background='white')
    btn10=Button(root10,text='Read',width=10,height=5)
    btn10.place(x=0,y=700)
    btnw10=Button(root10,text='Listen',width=10,height=5)
    btnw10.place(x=100,y=700)
    lblw10=Label(root10,text="Jack And The Bean Stalk",font='Times 46',fg='black',bg='white')
    lblw10.pack()
    by=Button(root10,text='close',width=10,height=5)
    by.place(x=200,y=700)
                                
    def ten():       
        with open('Stories\\Gold 3 Beers.txt', "r") as f:
            Label(root10, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn10.config(command=ten)

    def tenn():
        winsound.PlaySound('Audio\\Jack and The Beanstalk.wav', winsound.SND_ASYNC)
    btnw10.config(command=tenn)
    
    def close_window1 (): 
        root10.destroy()

    def O():
        winsound.PlaySound(None, winsound.SND_ASYNC) 
    by.config(command=O)
    button = Button (root10, text = "Another Story ",width=10,height=5,command = close_window1).place(x=300,y=700)    
btn10.config(command=window10)


#(I Love My Mummy).
def window11():
    root11=Tk()
    scrn_W=root11.winfo_screenwidth()
    scrn_H=root11.winfo_screenheight()
    root11.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
    root11.title("I Love My Mummy")
    root11.configure(background='white')
    btn11=Button(root11,text='Read',width=10,height=5)
    btn11.place(x=0,y=700)
    btnw11=Button(root11,text='Listen',width=10,height=5)
    btnw11.place(x=100,y=700)
    lblw11=Label(root11,text="I Love My Mummy",font='Times 46',fg='black',bg='white')
    lblw11.pack()
    by=Button(root11,text='close',width=10,height=5)
    by.place(x=200,y=700)    
                                
    def eleven():       
        with open('Stories\\Gold 3 Beers.txt', "r") as f:
            Label(root11, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn11.config(command=eleven)

    def elevenn():
        winsound.PlaySound('Audio\\I Love My Mommy.wav', winsound.SND_ASYNC)
    btnw11.config(command=elevenn)
    
    def close_window1 (): 
        root11.destroy()

    def O():
        winsound.PlaySound(None, winsound.SND_ASYNC) 
    by.config(command=O)
    button = Button (root11, text = "Another Story ",width=10,height=5,command = close_window1).place(x=300,y=700)    
btn11.config(command=window11)


#(I Love My Daddy).
def window12():
    root12=Tk()
    scrn_W=root12.winfo_screenwidth()
    scrn_H=root12.winfo_screenheight()
    root12.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
    root12.title("I Love My Daddy")
    root12.configure(background='white')
    btn12=Button(root12,text='Read',width=10,height=5)
    btn12.place(x=0,y=700)
    btnw12=Button(root12,text='Listen',width=10,height=5)
    btnw12.place(x=100,y=700)
    lblw12=Label(root12,text="I Love My Daddy",font='Times 46',fg='black',bg='white')
    lblw12.pack()
    by=Button(root12,text='close',width=10,height=5)
    by.place(x=200,y=700)
                                
    def lve():       
        with open('Stories\\Gold 3 Beers.txt', "r") as f:
            Label(root12, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn12.config(command=lve)

    def lvee():
        winsound.PlaySound('Audio\\I Love My Daddy.wav', winsound.SND_ASYNC)
    btnw12.config(command=lvee)
    
    def close_window1 (): 
        root12.destroy()

    def O():
        winsound.PlaySound(None, winsound.SND_ASYNC) 
    by.config(command=O)
    button = Button (root12, text = "Another Story ",width=10,height=5,command = close_window1).place(x=300,y=700)    
btn12.config(command=window12)
mainloop()