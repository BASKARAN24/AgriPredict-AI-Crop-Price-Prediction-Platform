
# 🌾 AgriPredict: AI-Powered Smart Farming Assistant

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AgriPredict is a comprehensive Machine Learning platform designed to bridge the gap between traditional farming and data science. It empowers farmers with actionable insights to maximize profit and minimize crop failure.

## 🧠 How It Works

### 1. Market Price Forecasting
The system uses a **Random Forest Regressor** (or your specific model) trained on historical datasets. It doesn't just look at the crop name; it analyzes the correlation between **Cost of Cultivation**, **State-wise Yield**, and **Climate Variables**. 
* **Input:** Crop, State, Rainfall, Temp, Cost, Yield.
* **Output:** Estimated price per quintal.

### 2. Crop Recommendation Engine
This module uses a **Multi-class Classification algorithm**. By feeding it the chemical composition of your soil (NPK) and local climate data, the model maps these variables to the optimal crop type.
* **The Logic:** If $N > 90$ and $Rainfall > 200mm$, the model leans heavily toward water-intensive crops like Rice.

### 3. Real-time Environmental Sync
Instead of manual entry, the weather module fetches live JSON data from the **OpenWeatherMap API**. This provides a real-time snapshot of humidity and wind speed, which are critical for determining the right time to apply fertilizers.

## 🛠️ Tools & Technologies

| Category | Tools |
| :--- | :--- |
| **Backend** | Python, Flask |
| **Machine Learning** | Scikit-Learn, Pandas, NumPy, Pickle |
| **Frontend** | HTML5, CSS3 (Glassmorphism), JavaScript, Chart.js |
| **Data API** | OpenWeatherMap API |
| **Environment** | VS Code, Pip, Virtualenv |

## ⚙️ Quick Start
Clone & Install:


git clone [https://github.com/your-username/AgriPredict.git](https://github.com/your-username/AgriPredict.git)
pip install flask pandas numpy scikit-learn requests
API Configuration:
In app.py, insert your API Key:

WEATHER_API_KEY = "your_openweathermap_key_here"
Launch:


python app.py
## Screenshots
### Home page
<img width="1920" height="1080" alt="Screenshot (491)" src="https://github.com/user-attachments/assets/bd4dd6ec-905e-4645-9b23-b7fb8d30fb26" />

---
### Price prediction page
<img width="1920" height="1080" alt="Screenshot (494)" src="https://github.com/user-attachments/assets/109fbdf3-a1d7-4536-8261-83bfca55ab19" />
<img width="1920" height="1080" alt="Screenshot (495)" src="https://github.com/user-attachments/assets/ccb65cd4-7e26-488d-9900-fefa4f3486b2" />
<img width="1920" height="1080" alt="Screenshot (496)" src="https://github.com/user-attachments/assets/f2f12b4b-5aa1-40c3-8bbb-5d9c2fbab834" />

---
### Crop Recommendation page
<img width="1920" height="1080" alt="Screenshot (497)" src="https://github.com/user-attachments/assets/a41bcc89-73ad-4e8b-afc8-121adbf73f20" />
<img width="1920" height="1080" alt="Screenshot (498)" src="https://github.com/user-attachments/assets/1c272c0d-6de4-4c09-93ca-e776928289f7" />
<img width="1920" height="1080" alt="Screenshot (499)" src="https://github.com/user-attachments/assets/645f7604-4df2-4a6f-a5b5-503f22988ad0" />

---
###  Weather Alerts
<img width="1920" height="1080" alt="Screenshot (500)" src="https://github.com/user-attachments/assets/e6c73820-fa50-457a-b422-9da8b489889d" />
<img width="1920" height="1080" alt="Screenshot (503)" src="https://github.com/user-attachments/assets/724f34cc-10a9-463a-8f34-168fb3aba044" />
<img width="1920" height="1080" alt="Screenshot (504)" src="https://github.com/user-attachments/assets/0b5ab77d-1597-4eb1-951b-2f79b43fd951" />



---
### Market trend analysis
<img width="1920" height="1080" alt="Screenshot (501)" src="https://github.com/user-attachments/assets/0532b6ed-8f7d-4065-80f6-5dd0b68c74d2" />

---

## 📂 Project Structure

```text
AgriPredict/
├── app.py              # Flask server & API routing logic
├── ml_model/           # Serialized (.pkl) ML models
├── templates/          # UI Components (Home, Predict, Recommend, etc.)
└── static/             # Styling & Asset management





