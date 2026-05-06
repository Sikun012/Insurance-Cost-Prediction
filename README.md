<<<<<<< HEAD
# Insurance-Cost-Prediction
=======
# 🏥 Insurance Cost Prediction – Machine Learning Model Deployment

This project presents a **placement-oriented Machine Learning application** that predicts **medical insurance charges** using user health and demographic data.  
The trained ML model is deployed using **Flask**, exposing a REST API for real-time predictions.

---

## 📌 Project Objective

To build, train, and deploy a **Linear Regression model** that estimates insurance costs based on multiple personal and lifestyle features.

This project highlights:
- End-to-end ML workflow
- Feature engineering & encoding
- Model serialization
- Flask-based deployment

---

## 🧠 Machine Learning Model

- **Algorithm:** Linear Regression  
- **Problem Type:** Regression  
- **Target Variable:** Insurance Charges  

---

## 🧾 Input Features

| Feature | Description |
|------|------------|
| age | Age of the policy holder |
| sex | Gender |
| bmi | Body Mass Index |
| children | Number of dependents |
| smoker | Smoking status |
| region | Residential region |

---

## 🔄 Feature Engineering

- Binary encoding for gender & smoker
- One-hot encoding for region
- BMI category generation (Normal / Overweight / Obese)

---

## 🚀 Flask API

### Endpoint
POST /predict

### Sample Input
```json
{
  "age": 40,
  "sex": "female",
  "bmi": 27.5,
  "children": 2,
  "smoker": "yes",
  "region": "southeast"
}
```

### Sample Output
```json
{
  "prediction": 24350.75
}
```

---

## 🗂 Project Structure
```
insurance-cost-prediction/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── templates/
│   └── index.html
├── notebook/
│   └── model_training.ipynb
└── README.md
```
---

## ⚙️ Tech Stack

Python, Flask, NumPy, Pandas, Scikit-learn

---

## 👤 Author

Priyatam Dash
>>>>>>> 55b86d7 (Initial commit)
