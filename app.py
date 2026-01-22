from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("customer_churn_model.pkl")
scaler = joblib.load("encoders.pkl")

@app.route("/")
def home():
    return {"message": "Customer Churn Prediction API"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    values = np.array(list(data.values())).reshape(1, -1)

    values_scaled = scaler.transform(values)
    prediction = model.predict(values_scaled)

    return jsonify({"churn_prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
