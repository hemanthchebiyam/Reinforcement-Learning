# This code is written by Hemanth Chebiyam.
# Email: hc3746@rit.edu

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Loading the dataset
data = pd.read_csv("C:\Hemanth\Rochester_Institute_of_Technology\Courses\Spring24\SWEN-711\Homework3\Linear Regression - Example Data.csv")

# Split the data into explanatory variable (X) and dependent variable (Y)
X = data[['X']]
Y = data['Y']

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# Predict on the testing set
Y_pred = model.predict(X_test)

# Calculate R^2 and other metrics
r2 = r2_score(Y_test, Y_pred)
print("R2 = ", r2)

mse = mean_squared_error(Y_test, Y_pred)
print("Mean squared error = ", mse)

rmse = np.sqrt(mse)
print("Root mean squared error = ", rmse)

print("Intercept = ", model.intercept_)
print("Slope = ", model.coef_[0])