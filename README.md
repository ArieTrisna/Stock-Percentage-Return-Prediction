# Stock Percentage Return Prediction Using Linear Regression

## Objective
To analyze and predict how much of percentage return daily based on past historical data and technical indicators such as RSI, Moving Average, and Moving Average Convergence Divergence. Prediction are made by applying supervised learning methods with Linear Regression model.

## Methodology
1. Data Collecting and Cleaning
2. Explatory Data Analysis
3. Feature Engineering
4. Model Training & Evaluation
5. Summary

## Dataset
In this project we are using yfinance API to collect the data. 
Stock that are used in this topic is BBCA.JK, it is one of the biggest bank from Indonesia.

## Summary
Linear Regression surprisingly performs quite good for stock return prediction, even if the stock market or financial market is really volatile and there are so many things that could affect it's movement, but the machine learning can predict pretty well using historical data and technical indicators. It is true that the value is off a little bit from true value but Linear Regression can catch bit of momentum when they go down and go up. With more suitable features and tuning in the future, the model can be more accurate than what it is now.
Evaluation Metrics Results:
1. MAE = 0.042
Means that on average the model's prediction are approx. 0.042 away from the true value
2. MSE = 0.0023
Means that on average the squared prediction errors are approx. 0.0023
3. R-squared = -0.197 
Indicates that the model can explain approximately -19.7% of the variance in values
4. RMSE = 0.048
Indicates that on average the model's predictions have an error of approximately 0.048 in the same units as the values.
