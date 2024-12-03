# app.py

import gradio as gr
import joblib
from linear_regression import predict_amount  # Import the predict function from linear_regression.py

# Load the saved model (optional, in case you want to load it directly in app.py)
# lm = joblib.load('model.pkl')  # This is also an option, but we use the imported function instead

# Prediction function using the imported model
def gradio_predict(avg_session_length, time_on_app, time_on_website, length_of_membership):
    prediction = predict_amount(avg_session_length, time_on_app, time_on_website, length_of_membership)
    return f"Predicted Yearly Amount Spent: ${prediction:.2f}"

# Define components for input and output
avg_session_length = gr.Number(label="Average Session Length")
time_on_app = gr.Number(label="Time on App")
time_on_website = gr.Number(label="Time on Website")
length_of_membership = gr.Number(label="Length of Membership")

# Output component
output = gr.Textbox(label="Prediction")

# Gradio Interface
app = gr.Interface(
    fn=gradio_predict, 
    inputs=[avg_session_length, time_on_app, time_on_website, length_of_membership], 
    outputs=output,
    title="Yearly Amount Spent Prediction"
)

# Launch the app
app.launch()
