import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('DT_Model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if prediction == 0:
        result = "FlowCool Pressure Dropped Below Limit	Fault"
    elif prediction == 1:
        result = "Flowcool Pressure Too High Check Flowcool Pump Fault"
    elif prediction == 2:
        result = "Flowcool leak	Fault"
    elif prediction == 3:
        result = "No Falut"
        

    return render_template('index.html', prediction_text='{}: {} '.format(prediction,result))


if __name__ == "__main__":
    app.run(debug=True)