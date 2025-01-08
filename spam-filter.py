import pandas as pd
import os
import get_data  # Importiere deine get_data-Funktion
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

# List with path and types (1 = Spam, 0 = Ham)
paths_and_types = [
    (r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20021010_easy_ham\easy_ham", "ham"),
    (r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20021010_spam\spam", "spam"),
    (r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20050311_spam_2\spam_2", "spam")
]

# Initialize the DataFrame
dataset = []

# Loop through every file
for path, type_ in paths_and_types:
    print(f"Lese Daten aus: {path} (Typ: {type_})")
    data = get_data.read_files_from_folder(path, label=1 if type_ == "spam" else 0)
    dataset.extend(data)  # add data to the set

# create dataframe
df = pd.DataFrame(dataset)
print(f"DataFrame enthält {df.shape[0]} Einträge.")

# save if necessary
get_data.data_saving(df)

# Train-Test-Split
x_train, x_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

# TF-IDF Vektorize
vectorize = TfidfVectorizer(stop_words="english", max_features=5000)
x_train_vec = vectorize.fit_transform(x_train)
x_test_vec = vectorize.transform(x_test)

# Naive Bayes Modell
model = MultinomialNB()
model.fit(x_train_vec, y_train)

# predictions
y_pred = model.predict(x_test_vec)

y_train_pred = model.predict(x_train_vec)
print(f"Training Accuracy: {accuracy_score(y_train, y_train_pred):.2f}")
print(classification_report(y_train, y_train_pred))


# save trained modell and victorizer
joblib.dump(vectorize, "vectorizer.pkl")
joblib.dump(model, "naive_bayesModel.pkl")

# accuracy
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# classification
print("Classification Report:")
print(classification_report(y_test, y_pred))
