from google.colab import files
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
import io

# Manually upload the 'spam.csv' file
uploaded = files.upload()

# Get the first uploaded file
file_key = next(iter(uploaded))

# Read the dataset
df = pd.read_csv(io.StringIO(uploaded[file_key].decode('latin1')))

# Print column names
print("Column Names:", df.columns)

# Separate data and labels
X = df['Message']
y = df['Category']

# Convert text labels to numerical values
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text data into feature vectors using TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_tfidf, y_train)

# Train a Support Vector Machine (SVM) classifier
svm_classifier = SVC()
svm_classifier.fit(X_train_tfidf, y_train)

# Train a Random Forest classifier
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train_tfidf, y_train)

# Train a Decision Tree classifier
dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X_train_tfidf, y_train)

# Train a Multi-Layer Perceptron (MLP) classifier
mlp_classifier = MLPClassifier()
mlp_classifier.fit(X_train_tfidf, y_train)

# List of classifiers for iteration
classifiers = [
    ('Naive Bayes', nb_classifier),
    ('Support Vector Machine', svm_classifier),
    ('Random Forest', rf_classifier),
    ('Decision Tree', dt_classifier),
    ('Multi-Layer Perceptron', mlp_classifier)
]

# Evaluate each classifier
for clf_name, classifier in classifiers:
    predictions = classifier.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, predictions)
    conf_matrix = confusion_matrix(y_test, predictions)
    class_report = classification_report(y_test, predictions)

    print(f"\n{clf_name} Classifier:")
    print(f"Accuracy: {accuracy:.2f}")
    print("Confusion Matrix:")
    print(conf_matrix)
    print("Classification Report:")
    print(class_report)
