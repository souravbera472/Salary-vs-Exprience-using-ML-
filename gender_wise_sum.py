from tkinter import *
from tkinter import messagebox as msg
import pandas as pd
from sklearn import linear_model
import numpy as np
import math



class prediction:
    def __init__(self,root):
          self.f = Frame(root, height=350, width=500,bg='khaki')
          self.f.pack()    # Place the frame on root window
           
          # Creating label widgets
          self.label1 = Label(self.f,text='Gender wise salary',bg='yellow',font=('Arial', 14))
          #self.text1 = Entry(self.f, text='',font=('Arial', 14),width=6)
          self.label2 = Label(self.f,text='',fg='cyan',bg='black',font=('Arial', 14))
          self.label3 = Label(self.f,text='',fg='cyan',bg='black',font=('Arial', 14))
          self.label4 = Label(self.f,text='',fg='cyan',bg='black',font=('Arial', 14))
          self.label5 = Label(self.f,text='',fg='cyan',bg='black',font=('Arial', 14))
          
          
          # Buttons
          self.button1 = Button(self.f,text='Calculate', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.func)
          self.button2 = Button(self.f,text='Exit', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=root.destroy)
          

          # Placing the widgets using grid manager
          self.label1.grid(row=1, column=1)
          #self.text1.grid(row=1,column=1)
          self.button1.grid(row=2,column=0)
          self.button2.grid(row=2,column=2)
          self.label2.grid(row=3,column=1)
          self.label3.grid(row=4,column=1)
          self.label4.grid(row=5,column=1)
          self.label5.grid(row=6,column=1)
    def func(self):
        df=pd.read_csv("empsal.csv")
        sex=list(df['sex'])
        sal=list(df['salary'])
        hra=list(df['hra'])
        y=[]
        sum1=0
        sum2=0
        p=0
        q=0
        for i,j,k in zip(sex,sal,hra):
            if i=='M':
                sum1=sum1+(float(k)+float(j))
                p+=1;
            else:
                sum2=sum2+(float(k)+float(j))
                q+=1;
        mean1 = sum1/p
        mean2 = sum2/q
       
                
            
        #x=df.iloc[:,6:7]
        #x1=[]
        #x1.append(x)
        #reg=linear_model.LinearRegression()
        #reg.fit(x,y)
        #output=reg.predict([[float(self.text1.get())]])
        self.label2.configure(text='Male Salary {:.2f}'.format(sum1))
        self.label3.configure(text='Female Salary {:.2f}'.format(sum2))
        self.label4.configure(text='male Salary mean {:.2f}'.format(mean1))
        self.label5.configure(text='Female Salary mean {:.2f}'.format(mean2))
        #self.label4.configure(text='male Salary mean {:.2f}'.format(std1))
        #self.label4.configure(text='male Salary mean {:.2f}'.format(std2))
        
        
        
        


root=Tk()
root.title('Prediction Dialog Box')
root.geometry('500x500')
obj=prediction(root)
root.configure(bg='khaki')
root.mainloop()
