import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

# Generate synthetic data
x, y = make_regression(n_features=1, n_targets=1, n_informative=1, n_samples=100, random_state=13, noise=80)
clf = LinearRegression()
clf.fit(x, y)

# Plot the data and the initial linear regression line
plt.scatter(x, y, marker="+")
plt.plot(x, clf.predict(x), color='red', linestyle='solid', linewidth=2, label='LinearRegression fit')
plt.title("Graph for Gradient Descent")
plt.xlabel("X Random")
plt.ylabel("Y Random")

# Print the initial coefficients
print("Initial intercept (b):", clf.intercept_)
print("Initial slope (m):", clf.coef_)

# Initialize parameters for gradient descent
m = 100
b = -120
epochs = 40
lr = 0.2
n = len(y)  # Number of samples

# Perform gradient descent
for i in range(epochs):
    y_pred = m * x + b
    error = y - y_pred.ravel()
    
    # Calculate the gradients
    slope_m = -2 * np.sum(error * x.ravel()) / n
    slope_b = -2 * np.sum(error) / n
    
    # Update the parameters
    m -= lr * slope_m
    b -= lr * slope_b

    # Print updated parameters at each epoch
    print(f"Epoch {i+1}:")
    print("Intercept (b):", b)
    print("Slope (m):", m)
    print("\n")
    
    # Plotting the lines for each epoch (optional, may clutter the graph)
    plt.plot(x, m * x + b,label='b={}'.format(b), linewidth=1)

# Final plot configuration
plt.grid()
plt.legend()
plt.show()
