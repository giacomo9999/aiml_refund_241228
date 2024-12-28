import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv("csmith_data.csv")
scaler = StandardScaler()
model = LogisticRegression()

# Separate the features (X) and the target variable (y)
X = data.drop("Outcome", axis=1)  # Features (independent variables)
y = data["Outcome"]  # Target (dependent variable)
X_scaled = scaler.fit_transform(X)  # normalize the imported data to 1(?)

# Split the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.25, random_state=42
)

print(X)
print("-----")
print(y)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

new_customer = [[1000, 0.2, 10, 9]]  # data for flagrant fraud
new_customer2 = [[50, 7, 2, 1]]  # data for honest law-abiding citizen

# Predict the outcome (0 = no diabetes, 1 = diabetes)
prediction = model.predict(new_customer)
prediction2 = model.predict(new_customer2)

print(f"Refund Prediction: {prediction[0]}")
print(f"Refund Prediction: {prediction2[0]}")
