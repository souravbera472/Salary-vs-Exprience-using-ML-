from tkinter import *
from tkinter import messagebox as msg
import pandas as pd
from sklearn import linear_model
import numpy as np
import math



class prediction:
    def __init__(self,root):
          self.f = Frame(root,height=600,width=500,bg='white')
          self.f.pack()    # Place the frame on root window
          self.f1 = Frame(root,height=600,width=500,bg='white')
          self.f1.pack()    # Place the frame on root window
           
          # Creating label widgets
          self.label1 = Label(self.f,text='S.D. Genderwise',bg='white',font=('Arial', 20))
          self.label15 = Label(self.f,text='Female',bg='white',font=('Arial', 18))
          self.label2 = Label(self.f,text='',fg='black',bg='white',font=('Arial', 14))
          self.label3 = Label(self.f,text='',fg='black',bg='white',font=('Arial', 14))
          self.label4 = Label(self.f,text='',fg='black',bg='white',font=('Arial', 14))

          self.label25 = Label(self.f1,text='Male',bg='white',font=('Arial', 18))
          self.label5 = Label(self.f1,text='',fg='black',bg='white',font=('Arial', 14))
          self.label6 = Label(self.f1,text='',fg='black',bg='white',font=('Arial', 14))
          self.label7 = Label(self.f1,text='',fg='black',bg='white',font=('Arial', 14))
          
          
          # Buttons
          self.button1 = Button(self.f1,text='Calculate', font=('Arial', 14), bg='Slategray3',
                                 fg='Black', command=self.func)
          self.button2 = Button(self.f1,text='Exit', font=('Arial', 14), bg='Slategray3',
                                 fg='Black', command=root.destroy)
          

          # Placing the widgets using grid manager
          self.label1.grid(row=0,column=0)
          self.label15.grid(row=1, column=0)
          self.label2.grid(row=2,column=0)
          self.label3.grid(row=3,column=0)
          self.label4.grid(row=4,column=0)

          
          self.label25.grid(row=0, column=0)
          self.label5.grid(row=1,column=0)
          self.label6.grid(row=2,column=0)
          self.label7.grid(row=3,column=0)
          self.button1.grid(row=4,column=0)
          self.button2.grid(row=5,column=0)
          

          
    def func(self):
        df=pd.read_csv("empsal.csv")
        sex=list(df['sex'])
        sal=list(df['salary'])
        hra=list(df['hra'])
        y=[]
        sum1=0
        sum2=0
        h1=0
        s1=0
        h2=0
        s2=0
        m=0
        n=0
        for i,j,k in zip(sex,sal,hra):
            if i=='M':
                sum1=sum1+(float(k)+float(j))
                h1=h1+float(k)
                s1=s1+float(j)
                m=m+1
            else:
                sum2=sum2+(float(k)+float(j))
                h2=h2+float(k)
                s2=s2+float(j)
                n=n+1
        meanf1=sum2/n
        meanf2=h2/n
        meanf3=s2/n

        meanm1=sum1/m
        meanm2=h1/m
        meanm3=s1/m
        
        sdf1=0
        sdf2=0
        sdf3=0
        sdm1=0
        sdm2=0
        sdm3=0
        

        for i,j,k in zip(sex,sal,hra):
            if i=='M':
                sdf1=sdf1+((float(k)+float(j))-meanf1)**2
                sdf2=sdf2+(float(k)-meanf2)**2
                sdf3=sdf3+(float(j)-meanf3)**2
                
            else:
                sdm1=sdm1+((float(k)+float(j))-meanm1)**2
                sdm2=sdm2+(float(k)-meanm2)**2
                sdm3=sdm3+(float(j)-meanm3)**2
               
       
        self.label2.configure(text='S.D. of Total Female Salary = {:.2f}'.format((sdf1/n)**.5))
        self.label3.configure(text='S.D. of Female Salary = {:.2f}'.format((sdf3/n)**.5))
        self.label4.configure(text='S.D. of Female HRA = {:.2f}'.format((sdf2/n)**.5))

        
        self.label5.configure(text='S.D. of Total Male Salary = {:.2f}'.format((sdm1/m)**.5))
        self.label6.configure(text='S.D. of Male Salary = {:.2f}'.format((sdm3/m)**.5))
        self.label7.configure(text='S.D. of Male HRA = {:.2f}'.format((sdm2/m)**.5))
        
        
        
        


root=Tk()
root.title('Salary Breakdown Genderwise')
obj=prediction(root)
root.configure(bg='white')
root.geometry('600x500')
root.mainloop()
