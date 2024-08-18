import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Synthetic dataset creation
# Features: [engine_temp, rpm, speed, error_code]
X = np.array([
    [90, 3000, 60, 1], [95, 3200, 65, 1], [100, 3400, 70, 2],
    [85, 2800, 55, 0], [92, 3100, 62, 1], [105, 3500, 75, 2],
    [88, 2900, 58, 0], [97, 3300, 68, 1], [102, 3600, 72, 2],
    [93, 3250, 66, 1], [89, 3050, 60, 0], [98, 3400, 70, 2]
])
# Labels: 0 (no fault), 1 (minor fault), 2 (major fault)
y = np.array([0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Save the trained model to a file
joblib.dump(model, 'vehicle_fault_model.pkl')
