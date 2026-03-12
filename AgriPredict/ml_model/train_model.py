import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("ml_model/crop_price.csv")

# Rename columns to simple names
data = data.rename(columns={
"Cost of Cultivation (`/Hectare) A2+FL": "cost_a2",
"Cost of Cultivation (`/Hectare) C2": "cost_c2",
"Cost of Production (`/Quintal) C2": "production_cost",
"Yield (Quintal/ Hectare) ": "yield",
"Temperature": "temperature",
"Rainfall": "rainfall"
})

# Convert categorical columns
data = pd.get_dummies(data, columns=["Crop","State"])

X = data.drop("Price", axis=1)
y = data["Price"]

# Save column list
pickle.dump(X.columns, open("ml_model/columns.pkl","wb"))

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = LinearRegression()
model.fit(X_train,y_train)

pickle.dump(model, open("ml_model/model.pkl","wb"))

print("Model trained successfully")