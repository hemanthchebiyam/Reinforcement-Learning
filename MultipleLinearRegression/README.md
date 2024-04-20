# [Project A] Linear Regression Model for Predicting Y from X

1.	Building the Linear Regression Model:

![A1](/resources/A1.png) 

2.	Model Accuracy Evaluation:

![A2](/resources/A2.png) 

3.	Interpretation of Coefficient Estimate:

![A3](/resources/A3.png)

4. Dataset: [Linear Regression - Example Data.csv](https://github.com/hemanthchebiyam/Reinforcement-Learning/blob/main/MultipleLinearRegression/Health%20Insurance%20Dataset.csv)
   
5. Code Implementation: [Linear_Regression_Model.py](https://github.com/hemanthchebiyam/Reinforcement-Learning/blob/main/MultipleLinearRegression/Linear_Regression_Model.py)

The intercept represents the predicted value of Y when X is zero.
Here, the intercept is 6.58
 
The slope indicates the direction and magnitude of change in Y for a unit increase in X.
Here, the slope is 0.633. It means that for every one-unit increase in X, Y is expected to increase by 0.633 units.
#


# [Project B] Multiple linear regression model for predicting insurance charges

1.	Creating a new dependent variable Y

 ![B1](/resources/B1.png)

2.	Dataset Splitting

  ![B2](/resources/B2.png)

3.	Plotting Y vs Number of Children. Does it seem like the dependent variable Y is related to number of children?

 ![B4](/resources/B4.png)
 
As we can see from the bar plot, the average risk score remains relatively constant across different categories of the 'children' variable, and it indicates that the number of children may not have a significant impact on the risk score. There is no consistent pattern where Y increases or decreases as the number of children goes up.

4.	Multiple Linear Regression Model

 ![B3](/resources/B3.png)

 
5.	Interpretation of Coefficient Estimates

 ![B5](/resources/B5.png)
 
Based on the coefficient estimates that we got from the model:
a.	Sex (Female/Male):

-	encoder__sex_female: This coefficient represents the average change in the risk score Y for females compared to males, holding other variables constant. Since the coefficient is negative (-0.000075), it suggests that, on average, females have a slightly lower risk score than males, though the difference is very small.

-	encoder__sex_male: Similarly, this coefficient represents the average change in the risk score Y for males compared to females. Since it's positive (0.000075), it suggests that, on average, males have a slightly higher risk score than females, though again, the difference is very small.

b.	Smoker (No/Yes):

-	encoder__smoker_no: This coefficient represents the average change in the risk score Y for non-smokers compared to smokers, holding other variables constant. With a negative coefficient (-0.188947), it indicates that, on average, non-smokers have a lower risk score than smokers.

-	encoder__smoker_yes: Conversely, this coefficient represents the average change in the risk score Y for smokers compared to non-smokers. With a positive coefficient (0.188947), it suggests that, on average, smokers have a higher risk score than non-smokers.

c.	Age and BMI:

-	remainder__age: This coefficient represents the change in the risk score Y for a one-unit increase in age, holding other variables constant. With a positive coefficient (0.004141), it indicates that, on average, older individuals tend to have a slightly higher risk score than younger individuals, assuming all other variables remain constant.

-	remainder__bmi: Similarly, this coefficient represents the change in the risk score Y for a one-unit increase in BMI, holding other variables constant. With a positive coefficient (0.005211), it suggests that, on average, individuals with higher BMI tend to have a slightly higher risk score than individuals with lower BMI, assuming all other variables remain constant.

