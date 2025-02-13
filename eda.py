import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Read the data from filed
df = pd.read_csv("Churn_Data.csv")

# Display first few rows
print(df.head())

# Get info of Data
print(df.info())

# Replace blank values with 0 and convert to float
df["TotalCharges"] = df["TotalCharges"].replace(" ", "0")
df["TotalCharges"] = df["TotalCharges"].replace(" ", "0").astype(float)

# Check info after conversion
print(df.info())

# Find total null values
Number_Of_Null_Values = df.isnull().sum().sum()
if Number_Of_Null_Values != 0:
 df = df.dropna()
 print(df.head())  # Display after dropping nulls
else:
 print("No Null values present")

# Get statistical info#
print(df.describe())

# Convert SeniorCitizen column to Yes/No
def conv(value):
   if value == 1 :
    return "Yes"
   else:
       return "No"

df["SeniorCitizen"] = df["SeniorCitizen"].apply(conv)
print(df.head(33))

# Countplot of Churn column
sns.countplot(x='Churn', data=df)
plt.show()

# Pie chart for Churn distribution
churn_counts = df["Churn"].value_counts()
plt.pie(churn_counts, labels=churn_counts.index, autopct="%1.2f%%")
plt.show()

# Get sum of duplicates
print(df.duplicated().sum())

#To get the graph of paperlessbilling
sns.countplot(x = 'PaperlessBilling' , data=df )
plt.show()

#To get pie chart of Streaming Movies
Streaming_Movies_counts = df["StreamingMovies"].value_counts()
plt.pie(Streaming_Movies_counts , labels=Streaming_Movies_counts.index  , autopct = "%1.2f%%" )
plt.title("Users Streaming Movies")
plt.show()

#To see how many of users use Fiber Optics
Fiber_Optics = df["InternetService"].str.lower().eq("Fiber Optic").sum()
print(Fiber_Optics)

#To get a piechart of the type internet services users are using
Internet_services_count = df["InternetService"].value_counts()
plt.pie(Internet_services_count , labels = Internet_services_count.index , autopct = "%1.2f%%" , colors =["black" , "brown" , "blue"] )
plt.show()


#To get Historogram for how many of the have partners
Partners_count = df["Partner"].value_counts()
plt.bar(Partners_count.index , Partners_count.values , color = ["orange" , "blue"])
plt.title("User having partners")
plt.show()

#To get eda graph of monthly charges
MonthlyCharges = df["MonthlyCharges"].value_counts()
sns.kdeplot(MonthlyCharges , color = "blue" )
plt.title("Monthly Charges")
plt.show()


#To get Payment Method
Payment_Method_count = df["PaymentMethod"].value_counts()
sns.countplot( x ="PaymentMethod",  data = df)
plt.show()






