'''
# Pandas 
the main module which is used data analysis and data visualitation and eda( exploratory data analysis)
The main data Structure and series and data frame 
Series is one dimensional data structure 
'''
import pandas as pd 
#  series with values
#S=pd.Series([2,5,6,7,8])
#print(S)
#S=pd.Series(['A','B','C','D','E'],index=[501,502,503,504,505])
#print(S)

#S=pd.Series([501,502,503,504,505],index=['A','B','C','D','E'])
#print(S)
#S=pd.Series(7,index=[501,502,503,504,507])
#print(S)
'''
d={'empno':[101,102,103,104],
     'name':['A','B','C','D'],
    'age':[21,25,26,22]}

s=pd.Series(d)
print(s)
#Data Frame
Data frame is type of data structure
df=pd.DataFrame([20,25,28,35,35])
print(df)
'''
x=[['Raj', 25],['Amit', 25],['Rani', 25],['Rahul', 25]]
df=pd.DataFrame(x,columns=['Name','Age'])

print(df)