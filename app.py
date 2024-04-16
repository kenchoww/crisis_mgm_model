from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load your trained model (make sure to provide the correct file path)
model = joblib.load('/Users/kenneth/Desktop/NTU/Year 2 Sem 2/BC3415 AI /Kenneth_Final_Grp_Project/Crisis Mgm Cloud/model.joblib')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Retrieve all input features from the form and cast them to the expected type
            input_features = [
                float(request.form.get("case")),
                float(request.form.get("cc3")),
                float(request.form.get("country")),
                float(request.form.get("year")),
                float(request.form.get("systematic_crisis")),
                float(request.form.get("exch_usd")),
                float(request.form.get("domestic_debt_in_default")),
                float(request.form.get("sovereign_external_debt_default")),
                float(request.form.get("gdp_weighted_default")),
                float(request.form.get("inflation_annual_cpi")),
                float(request.form.get("independence")),
                float(request.form.get("currency_crises")),
                float(request.form.get("inflation_crises")),
            ]
            
            prediction = model.predict([input_features])[0]  # Predict method may vary based on your model
            
            # Interpret the prediction result
            if prediction == 0:
                result = "No crisis predicted."
            else:
                result = "Crisis predicted!"
            
        except ValueError as e:
            # Handle the error if the input is not a valid number
            result = f"Invalid input: {e}"

        return render_template("index.html", result=result)
    else:
        # When the page is loaded (GET request), show the form without a result
        return render_template("index.html", result="waiting for input...")

if __name__ == "__main__":
    app.run() 
