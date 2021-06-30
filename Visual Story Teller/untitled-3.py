from Tkinter import *

form = Tk()
form.title("Welcome to nile university")
form.geometry('1280x800')
photo=PhotoImage(file='/Users/macbook/Desktop/1st/91.gif')
labl=Label(form,image=photo,bd=0)
labl.place(x=400,y=50)
a = Label(form ,text = " ID").place(x=0,y=0)
l=Label(form ,text = "/").place(x = 320,y=3)
e = Entry(show ='*')
e.place(x=35,y=15)
PRESSURE = Label(text = "PRESSURE  ",).place(x = 15, y = 70)
SUGAR = Label(text = "SUGAR",).place(x = 15, y = 140)
PULSE = Label(text = "PULSE",).place(x = 15, y = 210)
HEIGHT = Label(text = "HEIGHT",).place(x = 15, y = 280)
WEIGHT = Label(text = "WEIGHT",).place(x = 15, y = 350)       
P = Entry( width = "30")
P.place(x = 15, y = 100)
S = Entry(width = "30")
S.place(x = 15, y = 180)
PU = Entry(width = "30")
PU.place(x = 15, y = 240)
H= Entry(width = "30")
H.place(x = 15, y = 320)
W= Entry(width = "30")
W.place(x = 15, y = 380)
p=open('lie.txt','a')
f=open('medic.txt','a')

def window1():
       f.write(e.get())
       f.write('\n')
       p.write(P.get())
       p.write('\n')
       p.write(S.get())
       p.write('\n')
       p.write(PU.get())
       p.write('\n')
       p.write(H.get())
       p.write('\n')
       p.write(W.get())              
       p.close()       
       f.close()
btn11=Button(form,text='submit',bd=0,command=window1).place(x=250,y=0)


       
      
def window2():
       form2 = Tk()
       form2.title("")
       form2.geometry('300x300')   
       Label(form2,text='Enter Your Data').pack()
       a2 = Entry(form2,bd=1,show='*')
       a2.place(x=3,y=40)
       y2 = Label(form2 ,text = "ID")
       y2.place(x=0,y=10)
       def wi():
              file=open("medic.txt",'r')
              Lines=file.readlines()
              Ln=[]
              
              for i in Lines:
                     Ln.append(i.strip())
              
              if a2.get() in Ln :
                     root = Tk()
                     root.title("Informations")
                     root.geometry('700x700')     
                     with open('lie.txt', "r") as we:
                            Label(root, text= we.read(),fg='black').grid()          
                     root.mainloop()
              else:
                     root1 = Tk()
                     root1.title("Error")
                     root1.geometry('200x200')
                     Label(root1,text='wrong ID').pack()
                     root1.mainloop()
                     
                     
       btn1=Button(form2,text='submit',bd=0,command=wi).place(x=0,y=80)
l1=Button(form,text='Login',bd=0,command=window2).place(x=340,y=0)
mainloop()