# menuprog.py 
# Menu program 

from tkinter import *
import os

class Testmenu:

    # Constructor
    def __init__(self, root):
        self.f = Frame(root, height=350, width=500,bg='black')
        self.f.pack()

        self.main_lbl=Label(self.f, text='Empolyee Salary Prediction',bg='yellow',fg='red', font=('Arial', -20, 'bold underline'))
        self.main_lbl.place(x=60, y=80)
       
        # Create menubar
        self.menubar=Menu(root)
        root.config(menu=self.menubar)            # attach the menubar to root
        # Now create Single menubar operation menu
        self.mysql_menu=Menu(root, tearoff=0)

        self.menubar.add_cascade(label='Data Conversion', menu=self.mysql_menu)
        # Now create menu items under menubar 
        self.mysql_menu.add_command(label='Build df', command=self.create_df)
        self.mysql_menu.add_command(label='Build CSV', command=self.create_empsal)
        self.mysql_menu.add_command(label='Convert to Excel', command=self.csv_to_xls)
         
        # Now add a separator
        self.mysql_menu.add_separator()
        # Now create a Exit menu
        self.mysql_menu.add_command(label='Exit', command=root.destroy)

        # Now create Data Maintenance operation menu
        self.data_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Reports',menu=self.data_menu)
        #self.data_menu.add_command(label='Display update df', command=self.rep1)
        self.data_menu.add_command(label='Gender wise Sum', command=self.gender_wise_sum)
        #self.data_menu.add_command(label='Mean', command=self.rep1)
        self.data_menu.add_command(label='State wise Mean', command=self.state_wise_mean_calc)
        self.data_menu.add_command(label='State Wise Total', command=self.state_wise_total_calc)
        #self.data_menu.add_command(label='Mean', command=self.rep3)
        self.data_menu.add_command(label='Scatter Plot', command=self.plot)
        
        # Prediction Menu
        self.predict_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Prediction', menu=self.predict_menu)
        self.predict_menu.add_command(label='Predict', command=self.prediction)
         

    def create_df(self):
        os.system("python.exe create_df1.py")
        #print("hello")
    def create_empsal(self):
        os.system("python.exe create_empsal.py")
    def csv_to_xls(self):
        os.system("python.exe csv_to_xls.py")
    
    def rep1(self):
        os.system("python.exe rep1.py")
    def state_wise_mean_calc(self):    
        os.system("python.exe state_wise_mean_calc.py")
    def state_wise_total_calc(self):
        os.system("python.exe state_wise_total_calc.py")
    def gender_wise_sum(self):
        os.system("python.exe gender_wise_sum.py")
    def plot(self):
        os.system("python.exe scatter_plot.py")
        
    def prediction(self):
        os.system("python.exe prediction.py")     
#=====================================================================================================
  
root=Tk()
root.title('ML project is Here')

obj=Testmenu(root)
root.geometry('400x225')
root.configure(bg='black')
root.mainloop()

                                 
        
        
        
        
                 
