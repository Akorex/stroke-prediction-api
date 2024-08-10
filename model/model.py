import pickle
from pathlib import Path
import warnings
import pandas as pd
from sklearn.exceptions import InconsistentVersionWarning
warnings.simplefilter("error", InconsistentVersionWarning)
import numpy as np

# BASE_DIR = Path(__file__).resolve(strict=True).parent
new_dir = r"model\stroke-model.pkl"
the_model = None

# try:
#     with open(f"{BASE_DIR}\stroke-model.pkl", "rb") as f:
#        the_model = pickle.load(f)
try:
    with open(r"model\stroke-model.pkl", "rb") as f:
        the_model = pickle.load(f) 
except InconsistentVersionWarning as w:
    print(w.original_sklearn_version)

# print(BASE_DIR)
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
        print(BASE_DIR)
    # print("the model is none")
    return None
    # prediction = model
    return prediction