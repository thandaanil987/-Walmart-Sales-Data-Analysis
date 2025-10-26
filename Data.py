import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

# Load the dataset
df = pd.read_csv(r"C:\Users\thand\OneDrive\Desktop\data analyst projects\walmart-analysis PY\Walmart.csv")
# Show first few rows
print("Dataset Shape:", df.shape)
#first 5 rows
print(df.head())
#last five rows
print(df.tail())
#missing value
print(df.isnull().sum())

#date convertion
df['Date']=pd.to_datetime(df['Date'],dayfirst=True,errors='coerce')
print(df['Date'])
df=df.sort_values('Date')
print(df)

#data exploration
# 1) sales over time
plt.figure(figsize=(12,5))
plt.plot(df['Date'],df['Weekly_Sales'],color="blue")
plt.title("walmarkt weekly sales over time")
plt.xlabel("date")
plt.ylabel("weekly sales")
plt.show()

#Weekly sales per store
plt.bar(df["Store"],df['Weekly_Sales'],color="blue")
plt.title("weekly sales per store")
plt.xlabel("store")
plt.ylabel("weekly sales")
plt.show()

# holoday vs non holiday sales
holiday_sales=df.groupby("Holiday_Flag")['Weekly_Sales'].mean()
sns.barplot(x=holiday_sales.index,y=holiday_sales.values,palette="coolwarm")
plt.title("Holiday vs Non-Holiday Sales")
plt.xlabel("holiday flag (0=n0, 1=yes)")
plt.ylabel("avg weekly sales")
plt.show()

#Temperature vs sales 
plt.figure()
sns.scatterplot(x="Temperature",y="Weekly_Sales",data=df,color="green")
plt.title("temp vs weekly sales")
plt.show()

#correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
plt.title("correlation heatmap")
plt.show()


#relation between cpi and weekly sales 
plt.figure()
sns.scatterplot(x='CPI',y="Weekly_Sales",data=df,color='purple')
plt.title("CPI vs Weekly sales")
plt.show()