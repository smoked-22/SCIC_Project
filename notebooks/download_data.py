import numpy as np
import os
import pandas as pd
# import urllib.request

# Data path
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/Jaehun-Kim22/SCIC_Project/master/"
DATA_PATH = os.path.join("assets")
DATA_URL = DOWNLOAD_ROOT + "assets/training_data.csv"


print(DATA_URL)
def load_data(data_path=DATA_URL, encoding = 'utf-8'):
    return pd.read_csv(data_path)


data = load_data()
data.head()