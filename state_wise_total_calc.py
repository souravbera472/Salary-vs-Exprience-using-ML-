# Program name : state_wise_total_calc.py
# Data science operations on empsal.csv
# State Wise figures of salary,hra,conv,total on empsal.csv
# Plot a bar graph where states would be in X axis and total figures
# would be in Y axis

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

empsal_df = pd.read_csv('empsal.csv', index_col='empno', parse_dates=['dob'])
print(empsal_df.info())
# Drop null values. axis=0 for rowwise drop, axis=1 for col wise.
# 'any' means - drop the row if any col in that row is null
# 'all' means = drop the row if all cols in that row is null 
empsal_df.dropna(axis=0, how='any', inplace=True)       
print(empsal_df.info())

# Add columns Conv. Salary
empsal_df['spallow']=empsal_df.salary * 0.15
empsal_df['total']= empsal_df.salary + empsal_df.hra + empsal_df.spallow
print(empsal_df.head())
sum_list = empsal_df.groupby(['state'])['salary','hra','spallow','total'].sum()
print(sum_list)

# Plotting a bar chart of mean figures of Salary, HRA, CONV, Total
sum_list.plot(kind='bar')
plt.title('State Wise Figures Of\n salary, hra, conv & total')
plt.xlabel('States-->')
plt.ylabel('Total Figures')
plt.tight_layout()
plt.legend(loc='best')
plt.show()

#x = input('Press Enter to continue')











