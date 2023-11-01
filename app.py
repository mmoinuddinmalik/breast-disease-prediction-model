from fastapi import FastAPI
from pydantic import BaseModel
from script.method.implementation import random_forest_test, random_forest_train, random_forest_predict
import numpy as np
import pandas as pd
from script.model.random_forest import accuracy
from time import time

app = FastAPI()

class InputData(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float
    radius_se: float
    texture_se: float
    perimeter_se: float
    area_se: float
    smoothness_se: float
    compactness_se: float
    concavity_se: float
    concave_points_se: float
    symmetry_se: float
    fractal_dimension_se: float
    radius_worst: float
    texture_worst: float
    perimeter_worst: float
    area_worst: float
    smoothness_worst: float
    compactness_worst: float
    concavity_worst: float
    concave_points_worst: float
    symmetry_worst: float
    fractal_dimension_worst: float

# Define a global variable for the model
global clf
clf = random_forest_train()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post('/breastDiseasePredict') 
def login_user(data: InputData):
    # Convert the Pydantic model to a NumPy array
    data_dict = data.dict()
    data_list = [data_dict[attr] for attr in data_dict]
    data_np = np.asarray(data_list, dtype=float)
    data_np = data_np.reshape(1, -1)

    # Make a prediction using the model
    out, acc, t = random_forest_predict(clf, data_np)

    if out == 1:
        output = 'Malignant'
    else:
        output = 'Benign'

    acc_x = acc[0][0]
    acc_y = acc[0][1]
    acc1 = max(acc_x, acc_y)

    return {"output": output, "accuracy": acc1, "time": t}

if __name__ == '__main__':
    # The script will run when executed, and the FastAPI server will start
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
