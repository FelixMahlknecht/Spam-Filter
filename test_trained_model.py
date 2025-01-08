import os
import joblib
import pandas as pd 

test_path = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20021010_hard_ham\hard_ham"
vectorize = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\vectorizer.pkl"
model_path = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\naive_bayesModel.pkl"


vectorizer = joblib.load(vectorize)
model = joblib.load(model_path)

def load_emails_from_folder(folderpath):
    emails = []
    filenames = []
    
    for filename in os.listdir(folderpath):
        file_path = os.path.join(folderpath, filename)
        if os.path.isfile(file_path):
            with open (file_path, "r", encoding="latin1") as file:
                emails.append(file.read())
                filenames.append(filename)
    
    return emails,filenames

emails, filenames = load_emails_from_folder(test_path)

# vectorize emails

email_vectors = vectorizer.transform(emails)

predictions = model.predict(email_vectors)

counter = 0
spamcounter = 0
hamcounter = 0

for filename, prediction in zip(filenames, predictions):
    counter = counter +1
    
    if prediction == 1:
        spamcounter= spamcounter +1 
        label = "spam"
    else:
        hamcounter = hamcounter +1   
        label = "ham" 
 
    print(f"email: {filename} -> vorhersage:{label}")

percantage_spam = (spamcounter/counter)*100
percantage_ham = (hamcounter/counter) * 100

print(f"the percentage of spam is {percantage_spam} and this is the percentage of ham {percantage_ham}")

