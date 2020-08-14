from tkinter import *

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):
    l=a if a>b else b
    while l<=a*b:
        if l%a==0 and l%b==0:
            return l
    l+=1
    
    
def hcf(a,b):
    h=a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
    h-=1
    
def extract_from_text(text):
    L=[]
    for t in text.split(' '):
        try:
            L.append(float(t))
            
        except ValueError:
            pass
    return L

def calculate():
    text=textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                L=extract_from_text(text)
                r=operations[word.upper()](L[0],L[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'Something Went Wrong Please Enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'Something Went Wrong Please Enter again')
            
    
    
operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUB':sub,'DIFFERENCE':sub,'MINUS':sub,'SUBTRACT':sub,
            'LCM':lcm,'HCF':hcf,'PRODUCT':mul,'MULTIPLICATION':mul,
            'MULTIPLY':mul,'DIVISION':div,'DIV':div,'DIVIDE':div,'MOD':mod,'REMAINDER':mod,'MODULUS':mod}

win=Tk()
win.geometry('500x300')
win.title('CALCY')
win.configure(bg='Lightskyblue')


l1=Label(win,text='SMART CALCULATOR',width=20,padx=3)
l1.place(x=150,y=10)
l2=Label(win,text='Hello I am Here To Help You Out ',width=30,padx=3)
l2.place(x=115,y=40)
l3=Label(win,text='What can I Help You',padx=3)
l3.place(x=176,y=130)

textin=StringVar()
e1=Entry(win,width=50,textvariable=textin)
e1.place(x=100,y=160)

b1=Button(win,text='Just This',command=calculate)
b1.place(x=210,y=200)

list=Listbox(win,width=30,height=3)
list.place(x=150,y=230)

win.mainloop()