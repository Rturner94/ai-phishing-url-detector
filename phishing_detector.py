# phishing_detector.py

# Import Python libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv("phishing_dataset.csv")

print("Preview of dataset:")
print(df.head())
print("\nColumn names:")
print(df.columns)

# Separate features and labels
X = df.drop(['url', 'status'], axis=1)
y = df['status'].map({'phishing': 1, 'legitimate': 0})
df.drop(['status'], axis=1).head(20).to_csv("test_input_compatible.csv", index=False)




# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))
