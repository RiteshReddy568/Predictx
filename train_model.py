import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

normal = pd.read_csv('normal.csv')
high_temp = pd.read_csv('high_temp.csv')
obstruction = pd.read_csv('motor_obstruction.csv')
voltage = pd.read_csv('voltage_fluctuation.csv')

normal['label'] = 0
high_temp['label'] = 1
obstruction['label'] = 2
voltage['label'] = 3


data = pd.concat([normal, high_temp, obstruction, voltage], ignore_index=True)

X = data[['vibration', 'temperature', 'current', 'voltage']]
y = data['label']


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)


joblib.dump(model, 'model.pkl')
print("✅ Multi-class model trained via explicit separate files!")