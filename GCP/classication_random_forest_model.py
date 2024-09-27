import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import argparse
import seaborn as sns
import matplotlib.pyplot as plt

# Set up argument parser
parser = argparse.ArgumentParser(description='Train Random Forest model to predict tag_class_number.')
parser.add_argument('csv_file', type=str, help='Path to the input CSV file')

args = parser.parse_args()

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(args.csv_file)

# Define the feature columns and the target column
features = [
    'aspect_ratio', 'area', 'perimeter', 'surface_structure', 
    'solidity', 'circularity'
]
target = 'tag_class_number'

# Handle missing values (optional step: drop or fill)
df = df.dropna(subset=features + [target])  # Ensure no missing values

# Split the data into training and testing sets (80% train, 20% test)
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict the test set
y_pred = model.predict(X_test)

# Calculate accuracy metrics
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Output results
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(class_report)

# Display the confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('Actual Class')
plt.xlabel('Predicted Class')
plt.show()
