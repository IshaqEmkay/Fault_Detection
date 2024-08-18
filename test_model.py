import joblib
import numpy as np

# Load the trained model
model = joblib.load('vehicle_fault_model.pkl')

# Define a sample input for testing
# Adjust these values based on your model's expected input format and range
sample_input = np.array([[90, 3000, 60, 1]])

# Predict the fault
prediction = model.predict(sample_input)
print('Prediction:', prediction)
