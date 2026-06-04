from itertools import groupby

import pandas as pd
import matplotlib.pyplot as plt
from plotly.graph_objs.waterfall import Totals

df=pd.read_csv("sales_data.csv")

df.dropna()
#print(df.head())

df["Total"]=df["Price"]*df["Quantity"]
#print(df.head())

groupby_city=df.groupby("City")["Total"].sum().reset_index()
#print(df["Total"])

groupby_category=df.groupby("Category")["Total"].sum().reset_index()
#print(df["Total"])

print(groupby_city)
print(groupby_category)

most_sales=df.groupby("Product")["Quantity"].sum()
print(most_sales)

#mean price
avarage_price=df.groupby("Product")["Price"].mean()
print("Avarage price",avarage_price)

#payment
payment=df.value_counts("PaymentMethod")
print(payment)

#graf
groupby_category.plot.bar(
    x="Category",
    y="Total",
    title="Total sales by category",
    figsize=(10, 6)
)

groupby_city.plot.bar(
    x="City",
    y="Total",
    title="Total sales by city",
    figsize=(10, 6),
    color="red"
)
plt.show()

payment.plot.pie(y="PaymentMethod", title="Payment method distribution", autopct="%1.1f%%")
plt.show()

df.plot(x="Date", y="Total")
plt.show()