import pandas as pd

df = pd.read_csv("../data/sensor_data.csv")

df["soil_deficit"] = 100 - df["soil_moisture"]
df["temp_humidity_index"] = df["temperature"] * df["humidity"] / 100
df["rain_effect"] = df["rainfall"].rolling(3).mean().fillna(0)

df.to_csv("../data/engineered_data.csv", index=False)
print("Advanced features generated")
