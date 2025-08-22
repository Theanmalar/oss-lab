import pandas as pd
from sklearn.preprocessing import MinMaxscaler,LabelEncoder
import numpy as np

data={'Name':['Ragu','priya','anu','karan','Ragu','janu'],'Age':[25,np.non,22,28,30,25],'Salary':[50000,54000,58000,np.non,60000,50000],'Gender':['Male','Female','Female','Male','Male','Female']}
#load dataset into dataframe
df=pd.DataFrame(data)
print("Original Data:\n",df)
#Remove duplicates
df.drop_duplicate(inplace=True)
#handle Missing values
df['Age'].fillna(df['Age'],mean(),inplace=True)
df['Salary'].fillna(df['Salary'],mean(),inplace=True)
#Normalize numerical columns 
Scaler=MinMaxScaler()
df[['Age','salary']]=Scaler.fit_transform(df[['Age','Salary']])
#Encode categorical columns
Encoder=LabelEncoder()
df['Gender']=Encoder.fit_transform(df[['Gender']])
#feature Enginering
df['Salary_per_age']=df['Salary']/df['Age']
#display
print("\n Proceesd Data:\n",df)



