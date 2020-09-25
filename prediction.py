from tkinter import *
from tkinter import messagebox as msg
import pandas as pd
from sklearn import linear_model
import numpy as np



class prediction:
    def __init__(self,root):
          self.f = Frame(root, height=350, width=500,bg='khaki')
          self.f.pack()    # Place the frame on root window
           
          # Creating label widgets
          self.label1 = Label(self.f,text='Experience',bg='khaki',fg='black',font=('Arial', 14))
          self.text1 = Entry(self.f, text='',font=('Arial', 14),width=6)
          self.label2 = Label(self.f,text='',font=('Arial', 14),fg='red')
          
          
          
          # Buttons
          self.button1 = Button(self.f,text='Calculate', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.func)
          self.button2 = Button(self.f,text='Reset', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.reset)
          self.button3 = Button(self.f,text='Exit', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=root.destroy)

          # Placing the widgets using grid manager
          self.label1.grid(row=1, column=0)
          self.text1.grid(row=1,column=2)
          self.button1.grid(row=3,column=0)
          self.button2.grid(row=4,column=0)
          self.button3.grid(row=5,column=1)
          self.label2.grid(row=3,column=2)
    def func(self):
        df=pd.read_csv("empsal.csv")
        sal=list(df['salary'])
        hra=list(df['hra'])
        y=[]
        for i,j in zip(sal,hra):
            y.append(float(i)+float(j))
        x=df.iloc[:,6:7]
        x1=[]
        x1.append(x)
        reg=linear_model.LinearRegression()
        reg.fit(x,y)
        output=reg.predict([[float(self.text1.get())]])
        self.label2.configure(text='Salary {:.2f}'.format(output[0]))
        
    def reset(self):
        self.text1.delete(0,END)
        self.label2.configure(text='')
        
        
        
        


root=Tk()
root.title('Prediction Dialog Box')
root.geometry('400x400')
obj=prediction(root)
root.configure(bg='khaki')
root.mainloop()
