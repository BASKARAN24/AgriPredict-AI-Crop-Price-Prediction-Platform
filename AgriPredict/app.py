from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
import requests
WEATHER_API_KEY = "4c5d77ec6b0ee65b2c9bc7815336b655"
app = Flask(__name__)

# --- Load Models & Data ---
try:
    price_model = pickle.load(open("ml_model/model.pkl", "rb"))
    columns = pickle.load(open("ml_model/columns.pkl", "rb"))
    recommend_model = pickle.load(open("ml_model/recommend_model.pkl", "rb"))
except FileNotFoundError:
    print("Error: Model files not found. Please run training scripts first.")

# --- Navigation Routes ---

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/price")
def price_page():
    return render_template("predict.html")

@app.route("/recommend")
def recommend_page():
    return render_template("recommend.html")





# --- Logic Routes ---

@app.route("/predict_price", methods=["POST"])
def predict_price():
    # Extraction from form
    crop = request.form["crop"]
    state = request.form["state"]
    rainfall = float(request.form["rainfall"])
    temp = float(request.form["temperature"])
    yield_val = float(request.form["yield"])
    cost = float(request.form["cost"])

    # Prepare input DataFrame
    input_df = pd.DataFrame([[0]*len(columns)], columns=columns)
    input_df["rainfall"] = rainfall
    input_df["temperature"] = temp
    input_df["yield"] = yield_val
    input_df["cost_a2"] = cost

    # Handle dummy variables
    crop_col = "Crop_" + crop
    state_col = "State_" + state
    if crop_col in input_df.columns: input_df[crop_col] = 1
    if state_col in input_df.columns: input_df[state_col] = 1

    prediction = price_model.predict(input_df)
    return render_template("predict.html", result=round(prediction[0], 2))

@app.route("/predict_recommend", methods=["POST"])
def predict_recommend():
    features = [
        float(request.form['n']),
        float(request.form['p']),
        float(request.form['k']),
        float(request.form['temperature']),
        float(request.form['humidity']),
        float(request.form['ph']),
        float(request.form['rainfall'])
    ]
    prediction = recommend_model.predict([features])
    return render_template("recommend.html", result=prediction[0].capitalize())
# ----------weather----------------
@app.route("/weather", methods=["GET", "POST"])
def weather_page():
    weather_data = None
    city = None
    
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
            response = requests.get(url).json()
            
            if response.get("cod") == 200:
                weather_data = {
                    "temp": response["main"]["temp"],
                    "humidity": response["main"]["humidity"],
                    "desc": response["weather"][0]["description"].capitalize(),
                    "icon": response["weather"][0]["icon"],
                    "wind": response["wind"]["speed"],
                    "city": response["name"]
                }
            else:
                weather_data = "error"

    return render_template("weather.html", weather=weather_data)
#---------------trends--------------
@app.route("/trends")
def trends_page():
    graph_data = {
        "months": ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar"],
        "prices": [1800, 1950, 2100, 2050, 2200, 2350]
    }
    return render_template("trends.html", data=graph_data)
if __name__ == "__main__":
    app.run(debug=True)