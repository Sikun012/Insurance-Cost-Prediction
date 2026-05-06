from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load your trained model (you'll need to save it first from the notebook)
# model = pickle.load(open('model.pkl', 'rb'))
# scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Extract features
        age = float(data['age'])
        is_female = int(data['sex'] == 'female')
        bmi = float(data['bmi'])
        children = int(data['children'])
        is_smoker = int(data['smoker'] == 'yes')
        region = data['region']
        
        # Region encoding
        region_southeast = 1 if region == 'southeast' else 0
        region_northwest = 1 if region == 'northwest' else 0
        region_southwest = 1 if region == 'southwest' else 0
        
        # BMI category
        if bmi < 18.5:
            bmi_category_Obese = 0
            bmi_category_Overweight = 0
        elif bmi < 24.9:
            bmi_category_Obese = 0
            bmi_category_Overweight = 0
        elif bmi < 29.9:
            bmi_category_Obese = 0
            bmi_category_Overweight = 1
        else:
            bmi_category_Obese = 1
            bmi_category_Overweight = 0
        
        # Prepare features
        features = np.array([[age, is_female, bmi, children, is_smoker, region_southeast, bmi_category_Obese]])
        
        # Note: You need to save your scaler and model from the notebook
        # scaler.transform() on age, bmi, children columns
        # prediction = model.predict(features)[0]
        
        # For now, returning a mock prediction
        prediction = 5000 + (age * 100) + (bmi * 50) + (is_smoker * 10000)
        
        return jsonify({'prediction': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
