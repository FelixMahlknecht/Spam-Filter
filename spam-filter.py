import pandas as pd
import os
import get_data
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib


# Pfade zu den Ordnern
path_ham = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20021010_easy_ham\easy_ham"
path_spam = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20021010_spam\spam"

#get_data.get_dataframe(path_ham, path_spam)

df = pd.read_csv(r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\spam_ham_dataset.csv")

x_train, x_test, y_train, y_test = train_test_split(df["text"],df["label"], test_size=0.2,random_state=42 )
vectorize = TfidfVectorizer(stop_words="english",max_features=5000)
x_train_vec = vectorize.fit_transform(x_train)
x_test_vec = vectorize.transform(x_test)

model = MultinomialNB()
model.fit(x_train_vec, y_train)

y_pred = model.predict(x_test_vec)

#save modell for later use

joblib.dump(vectorize, "vectorizer.pkl")
joblib.dump(model, "naive_bayesModel.pkl")

# Genauigkeit
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Klassifikationsbericht
print("Classification Report:")
print(classification_report(y_test, y_pred))





