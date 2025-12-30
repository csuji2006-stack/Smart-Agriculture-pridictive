import pandas as pd, joblib
from sklearn.ensemble import RandomForestRegressor, GradientBoostingClassifier

data = pd.read_csv("../data/engineered_data.csv")

X = data[['soil_deficit','temp_humidity_index','rain_effect']]
y_reg = data['water_quantity']
y_cls = data['irrigation_required']

reg = RandomForestRegressor(n_estimators=200)
cls = GradientBoostingClassifier()

reg.fit(X, y_reg)
cls.fit(X, y_cls)

joblib.dump(reg,"water_model.pkl")
joblib.dump(cls,"decision_model.pkl")
print("Advanced ML models saved")