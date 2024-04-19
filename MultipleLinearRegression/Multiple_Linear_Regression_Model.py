# This code is written by Hemanth Chebiyam.
# Email: hc3746@rit.edu

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
data = pd.read_csv("C:\Hemanth\Rochester_Institute_of_Technology\Courses\Spring24\SWEN-711\Homework3\Health Insurance Dataset.csv")
print(data.head(5))

# 1. Creating Risk Score (Y)
# Normalizing insurance charges to a risk score
data['Y'] = (data['charges'] - data['charges'].min()) / (data['charges'].max() - data['charges'].min())

print(data['Y'].head(10))
# 2. Splitting dataset
X = data[['age', 'sex', 'bmi', 'smoker']]
y = data['Y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Encode categorical variables
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1, 3])], remainder='passthrough')
X_train = ct.fit_transform(X_train)
X_test = ct.transform(X_test)

# plt.scatter(data['children'], data['Y'])
average_y_children = data.groupby('children')['Y'].mean()
plt.bar(average_y_children.index, average_y_children.values)
plt.xlabel('Number of Children')
plt.ylabel('Risk Score (Y)')
plt.title('Relationship between Y and Number of Children')
plt.show()

# 4. Multiple Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluating the model
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f'R^2 Score: {r2}')
print(f'Mean Squared Error: {mse}')
print(f'Root mean squared error = {rmse}')

# 5. Interpretation of Coefficients
coefficients = pd.DataFrame({'Variable': ct.get_feature_names_out(input_features=X.columns), 'Coefficient': model.coef_})
print(coefficients)