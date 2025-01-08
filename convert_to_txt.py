import os

# write the absolute folder path
folder_path = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20021010_hard_ham\hard_ham"
# got through every file
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    print(f"Überprüfe: {file_path}")
    
    # only change files not the folder
    if os.path.isfile(file_path):
        print(f"Datei gefunden: {filename}")
        
        # New filename with .txt ending
        new_filename = os.path.splitext(filename)[0] + ".txt"
        new_file_path = os.path.join(folder_path, new_filename)
        
        # Datei umbenennen
        try:
            os.rename(file_path, new_file_path)
            print(f"Umgewandelt: {filename} -> {new_filename}")
        except Exception as e:
            print(f"Fehler beim Umbenennen von {filename}: {e}")
    else:
        print(f"Kein reguläres File: {filename}")
