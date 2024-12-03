# linear_regression.py

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load and prepare the data

df = pd.read_csv('ecommerce.csv')

# Prepare features and target variable
X = df[["Avg. Session Length", "Time on App", "Time on Website", "Length of Membership"]]
y = df['Yearly Amount Spent']

# Train the linear regression model
lm = LinearRegression()
lm.fit(X, y)

# Save the model to a file
joblib.dump(lm, 'model.pkl')

# Function to make predictions with the trained model
def predict_amount(avg_session_length, time_on_app, time_on_website, length_of_membership):
    input_data = [[avg_session_length, time_on_app, time_on_website, length_of_membership]]
    prediction = lm.predict(input_data)
    return prediction[0]
