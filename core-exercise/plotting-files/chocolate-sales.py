import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Data 1 - Chocolate Sales per Country (Country and Boxes Shipped)
data = pd.read_csv("C:\\Users\\User\\Desktop\\Coding\\Chocolate_Sales.csv.csv")
plt.rcParams.update({'font.size': 8})
sales_person = np.array(data['Sales Person'])
country = np.array(data['Country'])
date = np.array(data['Date'])
amt = np.array(data['Amount'])
bxs_shp = np.array(data['Boxes Shipped'])

countries, c_count = np.unique(country, return_counts=True)
fig, ax = plt.subplots()
color = ("Pink") 
plt.bar(countries, c_count, color=color)
plt.title("Chocolate Sales per Country")
ax.set_xlabel('Boxes Shipped')
plt.figure(figsize=(10,6))

plt.show()

#Data 2 - Product
product = np.array(data['Product'])

product, c_count = np.unique(product, return_counts=True)
fig, ax = plt.subplots()
color = ("Gray") 
plt.barh(product, c_count, color=color)
plt.title("Chocolate Type")
ax.set_xlabel('Item Count')
plt.figure(figsize=(10,6))
plt.show()

#Data 3 - Dates and Amount
df = pd.DataFrame(data, columns=['Date']
                  )
df.Date = pd.to_datetime(df.Date, format="mixed")

plt.plot(df.Date, '.')
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.title("Date and Amount")
plt.show()

#Data 4 - Sales Person
sales_person = np.array(data['Sales Person'])

sales_person, c_count = np.unique(sales_person, return_counts=True)
fig, ax = plt.subplots()
color = ("Maroon") 
plt.barh(sales_person, c_count, color=color)
plt.title('Sales Person')
ax.set_xlabel('Amount Bought')
plt.figure(figsize=(10,6))
plt.show()
