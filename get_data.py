import pandas as pd
import os

# Pfade zu den Ordnern
#path_ham = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20021010_easy_ham\easy_ham"
#path_spam = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20021010_spam\spam"

# Funktion zum Lesen der Dateien und Hinzufügen eines Labels
def read_files_from_folder(folder_path, label):
    data = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Nur Dateien öffnen
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r", encoding="latin1") as file:
                    content = file.read()
                    data.append({"text": content, "label": label})
            except Exception as e:
                print(f"Fehler beim Lesen der Datei {filename}: {e}")
    return data
def get_dataframe(path_ham, path_spam):

    # Daten aus beiden Ordnern lesen
    ham_data = read_files_from_folder(path_ham, label=0)  # Ham = 0
    spam_data = read_files_from_folder(path_spam, label=1)  # Spam = 1

    # Kombiniere die Daten und erstelle einen DataFrame
    dataset = ham_data + spam_data
    df = pd.DataFrame(dataset)

    # DataFrame anzeigen
    print(df.head())
    print(f"DataFrame enthält {df.shape[0]} Einträge.")



    data_saving = input("do you want to save the dataframe? [y/n]")

    if data_saving=="y":
        print("data was saved to spam_ham_dataset.csv")            
        df.to_csv("spam_ham_dataset.csv", index=False)
    else: 
        print("data wasn`t saved")

