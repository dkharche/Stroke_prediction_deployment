from flask import Flask , render_template
from flask import request
import numpy as np

import pickle
model = pickle.load(open('model3.pkl', 'rb'))
app = Flask(__name__ ,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict' ,methods = ['POST'])
def predict_stroke():
    gender = request.form.get('gender')
    age = request.form.get('age')
    hypertension = request.form.get('hypertension')
    heart_disease = request.form.get('heart_disease')
    ever_married = request.form.get('ever_married')
    work_type = request.form.get('work_type')
    residence_type = request.form.get('residence_type')
    avg_glucose_level = request.form.get('avg_glucose_level')
    bmi = request.form.get('bmi')
    smoking_status = request.form.get('smoking_status')


    result=model.predict(np.array([gender,age,hypertension,heart_disease,ever_married,work_type,residence_type,avg_glucose_level,bmi
                                   ,smoking_status]))
    return str(result)



if __name__ == '__main__':
    app.run(debug=True)