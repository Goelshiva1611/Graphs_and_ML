import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the data
df = pd.read_csv('placement.csv')
df.head()

# Define the features and the target
x = df.iloc[:, 0:1].values
y = df.iloc[:, -1].values

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)

# Initialize and train the Linear Regression model
clf = LinearRegression()
clf.fit(x_train, y_train)

# Predict the value for a specific test sample
predicted_value = clf.predict(x_test[0].reshape(1,1))
print(f"Predicted value for first test sample: {predicted_value}")

# Plotting the results
plt.scatter(df['cgpa'], df['package'], color='blue', label='Actual Data',marker="+")
plt.plot(x_train, clf.predict(x_train), color='red', linewidth=2, label='Regression Line')
plt.xlabel("CGPA")
plt.ylabel("Package")
plt.title("CGPA vs Package with Linear Regression")
plt.legend()
plt.grid(True)
plt.show()

m=clf.coef_
b=clf.intercept_
print(f"Intercept value is : {b}")
print(f"Slope value is : {m}")
print(m * 8.58 + b)