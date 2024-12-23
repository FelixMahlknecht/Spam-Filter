import os

# Ordnerpfad angeben
folder_path = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data_spam_and_ham\20021010_spam\spam"

# Alle Dateien im Ordner durchgehen
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    print(f"Überprüfe: {file_path}")
    
    # Nur Dateien bearbeiten, keine Ordner
    if os.path.isfile(file_path):
        print(f"Datei gefunden: {filename}")
        
        # Neuer Dateiname mit .txt-Endung
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
