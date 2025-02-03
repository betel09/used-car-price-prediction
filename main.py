from fastapi import FastAPI, HTTPException
import pandas as pd
import joblib
import uvicorn

app = FastAPI()

# Load trained model
model = joblib.load("used_car_price_model.pkl")

# Load feature columns
try:
    trained_columns = joblib.load("feature_columns.pkl")
except Exception as e:
    raise RuntimeError(f"Error loading feature_columns.pkl: {e}")

# Expected categorical columns (same as used during training)
categorical_cols = ["Brand", "model", "Transmission", "Owner", "FuelType"]

@app.get("/")
def home():
    return {"message": "Used Car Price Prediction API is running."}

@app.post("/predict")
def predict(data: dict):
    try:
        # Convert input JSON to DataFrame
        input_data = pd.DataFrame([data])

        # Drop unnecessary columns
        drop_columns = ["PostedDate", "AdditionInfo"]
        input_data = input_data.drop(columns=[col for col in drop_columns if col in input_data], errors="ignore")

        # Ensure `kmDriven` is numeric
        input_data["kmDriven"] = input_data["kmDriven"].astype(int)

        # Encode categorical variables
        input_data = pd.get_dummies(input_data, columns=categorical_cols, drop_first=True)

        # Align with training feature set
        input_data = input_data.reindex(columns=trained_columns, fill_value=0)

        # Make prediction
        prediction = model.predict(input_data)

        return {"predicted_price": prediction[0]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
