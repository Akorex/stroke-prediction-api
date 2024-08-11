import pickle
from pathlib import Path
import warnings
import pandas as pd
from sklearn.exceptions import InconsistentVersionWarning
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)
import numpy as np


file_path = r"model\stroke-model.pkl"

try:
    with open(file_path, "rb") as f:
        the_model = pickle.load(f)  
except InconsistentVersionWarning as w:
    print(w.original_sklearn_version)

print(type(the_model))

def process_stroke_data(data): 
    print("printing from process_stroke_data")
    # print(data)
    df = pd.DataFrame([data])
    print(df)
    str_columns = ['sex', 'age', 'bmi', 'average_glucose_level']
    df[str_columns] = df[str_columns].astype(np.float64)
    print(df)
    
    if the_model is not None:
        print("the model is not None")
        # prediction = the_model.predict([df])
        # return prediction
    # print("the model is none")
    return None
    # prediction = model
    return prediction