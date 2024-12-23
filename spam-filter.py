import pandas as pd
import os
import get_data 


# Pfade zu den Ordnern
path_ham = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20021010_easy_ham\easy_ham"
path_spam = r"C:\Users\User\Documents\MCI\1_WS_24\Machine_Learing_2\Final_project\Spam-Filter\data\20021010_spam\spam"

get_data.get_dataframe(path_ham, path_spam)
