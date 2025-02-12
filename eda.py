import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from file
df = pd.read_csv("Churn_Data.csv")

# Display first few rows
print(df.head())

# Get info of Data
print(df.info())

# Replace blank values with 0 and convert to float
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

# Get statistical info
print(df.describe())

# Convert SeniorCitizen column to Yes/No
def conv(value):
    return "yes" if value == 1 else "no"

df["SeniorCitizen"] = df["SeniorCitizen"].apply(conv)
print(df.head())

# Countplot of Churn column
sns.countplot(x='Churn', data=df)
plt.show()

# Pie chart for Churn distribution
churn_counts = df["Churn"].value_counts()
plt.pie(churn_counts, labels=churn_counts.index, autopct="%1.2f%%")
plt.show()

# Get sum of duplicates
print(df.duplicated().sum())








