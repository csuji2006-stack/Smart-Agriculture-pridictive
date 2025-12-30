from fastapi import FastAPI
import joblib

app = FastAPI()
reg = joblib.load("../ml/water_model.pkl")
cls = joblib.load("../ml/decision_model.pkl")

@app.post("/predict")
def predict(data: dict):
    X = [[
        100 - data["soil_moisture"],
        data["temperature"] * data["humidity"] / 100,
        data["rainfall"]
    ]]
    water = reg.predict(X)[0]
    decision = cls.predict(X)[0]

    return {
        "irrigation_required": "Yes" if decision else "No",
        "water_quantity_liters": round(water,2)
    }