"""
Calling The liberaries
"""
from Tkinter import*
import subprocess


"""
First Window => 
"""

root=Tk()
root.title('KIDO Stories')
scrn_W=root.winfo_screenwidth()
scrn_H=root.winfo_screenheight()
x=int((scrn_W/2)-(scrn_W/2))
y=int((scrn_H/2)-(scrn_H/2))
root.geometry('{:d}x{:d}+{:d}+{:d}'.format(scrn_W,scrn_H,x,y))
photo=PhotoImage(file='i13.gif')
labl=Label(root,image=photo)
labl.place(x=0,y=0)

img1=PhotoImage(file='i1.gif')
btn1=Button(width=250,height=230,image=img1)
btn1.place(x=15,y=5)

img2=PhotoImage(file='i2.gif')
btn2=Button(width=250,height=230,image=img2)
btn2.place(x=285,y=5)

img3=PhotoImage(file='i3.gif')
btn3=Button(width=250,height=230,image=img3)
btn3.place(x=555,y=5)

img4=PhotoImage(file='i4.gif')
btn4=Button(width=250,height=230,image=img4)
btn4.place(x=825,y=5)

img5=PhotoImage(file='i5.gif')
btn5=Button(width=250,height=230,image=img5)
btn5.place(x=1095,y=5)

img6=PhotoImage(file='i6.gif')
btn6=Button(width=250,height=230,image=img6)
btn6.place(x=15,y=245)

img7=PhotoImage(file='i7.gif')
btn7=Button(width=250,height=230,image=img7)
btn7.place(x=15,y=485)

img8=PhotoImage(file='i8.gif')
btn8=Button(width=250,height=230,image=img8)
btn8.place(x=285,y=485)

img9=PhotoImage(file='i9.gif')
btn9=Button(width=250,height=230,image=img9)
btn9.place(x=555,y=485)

img10=PhotoImage(file='i10.gif')
btn10=Button(width=250,height=230,image=img10)
btn10.place(x=825,y=485)

img11=PhotoImage(file='i11.gif')
btn11=Button(width=250,height=230,image=img11)
btn11.place(x=1095,y=485)

img12=PhotoImage(file='i12.gif')
btn12=Button(width=250,height=230,image=img12)
btn12.place(x=1095,y=245)
lbl=Label(root,text="KIDO STORIES",font='Tahoma 86',bg='#ffff00')
lbl.place(x=300,y=290)

#Second Window => Stories(Goldillock's and The Three Bears Story).
def window1():
    root1=Tk()
    root1.geometry('1920x1090')
    root1.title("Goldillock's and The Three Bears Story")
    root1.configure(background='white')
    btn1=Button(root1,text='Read',width=10,height=5)
    btn1.place(x=20,y=100)
    btnw1=Button(root1,text='Listen',width=10,height=5)
    btnw1.place(x=20,y=200)
    lblw1=Label(root1,text="Goldillock's and The Three Bears Story",font='Times 46',fg='black',bg='white')
    lblw1.pack()
            
    def one():       
        with open('/Users/macbook/Downloads/Project/st1.docx', "r") as f:
            Label(root1, text= f.read().strip(),fg='black',bg='white').pack()           
    btn1.config(command=one)
    def onee():
        subprocess.call(['aplay','bl.mp3'],)
    btnw1.config(command=one)
btn1.config(command=window1)
#(cindrella).
def window2():
    root2=Tk()
    root2.geometry('1920x1090')
    root2.title("cindrella")
    root2.configure(background='white')
    btn2=Button(root2,text='Read',width=10,height=5)
    btn2.place(x=20,y=100)
    btnw2=Button(root2,text='Listen',width=10,height=5)
    btnw2.place(x=20,y=200)
    lblw2=Label(root2,text="cindrella",font='Times 46',fg='black',bg='white')
    lblw2.pack()
            
    def two():       
        with open('/Users/macbook/Downloads/Project/st1.docx', "r") as f:
            Label(root2, text= f.read().strip(),fg='black',bg='white').pack()
                
    btn2.config(command=two)
    def twoo():
        subprocess.call(['aplay','bl.mp3'],)
    btnw2.config(command=twoo)
btn2.config(command=window2)
#(bunny loves to read).
def window3():
    root3=Tk()
    root3.geometry('1920x1090')
    root3.title("Bunny Loves To Read")
    root3.configure(background='white')
    btn3=Button(root3,text='Read',width=10,height=5)
    btn3.place(x=20,y=100)
    btnw3=Button(root3,text='Listen',width=10,height=5)
    btnw3.place(x=20,y=200)
    lblw3=Label(root3,text="Bunny Loves To Read",font='Times 46',fg='black',bg='white')
    lblw3.pack()
            
    def three():       
        with open('/Users/macbook/Downloads/Project/st1.docx', "r") as f:
            Label(root3, text= f.read().strip(),fg='black',bg='white').pack()                
    btn3.config(command=three)
    def threee():
        subprocess.call(['aplay','bl.mp3'],)
    btnw3.config(command=threee)
btn3.config(command=window3)
#(The Gingerbread Man).
def window4():
    root4=Tk()
    root4.geometry('1920x1090')
    root4.title("The Gingerbread Man")
    root4.configure(background='white')
    btn4=Button(root4,text='Read',width=10,height=5)
    btn4.place(x=20,y=100)
    btnw4=Button(root4,text='Listen',width=10,height=5)
    btnw4.place(x=20,y=200)
    lblw4=Label(root4,text="The Gingerbread Man",font='Times 46',fg='black',bg='white')
    lblw4.pack()            
    def four():       
        with open('/Users/macbook/Downloads/Project/st1.docx', "r") as f:
                Label(root4, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn4.config(command=four)
    def fourr():
        subprocess.call(['aplay','bl.mp3'],)
    btnw4.config(command=fourr)
btn4.config(command=window4)
#(The Three Billy Goat Gruff).
def window5():
    root5=Tk()
    root5.geometry('1920x1090')
    root5.title("The Three Billy Goat Gruff")
    root5.configure(background='white')
    btn5=Button(root5,text='Read',width=10,height=5)
    btn5.place(x=20,y=100)
    btnw5=Button(root5,text='Listen',width=10,height=5)
    btnw5.place(x=20,y=200)
    lblw5=Label(root5,text="The Three Billy Goat Gruff",font='Times 46',fg='black',bg='white')
    lblw5.pack()
    
                    
    def five():       
        with open('/Users/macbook/Downloads/Project/st1.docx', "r") as f:
                Label(root5, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn5.config(command=five)
    def fivee():
        subprocess.call(['aplay','bl.mp3'],)
    btnw5.config(command=fivee)
btn5.config(command=window5)
#(The Littel Mermaid).
def window6():
    root6=Tk()
    root6.geometry('1920x1090')
    root6.title("The Littel Mermaid")
    root6.configure(background='white')
    btn6=Button(root6,text='Read',width=10,height=5)
    btn6.place(x=20,y=100)
    btnw6=Button(root6,text='Listen',width=10,height=5)
    btnw6.place(x=20,y=200)
    lblw6=Label(root6,text="The Littel Mermaid",font='Times 46',fg='black',bg='white')
    lblw6.pack()
            
    def six():       
        with open('/Users/macbook/Downloads/Project/st1.docx', "r") as f:
            Label(root6, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn6.config(command=six)
    def sixx():
        subprocess.call(['aplay','bl.mp3'],)
    btnw6.config(command=sixx)
btn6.config(command=window6)
#(The Princess And The Pea).
def window7():
    root7=Tk()
    root7.geometry('1920x1090')
    root7.title("The Princess And The Pea")
    root7.configure(background='white')
    btn7=Button(root7,text='Read',width=10,height=5)
    btn7.place(x=20,y=100)
    btnw7=Button(root7,text='Listen',width=10,height=5)
    btnw7.place(x=20,y=200)
    lblw7=Label(root7,text="The Princess And The Pea",font='Times 46',fg='black',bg='white')
    lblw7.pack()
            
                            
    def seven():       
        with open('/Users/macbook/Downloads/Project/st1.docx', "r") as f:
            Label(root7, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn7.config(command=seven)
    def sevenn():
        subprocess.call(['aplay','bl.mp3'],)
    btnw7.config(command=sevenn)
btn7.config(command=window7)
#(Little Red Riding Hood).
def window8():
    root8=Tk()
    root8.geometry('1920x1090')
    root8.title("Little Red Riding Hood")
    root8.configure(background='white')
    btn8=Button(root8,text='Read',width=10,height=5)
    btn8.place(x=20,y=100)
    btnw8=Button(root8,text='Listen',width=10,height=5)
    btnw8.place(x=20,y=200)
    lblw8=Label(root8,text="Little Red Riding Hood",font='Times 46',fg='black',bg='white')
    lblw8.pack()
                
                                
    def eight():       
        with open('/Users/macbook/Downloads/Project/st1.docx', "r") as f:
            Label(root8, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn8.config(command=eight)
    def eightt():
        subprocess.call(['aplay','bl.mp3'],)
    btnw8.config(command=eightt)
btn8.config(command=window8)
#(One Bear Lost).
def window9():
    root9=Tk()
    root9.geometry('1920x1090')
    root9.title("One Bear Lost")
    root9.configure(background='white')
    btn9=Button(root9,text='Read',width=10,height=5)
    btn9.place(x=20,y=100)
    btnw9=Button(root9,text='Listen',width=10,height=5)
    btnw9.place(x=20,y=200)
    lblw9=Label(root9,text="One Bear Lost",font='Times 46',fg='black',bg='white')
    lblw9.pack()
                
                                
    def nine():       
        with open('/Users/macbook/Downloads/Project/st1.docx', "r") as f:
            Label(root9, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn9.config(command=nine)
    def ninee():
        subprocess.call(['aplay','bl.mp3'],)
    btnw9.config(command=ninee)
btn9.config(command=window9)
#(Jack And The Bean Stalk).
def window10():
    root10=Tk()
    root10.geometry('1920x1090')
    root10.title("Jack And The Bean Stalk")
    root10.configure(background='white')
    btn10=Button(root10,text='Read',width=10,height=5)
    btn10.place(x=20,y=100)
    btnw10=Button(root10,text='Listen',width=10,height=5)
    btnw10.place(x=20,y=200)
    lblw10=Label(root10,text="Jack And The Bean Stalk",font='Times 46',fg='black',bg='white')
    lblw10.pack()
                
                                
    def ten():       
        with open('/Users/macbook/Downloads/Project/st1.docx', "r") as f:
            Label(root10, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn10.config(command=ten)
    def tenn():
        subprocess.call(['aplay','bl.mp3'],)
    btnw10.config(command=tenn)
btn10.config(command=window10)
#(I Love My Mummy).
def window11():
    root11=Tk()
    root11.geometry('1920x1090')
    root11.title("I Love My Mummy")
    root11.configure(background='white')
    btn11=Button(root11,text='Read',width=10,height=5)
    btn11.place(x=20,y=100)
    btnw11=Button(root11,text='Listen',width=10,height=5)
    btnw11.place(x=20,y=200)
    lblw11=Label(root11,text="I Love My Mummy",font='Times 46',fg='black',bg='white')
    lblw11.pack()
                
                                
    def eleven():       
        with open('/Users/macbook/Downloads/Project/st1.docx', "r") as f:
            Label(root11, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn11.config(command=eleven)
    def elevenn():
        subprocess.call(['aplay','bl.mp3'],)
    btnw11.config(command=elevenn)
btn11.config(command=window11)
#(I Love My Daddy).
def window12():
    root12=Tk()
    root12.geometry('1920x1090')
    root12.title("I Love My Daddy")
    root12.configure(background='white')
    btn12=Button(root12,text='Read',width=10,height=5)
    btn12.place(x=20,y=100)
    btnw12=Button(root12,text='Listen',width=10,height=5)
    btnw12.place(x=20,y=200)
    lblw12=Label(root12,text="I Love My Daddy",font='Times 46',fg='black',bg='white')
    lblw12.pack()
                
                                
    def lve():       
        with open('/Users/macbook/Downloads/Project/st1.docx', "r") as f:
            Label(root12, text= f.read().strip(),fg='black',bg='white').pack()                    
    btn12.config(command=lve)
    def lvee():
        subprocess.call(['aplay','bl.mp3'],)
    btnw12.config(command=lvee)
btn12.config(command=window12)
mainloop()