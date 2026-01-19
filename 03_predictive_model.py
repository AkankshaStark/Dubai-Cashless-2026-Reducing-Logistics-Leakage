import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# 1. Load data
df = pd.read_csv('dubai_cashless_2026_data.csv')

# 2. Feature Engineering: Selecting relevant predictors
# We exclude IDs and Timestamps but keep business-critical features
features = ['District', 'Payment_Method', 'Order_Value_AED', 'Distance_KM', 'Temperature_C', 'Is_Ramadan']
X = pd.get_dummies(df[features], drop_first=True) # Convert text to numbers
y = df['RTO_Flag']

# 3. Train/Test Split (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2026)

# 4. Initialize and Train the model
model = RandomForestClassifier(n_estimators=100, random_state=2026)
model.fit(X_train, y_train)

# 5. Evaluate Performance
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 6. Save the model for later use in our dashboard/app
joblib.dump(model, 'rto_predictor_model.pkl')
joblib.dump(X_train.columns.tolist(), 'model_columns.pkl')