# 🌾 Smart Agriculture – Predictive Irrigation System (Advanced)

An advanced Machine Learning and IoT-based system that predicts irrigation
requirements and optimal water quantity using simulated sensor data, real-time
MQTT streaming, feature engineering, and ensemble ML models.

This project follows an industry-style architecture using MQTT, FastAPI,
Scikit-learn, and Streamlit, making it suitable for final-year engineering
projects and real-world smart agriculture applications.

---

## 📌 Problem Statement
Farmers often over-irrigate crops due to the lack of predictive insights.
This project builds a predictive irrigation system that analyzes soil and
weather conditions to determine whether irrigation is required and how much
water should be supplied.

---

## 🎯 Objectives
- Simulate real-time IoT sensor data
- Stream data using MQTT protocol
- Store sensor data reliably in a database
- Perform advanced feature engineering
- Train ensemble ML models for prediction
- Expose predictions via FastAPI REST services
- Visualize results using an interactive dashboard

---

## 🧠 System Architecture

Sensor Simulator  
→ MQTT Broker (Mosquitto)  
→ Data Collector Service  
→ Database  
→ Feature Engineering  
→ ML Models  
→ FastAPI Prediction Service  
→ Streamlit Dashboard  

---

## 🛠 Technologies Used

### IoT & Data Streaming
- MQTT Protocol
- Mosquitto Broker
- Paho-MQTT

### Backend & APIs
- Python
- FastAPI
- REST APIs

### Machine Learning
- NumPy
- Pandas
- Scikit-learn
- Ensemble Models (Random Forest, Gradient Boosting)

### Visualization
- Streamlit

### Database
- SQLite

---

## 📂 Project Structure

```
api.py                    # FastAPI prediction service
backend_mqtt_subscriber.py # MQTT data collector
dashboard.py              # Streamlit interactive dashboard
ml_engineering.py         # Feature engineering utilities
model_logger.py           # Model logging and monitoring
model_training.py         # ML model training scripts
mqttt_publisher.py        # MQTT sensor data publisher
requirements.txt          # Python dependencies
docs/                     # GitHub Pages website
  ├── index.html
  ├── style.css
  └── script.js
.github/
  └── workflows/
      └── deploy.yml      # GitHub Actions for Pages deployment
```

---

## 🌐 Website & Deployment

This project includes a static website hosted on GitHub Pages that showcases the system.

### Local Development
1. Clone the repository
2. Navigate to `docs/` folder
3. Open `index.html` in your browser

### GitHub Pages Deployment
The website is automatically deployed to GitHub Pages using GitHub Actions:

1. Create a new repository on GitHub
2. Push this code to your repository:
   ```bash
   git remote add origin https://github.com/yourusername/smart-agriculture.git
   git branch -M main
   git push -u origin main
   ```
3. Go to repository Settings > Pages
4. Under Source, select "Deploy from a branch"
5. Select branch `main` and folder `/docs`
6. Save - your site will be available at `https://yourusername.github.io/smart-agriculture`

The GitHub Actions workflow will also deploy automatically on each push to main.

### Running the Full Application
1. Install dependencies: `pip install -r requirements.txt`
2. Start MQTT broker (Mosquitto)
3. Run data collector: `python backend_mqtt_subscriber.py`
4. Run API server: `uvicorn api:app --reload`
5. Run dashboard: `streamlit run dashboard.py`

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.