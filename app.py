from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

# ✅ Correct
import joblib

model_path = 'profit_prediction_model.pkl'
model = None
try:
    model = joblib.load(model_path)
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model: {e}")


@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    return render_template('index.html', prediction=prediction)


@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form.to_dict()
    try:
        # Get input values from form
        investment = float(request.form['investment'])
        employees = float(request.form['employees'])
        daily_customers = float(request.form['daily_customers'])
        monthly_expenses = float(request.form['monthly_expenses'])
        monthly_revenue = float(request.form['monthly_revenue'])
        business_type = request.form['business_type']
        location = request.form['location']

        # ✅ Use exact column names from training data
        input_data = pd.DataFrame([{
            'Investment': investment,
            'Employees': employees,
            'Daily_Customers': daily_customers,
            'Monthly_Expenses': monthly_expenses,
            'Monthly_Revenue': monthly_revenue,
            'Business_Type': business_type,
            'Location': location
        }])

        prediction = model.predict(input_data)[0]

        return render_template('index.html',  prediction=round(prediction, 2))
        
   
    except Exception as e:
        print("❌ Error in predict function:", str(e))
        return render_template('index.html', error=str(e))

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
