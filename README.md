# 📈 Profit Prediction Web App

This is a Flask-based web application that predicts the potential profit of a business based on user input. It uses a trained machine learning model and dynamically adapts the form fields based on the selected business type.

---

## 🚀 Features

- Simple and interactive UI using Bootstrap
- Form adapts to different business types
- Machine Learning based profit prediction
- Clear output with result interpretation
- Modular structure with Flask templates

---

## 🔧 Technologies Used

- Python
- Flask
- HTML, CSS, Bootstrap
- Scikit-learn (for model)
- Jinja2 (templating)

---

## 🧠 Business Types Supported

1. Grocery Store  
2. Restaurant  
3. Online Business  

Each has a unique input form.

---

## 📂 Project Structure

profit-predictor/
│
├── app.py # Main Flask App
├── model/
│ └── profit_model.pkl # Trained ML Model
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── form.html
│ └── result.html
├── static/
│ └── style.css
└── README.md # You're here!