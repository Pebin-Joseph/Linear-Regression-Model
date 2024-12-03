Yearly Amount Spent Prediction Model
This project uses a linear regression model to predict the yearly amount spent by customers based on their online activities. The model is trained on a dataset containing customer information such as session length, time spent on the app and website, and the length of membership. The goal of this project is to predict how much a customer is likely to spend in a year based on these features.

Table of Contents
Project Overview
Dataset
Model
Usage
App
Requirements
License
Project Overview
This project demonstrates how to use a linear regression model to predict yearly spending based on various customer activity metrics. It also includes a simple Gradio web app for interacting with the model.

The following features are used for prediction:

Avg. Session Length: The average session length of the user.
Time on App: The total time spent by the user on the app.
Time on Website: The total time spent by the user on the website.
Length of Membership: The number of years the user has been a member.
Dataset
The dataset used in this project contains the following columns:

Email: Email address of the customer.
Address: The physical address of the customer.
Avatar: Avatar color for the user.
Avg. Session Length: The average session length in minutes.
Time on App: The total time spent on the app (in minutes).
Time on Website: The total time spent on the website (in minutes).
Length of Membership: The number of years the user has been a member.
Yearly Amount Spent: The target variable, representing the total yearly spending of the user.
Model
The linear regression model is implemented using scikit-learn and trained on the dataset to predict the yearly spending based on the customer activity features.

Training: The model is trained using LinearRegression from sklearn.linear_model.
Evaluation: Model performance is evaluated using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).
Usage
To use the model, follow these steps:

1. Clone the repository
Clone the repository to your local machine:

pip install -r requirements.txt

python train_model.py

python app.py
python app.py

Requirements
This project requires the following Python packages:

gradio pandas scikit-learn joblib matplotlib seaborn

