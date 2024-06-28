import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

df=pd.read_csv('apple_products.csv')

print(df.head(2))
print(df.describe())
print(df.isnull().sum())

high_rated=df.sort_values(by=["Star Rating"], ascending=False)
high_rated=high_rated.head(10)
print(high_rated['Product Name'])

iphone=high_rated['Product Name'].value_counts()
labels=iphone.index
counts=high_rated["Number Of Ratings"]
figure=px.bar(high_rated,x=labels,y=counts,title="Number of Ratings of Highest Rated Iphone")
figure.show()

iphone=high_rated['Product Name'].value_counts()
labels=iphone.index
counts=high_rated["Number Of Reviews"]
figure=px.bar(high_rated,x=labels,y=counts,title="Number of Reviews of Highest Rated Iphone")
figure.show()

figure = px.scatter(
    data_frame=df,
    x="Number Of Ratings",
    y="Discount Percentage",
    size="Sale Price",
    trendline="ols",
    title="Relationship between Discount perentage and the Number of Rating of the iPhone"
)

# Showing the plot
figure.show()

figure = px.scatter(
    data_frame=df,
    x="Number Of Ratings",
    y="Sale Price",
    size="Discount Percentage",
    trendline="ols",
    title="Relationship between Discount perentage and the Number of Rating of the iPhone"
)

# Showing the plot
figure.show()
