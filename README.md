# 📊 Customer Churn Prediction – End-to-End Machine Learning Project

This project is an end-to-end **Customer Churn Prediction system** built using **Machine Learning and Flask**.  
It predicts whether a customer is likely to churn, helping businesses take proactive retention actions.

---

## 🚀 Key Features

- Exploratory Data Analysis (EDA)
- Data preprocessing & feature engineering
- Machine Learning model training (Random Forest)
- Model evaluation with performance metrics
- Model serialization using `model.pkl` and `scaler.pkl`
- REST API built with Flask for real-time predictions

---

## 🧠 Machine Learning Pipeline

1. Load customer churn dataset
2. Perform data cleaning and encoding
3. Split data into training and testing sets
4. Scale features using StandardScaler
5. Train Random Forest Classifier
6. Evaluate model performance
7. Save trained model and scaler as `.pkl` files
8. Deploy model using Flask API

---

## 📁 Project Structure

Customer-Churn-Prediction/
│
├── data/
│ └── churn_data.csv
│
├── model/
│ ├── model.pkl
│ └── scaler.pkl
│
├── notebook/
│ └── churn_prediction.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore


---

## 🛠️ Tech Stack

- Python
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- joblib
- Flask

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/your-username/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
pip install -r requirements.txt


## 🧪 Train the Model

Run the Jupyter Notebook:

notebook/churn_prediction.ipynb

This will generate:

-model/model.pkl

-model/scaler.pkl 

🌐 Run the Flask API

python app.py


Server will start at:

http://127.0.0.1:5000/

🔮 API Endpoint

POST /predict

Sample Request
{
  "feature1": 45,
  "feature2": 1,
  "feature3": 120.5,
  "feature4": 0
}

Sample Response
{
  "churn_prediction": 1
}


1 → Customer likely to churn

0 → Customer not likely to churn

📈 Future Improvements

Add more ML models (XGBoost, Logistic Regression)

Hyperparameter tuning

Frontend UI (Streamlit / React)

Docker & Cloud Deployment

👤 Author

Kunjan A. Minama