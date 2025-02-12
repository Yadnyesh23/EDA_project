import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#To read the data from file
df = pd.read_csv("Churn_Data.csv")
print(df.head())

#To get info of Data
print(df.info())

#To replace black values with 0
df["TotalCharges"] = df["TotalCharges"].replace(" " , "0")
df["TotalCharges"] = df["TotalCharges"].astype("float")

df.info()

#To find total null values
Number_Of_Null_Values = df.isnull().sum().sum()
if(Number_Of_Null_Values != 0):
    print(df.dropna())
else:
    print("No Null values present")

#To get statistic info
print(df.describe())

#To get sum of duplicates
print(df.duplicated().sum())

def conv(value):
 if value == 1:
    return "yes"
 else:
     return "no"
df["SeniorCitizen"] = df["SeniorCitizen"].apply(conv)
print(df.head())

#To get a graph of how many of them are churned out and how many of them not
sns.countplot( x = 'Churn' , data = df)
plt.show()

#To get in the form of piechart
gb = df.groupby("Churn").agg({'Churn' : "count"})

plt.pie(gb['Churn'] , labels = gb.index ,autopct = "%1.2f%%")
plt.show()









