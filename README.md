# Breat Disease Prediction Model
## Model Developed by M. Moin Uddin Malik

### Prediction Model live implemented in e-hospital website

# FastAPI Breast Disease Predictor

This project provides a FastAPI-based REST API for predicting breast diseases using a trained machine learning model. It accepts input data related to breast cancer features and returns predictions and accuracy.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup and Usage](#setup-and-usage)
- [Making Predictions](#making-predictions)
- [Sample Example with Postman](#sample-example-with-postman)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Breast cancer is one of the most common cancers among women, and early detection is crucial for effective treatment. This project aims to provide a simple and easy-to-use REST API for predicting breast disease using a trained machine learning model. The model has been developed using breast cancer features, and it can predict whether a tumor is malignant or benign.

## Setup and Usage

1. **Installation**:

   Before you can use the API, you need to set up the project and install the necessary dependencies. You can do this using the following steps:

   - Clone the repository:

     ```bash
     git clone <repository-url>
     cd fastapi-breast-disease-predictor
     ```

   - Install Python dependencies:

     ```bash
     pip install -r requirements.txt
     ```

2. **Run the API**:

   The FastAPI server can be started using the following command:

   ```bash
   python -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

   The API will be accessible at http://0.0.0.0:8000.

## Making Predictions

    You can make predictions by sending a POST request to the /breastDiseasePredict endpoint. The API expects input data related to breast cancer features.

    - Input Data Fields

   ```json
   {
        "radius_mean": 17.99,
        "texture_mean": 10.38,
        "perimeter_mean": 122.8,
        "area_mean": 1001,
        "smoothness_mean": 0.1184,
        "compactness_mean": 0.2776,
        "concavity_mean": 0.3001,
        "concave_points_mean": 0.1471,
        "symmetry_mean": 0.2419,
        "fractal_dimension_mean": 0.07871,
        "radius_se": 1.095,
        "texture_se": 0.9053,
        "perimeter_se": 8.589,
        "area_se": 153.4,
        "smoothness_se": 0.006399,
        "compactness_se": 0.04904,
        "concavity_se": 0.05373,
        "concave_points_se": 0.01587,
        "symmetry_se": 0.03003,
        "fractal_dimension_se": 0.006193,
        "radius_worst": 25.38,
        "texture_worst": 17.33,
        "perimeter_worst": 184.6,
        "area_worst": 2019,
        "smoothness_worst": 0.1622,
        "compactness_worst": 0.6656,
        "concavity_worst": 0.7119,
        "concave_points_worst": 0.2654,
        "symmetry_worst": 0.4601,
        "fractal_dimension_worst": 0.1189
    }
   ```
   
## Sample Example with Postman
    
    Here's a sample example of making a prediction using Postman:

    1. Endpoint: http://0.0.0.0:8000/breastDiseasePredict
    2. HTTP Method: POST
    3. Request Body: JSON with input data fields (as shown in the "Input Data Fields" section)

    - Example response:

    ```json
    {
        "output": "Malignant",
        "accuracy": 0.95,
        "time": 0.055
    }
    ```