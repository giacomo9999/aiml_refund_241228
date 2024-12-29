import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("order-data.csv")
scaler = StandardScaler()
# model = LogisticRegression()
# Logistic Regression doesn't seem to work, for reasons that are utterly beyond me
model = DecisionTreeClassifier()

# Separate the features (X) and the target variable (y)
X = data.drop("Outcome", axis=1)  # Features (independent variables)
y = data["Outcome"]  # Target (dependent variable)
X_scaled = scaler.fit_transform(X)  # normalize the imported data to 1(?)

# Split the data into training and test sets
# (Adjust test size for data supplied...csmith_data_2.csv has six 'training' cases and four 'test' cases, so 'test_size' for that dataset should be 0.4)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.4, random_state=None, shuffle=False
)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

honest_customer = [[25, 3, 0, 1]]  # data for honest law-abiding citizen
dishonest_customer = [[1154, 0.1, 10, 15]]  # data for flagrant fraud

# Predict the outcome (0 = refund denied, 1 = refund granted)
prediction_honest = model.predict(honest_customer)
prediction_dishonest = model.predict(dishonest_customer)

print(f"Refund Prediction (Honest Customer): {prediction_honest[0]}")
print(f"Refund Prediction (Dishonest Customer): {prediction_dishonest[0]}")
