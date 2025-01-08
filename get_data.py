import pandas as pd
import os

# Path to the folders
#path_ham = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20021010_easy_ham\easy_ham"
#path_spam = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20021010_spam\spam"

# Function to read the files
def read_files_from_folder(folder_path, label):
    data = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Open only
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r", encoding="latin1") as file:
                    content = file.read()
                    data.append({"text": content, "label": label})
            except Exception as e:
                print(f"Fehler beim Lesen der Datei {filename}: {e}")
    return data


def get_dataframe_training(path, type):
    
    if type == 1 or "spam":
        data = read_files_from_folder(path, label = 1)
    elif type == 0 or "ham":
        data = read_files_from_folder(path,label = 0)
    else:
        print("please enter a valid type, (spam or ham) or (1 0)")
        
    dataset = dataset.append(data)
    df = pd.DataFrame(dataset)
    return df

def data_saving(df):
    
    user = input("do you want to save the dataframe? [y/n]")

    if user=="y":
        print("data was saved to spam_ham_dataset.csv")            
        df.to_csv("spam_ham_dataset.csv", index=False)
    else: 
        print("data wasn`t saved")
