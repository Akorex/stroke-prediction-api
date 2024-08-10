
import warnings
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model.model import process_stroke_data
from sklearn.ensemble import RandomForestClassifier


class StrokeModel(BaseModel):
    sex: int    
    age: str
    hypertension: int
    heart_disease: int
    ever_married: int
    work_type: int
    residence_type: int 
    average_glucose_level: str
    bmi: str
    smoking_status: int

class StrokeEntity(BaseModel):
    sex: int     
    age: int
    hypertension: int
    heart_disease: int
    ever_married: int
    work_type: int
    residence_type: int 
    average_glucose_level: int
    bmi: int
    smoking_status: int

class StrokeResult(BaseModel):
    stroke: int



# with open('stroke-model.pkl', 'rb') as f:
#     model = pickle.load(f)

# origins = ["http://localhost:5173/"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.post("/predict/")
async def predict_stroke(data: StrokeModel):
    age = data.age
    bmi = data.bmi
    average_glucose_level = float(data.average_glucose_level)
    # print(f"{age}, {bmi}, {average_glucose_level}")
    # print(data)
    predictions = process_stroke_data(data.model_dump())
    print(f"This is the prediction {predictions}")

    
    return {"data": data}


@app.get("/")
async def get_root():
    return {"message": "Hello World"}